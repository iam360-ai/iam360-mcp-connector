# Client configuration examples

All examples connect to `https://app.iam360.ai/api/mcp` with native OAuth. They contain no credentials. Complete browser sign-in after adding the server.

| File | Merge into | Important difference |
| --- | --- | --- |
| [cursor.json](cursor.json) | `~/.cursor/mcp.json` or project `.cursor/mcp.json` | `mcpServers` with `url` |
| [claude-code.json](claude-code.json) | Project `.mcp.json` | `mcpServers`, `type: http` |
| [vscode.json](vscode.json) | Project `.vscode/mcp.json`, or use **MCP: Add Server** for your user profile | `servers`, not `mcpServers` |
| [codex.toml](codex.toml) | `~/.codex/config.toml`, or a trusted project's `.codex/config.toml` | TOML table; do not duplicate an existing `iam360` table |
| [copilot-cli.json](copilot-cli.json) | `~/.copilot/mcp-config.json` | `mcpServers`, `type: http`, `tools` list |
| [gemini-cli.json](gemini-cli.json) | `~/.gemini/settings.json` | `httpUrl` means Streamable HTTP; `url` means SSE |
| [devin.json](devin.json) | `~/.config/devin/mcp_config.json` in current Devin clients | `transport: http`; not a legacy Windsurf config |

Back up your current file and merge only the `iam360` server entry. Preserve other servers and unrelated settings. Some clients require a restart, reload or explicit trust approval before loading changes.

Do not add authorization headers, passwords, static client secrets or demo credentials to these examples. OAuth credentials belong in the client's credential store.

See the [web](../docs/clients/web.md), [editor](../docs/clients/editors.md) and [CLI](../docs/clients/cli.md) guides for client-specific sign-in and verification steps.
