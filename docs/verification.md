# Verification and maintenance notes

This documentation was prepared on **October 31, 2026**. Client interfaces and plan availability change; the official references beside each setup guide are the update sources.

## Verified for this release

- The live endpoint responds to an unauthenticated MCP request with the expected `401` OAuth discovery challenge.
- Public resource metadata identifies `https://app.iam360.ai/api/mcp` and the `https://clerk.iam360.ai` authorization issuer. OAuth metadata advertises PKCE S256, Dynamic Client Registration and Client ID Metadata Documents.
- Against an isolated local server build, official MCP Inspector 2.13.0 listed all **27 tools** with strict validation and successfully ran exercise search. This was not an authenticated production-endpoint test, a full client end-to-end test or a test of every write tool.
- The official MCP Registry record for `ai.iam360.app/iam360@1.0.0` is public and active. [View the immutable record](https://registry.modelcontextprotocol.io/v0.1/servers/ai.iam360.app%2Fiam360/versions/1.0.0).
- The committed brand icon is the app's public 512×512 PNG. Cursor's official template validator accepted the connector package.
- The client examples and commands were checked against current official client documentation. Repository validation covers syntax, shapes, local links and tool catalog consistency.

## Agent skills package, November 9, 2026

- Package version `1.1.0` adds four portable IAM360 skills and a Claude plugin with a company-hosted marketplace manifest. Cursor and Gemini CLI use the same skill folders.
- Workflow names, parameter constraints and write semantics were checked against the current IAM360 MCP implementation. Live tool schemas remain authoritative.
- Claude Code 2.1.321 strict manifest validation and its directory submission profile accepted the plugin and marketplace without warnings. The `plugins/iam360` runtime bundle was then validated separately. These are local validation results, not directory approval.
- Claude directory submissions use the self-contained `plugins/iam360` path. Its nine files contain only four skills, one remote MCP configuration, its manifest, logo, license and README. Repository development utilities and other-client configurations remain outside it. The root Claude manifest is retained for direct-root compatibility.
- The package validator enforces exact copies of canonical skill, logo and license files, consistent manifest/MCP values and the runtime bundle's file allowlist.
- Each skill passed the skill format validator. The package validator checks declared dependencies, relative file paths, supported tool references and instruction-only contents.
- The `plugins/iam360-openai` portable bundle packages those same four skills and their OpenAI display/dependency metadata, with the existing remote MCP and OAuth configuration. Its thirteen-file allowlist and exact copies are checked separately from the nine-file Claude bundle. Local schema and metadata checks do not replace OpenAI's upload scans or an authenticated skill activation test.
- This update did not authenticate user accounts, run private production tools or prove every client's installation flow end to end.

## Limits of that verification

These are documented custom-connection paths. A successful source/configuration review does not establish an end-to-end test of every listed client, account plan or workspace policy. The hosted tools are not all exercised by the repository validator.

This repository makes no claim of approval in Claude, ChatGPT, Cursor, Grok, Muse or Google's public directories. Official MCP Registry indexing is separate from those curated review processes. Gemini CLI setup is separate from Google's Connected Apps program.

The current server catalog is authoritative. The connector package's `1.1.0` version identifies this skills distribution. It does not change the hosted server or the registry's immutable `1.0.0` record.

## Public sources of truth

| Topic | Reference |
| --- | --- |
| Product and account access | [app.iam360.ai](https://app.iam360.ai) |
| Current tool schemas, examples and errors | [Full MCP reference](https://app.iam360.ai/docs/llms-full.txt) |
| Account consent and disconnection | [Connection guide](https://app.iam360.ai/docs/mcp/connect) |
| OAuth contract | [Authentication guide](https://app.iam360.ai/docs/mcp/authentication) |
| Client setup | Official links beside each [web](clients/web.md), [CLI](clients/cli.md) and [editor](clients/editors.md) section |
| Public connector source | [iam360-ai/iam360-mcp-connector](https://github.com/iam360-ai/iam360-mcp-connector) |

For the maintainer validation workflow, see [Contributing](../CONTRIBUTING.md).
