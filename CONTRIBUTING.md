# Contributing

This repository distributes the remote iAM360 connector, documentation and client examples. Keep application source, production credentials, test accounts and user records out of it.

## Make a focused change

1. Check the relevant client's current official documentation and cite it beside the instructions.
2. Preserve the endpoint `https://app.iam360.ai/api/mcp`. Use `https://www.iam360.ai` for marketing links, and `https://app.iam360.ai` for account access, product pages and MCP docs.
3. Update the matching example and guide together. Client keys differ (`servers`, `mcpServers`, `httpUrl`, TOML tables); do not normalize them into one incorrect format.
4. Keep OAuth credentials out of examples. Never add a demo password, personal email address, token or shared client secret.
5. If server capabilities change, compare the public [tool reference](https://app.iam360.ai/docs/mcp), [full machine-readable docs](https://app.iam360.ai/docs/llms-full.txt) and an authenticated `tools/list` result. Update the capability map and verification date together.
6. Distinguish source-checked setup from a client you actually tested. Marketplace submission, listing and approval are different states.

## Validate before a pull request

Python 3.11 or newer is needed only for this optional maintainer check, not for connecting to iAM360:

```sh
python3 scripts/validate.py
```

It checks client JSON/TOML shapes, endpoint consistency, the plugin/logo reference, Markdown code samples, local links/anchors, the 27-tool map and obvious credential-file hazards. It does not authenticate or call any private tool.

An optional public-link pass is available:

```sh
python3 scripts/validate.py --check-links
```

This reads public linked pages. Login-only links and social sites are reported as skipped; an automated `403` or `429` is reported separately for manual review rather than called a verified link. Broken links and structural errors fail the check.

For a client behavior change, also perform a real OAuth connection and a read-only call using your own account. Check client approval handling before testing mutations, clean up any test records, and report the actual coverage in your pull request. Never commit the session or account data used for a test.

## Scope of the license

The MIT license covers this repository. It does not publish the hosted application's source or change the hosted service's terms. Preserve iAM360 attribution and logo provenance.
