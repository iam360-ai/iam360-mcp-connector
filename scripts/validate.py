#!/usr/bin/env python3
"""Validate this public connector package without credentials or private calls."""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import re
import struct
import sys
import tomllib
import urllib.error
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
ENDPOINT = "https://app.iam360.ai/api/mcp"
REPOSITORY = "https://github.com/iam360-ai/iam360-mcp-connector"
errors: list[str] = []


def check(condition: bool, message: str) -> None:
    if not condition:
        errors.append(message)


def read_json(relative: str) -> dict:
    try:
        data = json.loads((ROOT / relative).read_text())
        if not isinstance(data, dict):
            raise ValueError("root must be an object")
        return data
    except (OSError, ValueError) as exc:
        errors.append(f"{relative}: {exc}")
        return {}


def headings(text: str) -> set[str]:
    anchors: set[str] = set()
    counts: dict[str, int] = {}
    for title in re.findall(r"^#{1,6}\s+(.+?)\s*#*\s*$", text, re.MULTILINE):
        base = re.sub(r"[^\w\- ]", "", title.lower()).replace(" ", "-")
        count = counts.get(base, 0)
        counts[base] = count + 1
        anchors.add(base if not count else f"{base}-{count}")
    return anchors


def check_remote(url: str) -> tuple[str, str]:
    parsed = urllib.parse.urlsplit(url)
    host, path = parsed.netloc, parsed.path
    social_hosts = {"www.instagram.com", "x.com", "www.linkedin.com", "www.youtube.com", "www.tiktok.com"}
    login_only = (
        host in {"chatgpt.com", "grok.com"}
        or (host == "app.iam360.ai" and (path.startswith("/dashboard/") or path == "/plans"))
    )
    if host in social_hosts or login_only:
        return "SKIP", url
    request = urllib.request.Request(url, headers={"User-Agent": "iAM360-connector-docs-check/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            response.read(1)
            return str(response.status), url
    except urllib.error.HTTPError as exc:
        if exc.code in {401, 403, 429}:
            return f"REVIEW {exc.code}", url
        return f"FAIL {exc.code}", url
    except (OSError, urllib.error.URLError) as exc:
        return f"REVIEW {type(exc).__name__}", url


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check-links", action="store_true", help="read public linked pages; never authenticate")
    args = parser.parse_args()

    expected = {
        "mcp.json": {"mcpServers": {"iam360": {"url": ENDPOINT}}},
        "configs/cursor.json": {"mcpServers": {"iam360": {"url": ENDPOINT}}},
        "configs/claude-code.json": {"mcpServers": {"iam360": {"type": "http", "url": ENDPOINT}}},
        "configs/vscode.json": {"servers": {"iam360": {"type": "http", "url": ENDPOINT}}},
        "configs/copilot-cli.json": {"mcpServers": {"iam360": {"type": "http", "url": ENDPOINT, "tools": ["*"]}}},
        "configs/gemini-cli.json": {"mcpServers": {"iam360": {"httpUrl": ENDPOINT, "oauth": {"enabled": True, "scopes": ["fitness", "offline_access"]}}}},
        "configs/devin.json": {"mcpServers": {"iam360": {"url": ENDPOINT, "transport": "http"}}},
    }
    for name, value in expected.items():
        check(read_json(name) == value, f"{name}: expected documented client schema/endpoint")

    gemini = read_json("gemini-extension.json")
    check(set(gemini) == {"name", "version", "description", "mcpServers"}, "Gemini extension must contain only identity and remote MCP configuration")
    check(gemini.get("name") == "iam360-mcp-connector", "Gemini extension name must match the repository directory")
    check(isinstance(gemini.get("version"), str) and re.fullmatch(r"\d+\.\d+\.\d+", gemini["version"]) is not None, "Gemini extension version must use major.minor.patch")
    check(isinstance(gemini.get("description"), str) and bool(gemini["description"].strip()), "Gemini extension must have a description")
    check(gemini.get("mcpServers") == expected["configs/gemini-cli.json"]["mcpServers"], "Gemini extension must match the documented OAuth HTTP configuration without credentials or trust overrides")
    for component in ["GEMINI.md", "hooks", "commands", "agents", "skills", "policies"]:
        check(not (ROOT / component).exists(), f"remote-only Gemini extension must not add {component}")

    try:
        codex = tomllib.loads((ROOT / "configs/codex.toml").read_text())
        check(codex == {"mcp_servers": {"iam360": {"url": ENDPOINT, "scopes": ["fitness", "offline_access"]}}}, "Codex TOML differs from documented configuration")
    except (OSError, ValueError) as exc:
        errors.append(f"Codex TOML: {exc}")

    manifest = read_json(".cursor-plugin/plugin.json")
    check(manifest.get("name") == "iam360", "plugin name must be iam360")
    check(manifest.get("displayName") == "iAM360", "plugin display name must be iAM360")
    check(manifest.get("repository") == REPOSITORY, "plugin repository must use canonical owner")
    check(manifest.get("mcpServers") == "mcp.json", "plugin must point at mcp.json")
    check(manifest.get("author") == {"name": "iAM360"}, "plugin author must not contain personal contact details")
    check(manifest.get("license") == "MIT", "plugin license must match LICENSE")
    check(not (ROOT / ".cursor-plugin/marketplace.json").exists(), "single-plugin package must not include marketplace.json")
    check(not any(key in manifest for key in ["hooks", "commands", "agents"]), "remote-only connector must not add local execution components")
    try:
        logo = ROOT / manifest.get("logo", "")
        check(logo.resolve().is_relative_to(ROOT), "logo path must remain in repository")
        image = logo.read_bytes()
        check(image[:8] == b"\x89PNG\r\n\x1a\n" and struct.unpack(">II", image[16:24]) == (512, 512), "logo must be the 512x512 PNG")
    except (OSError, struct.error) as exc:
        errors.append(f"logo: {exc}")

    documents = {p: p.read_text() for p in ROOT.rglob("*.md") if ".git" not in p.parts}
    urls: set[str] = set()
    for path, text in documents.items():
        relative = path.relative_to(ROOT)
        check(not re.search(r"https?://iam360\.ai(?:[/\s)]|$)", text), f"{relative}: use www.iam360.ai for marketing links")
        check(not re.search(r"[A-Z0-9._%+-]+@(?:gmail|hotmail|outlook)\.com", text, re.I), f"{relative}: personal email address found")
        check("BEGIN PRIVATE KEY" not in text and "BEGIN OPENSSH PRIVATE KEY" not in text, f"{relative}: private-key material found")
        for language, content in re.findall(r"```(json|toml)\n(.*?)\n```", text, re.DOTALL):
            try:
                json.loads(content) if language == "json" else tomllib.loads(content)
            except ValueError as exc:
                errors.append(f"{relative}: invalid {language} code block: {exc}")
        links = re.findall(r"\[[^\]\n]*\]\(([^\s)]+)\)", text)
        links += re.findall(r'<img\s[^>]*src="([^"]+)"', text)
        for target in links:
            parsed = urllib.parse.urlsplit(target)
            if parsed.scheme in {"http", "https"}:
                urls.add(urllib.parse.urlunsplit((parsed.scheme, parsed.netloc, parsed.path, parsed.query, "")))
                continue
            if parsed.scheme == "mailto":
                continue
            destination = (path.parent / urllib.parse.unquote(parsed.path)).resolve() if parsed.path else path
            check(destination.is_relative_to(ROOT), f"{relative}: link escapes repository: {target}")
            if not destination.exists():
                errors.append(f"{relative}: broken local link: {target}")
            elif parsed.fragment and destination.suffix == ".md":
                check(urllib.parse.unquote(parsed.fragment) in headings(destination.read_text()), f"{relative}: missing anchor: {target}")

    tools_text = (ROOT / "docs/tools.md").read_text()
    rows = re.findall(r"^\| \[([a-z_]+)\]\(https://app\.iam360\.ai/docs/mcp/tools/\1\) \| ([^|]+) \|", tools_text, re.MULTILINE)
    check(len(rows) == 27 and len({name for name, _ in rows}) == 27, "capability map must contain 27 unique linked tools")
    check(sum(effect.strip() == "Read" for _, effect in rows) == 12, "capability map must contain 12 read tools")

    public_files = [p for p in ROOT.rglob("*") if p.is_file() and ".git" not in p.parts and "__pycache__" not in p.parts]
    for path in public_files:
        check(path.suffix not in {".pem", ".key", ".p12", ".pfx", ".token"} and not path.name.startswith(".env"), f"credential-like file present: {path.relative_to(ROOT)}")

    if args.check_links:
        print(f"Checking {len(urls)} unique linked URLs without credentials...")
        with ThreadPoolExecutor(max_workers=8) as pool:
            results = list(pool.map(check_remote, sorted(urls)))
        counts: dict[str, int] = {}
        for status, url in results:
            counts[status] = counts.get(status, 0) + 1
            if status != "200":
                print(f"{status}: {url}")
            if status.startswith("FAIL"):
                errors.append(f"broken external link ({status}): {url}")
        print("Public-link results:", json.dumps(counts, sort_keys=True))

    if errors:
        print("Validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"Validation passed: {len(expected) + 1} JSON/TOML connection configs, Gemini extension, Cursor plugin/logo, {len(documents)} Markdown files and 27 tools.")
    print("This check does not authenticate, test private tool calls or prove marketplace approval.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
