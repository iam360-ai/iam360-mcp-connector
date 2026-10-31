# iAM360 MCP connector

<img src="assets/iam360.png" width="128" height="128" alt="iAM360 logo" />

**Your fitness record, available in the assistant you choose.**

iAM360 connects your assistant to your wearable measurements, nutrition, workouts, challenges and journal. Ask it to look up your records, compare periods, or save a change you approve. The hosted server provides **27 tools: 12 read tools and 15 tools that create, update or delete records**.

[Website](https://www.iam360.ai) · [Full tool reference](https://app.iam360.ai/docs/mcp) · [Connection help](docs/troubleshooting.md) · [Privacy](https://app.iam360.ai/privacy)

## Connect in three steps

1. **[Create your iAM360 account](https://app.iam360.ai)**, or sign in there if you already have one. Connect WHOOP or Oura in iAM360 if you want wearable data.
2. Add a **remote MCP server** in your assistant, using this address and OAuth authentication:

   ```text
   https://app.iam360.ai/api/mcp
   ```

3. Complete iAM360's browser sign-in, review the requested access and choose **Allow**. Return to your assistant and enable the connection.

Try a read request first: **“Use iAM360 to show my logged meals and nutrition totals for today.”** Check that the tool actually ran; an assistant's general answer alone does not confirm a connection.

You do not need to clone this repository, run a local server or create an API key for normal use. Clients handle OAuth; do not put your iAM360 password in a config file.

## Choose your assistant

| Client | Setup guide | Copyable configuration |
| --- | --- | --- |
| Claude web, Desktop and Cowork | [Add a custom connector](docs/clients/web.md#claude-web-desktop-and-cowork) | Paste the endpoint in the connector form |
| ChatGPT | [Add a custom MCP plugin](docs/clients/web.md#chatgpt) | Paste the endpoint; choose OAuth |
| Grok | [Add a custom connector](docs/clients/web.md#grok) | Paste the endpoint in Connectors |
| Claude Code | [CLI and browser sign-in](docs/clients/cli.md#claude-code) | [Project JSON](configs/claude-code.json) |
| Codex | [CLI and TOML setup](docs/clients/cli.md#codex) | [TOML](configs/codex.toml) |
| GitHub Copilot CLI | [CLI OAuth setup](docs/clients/cli.md#github-copilot-cli) | [JSON](configs/copilot-cli.json) |
| Gemini CLI | [Install the extension and sign in](docs/clients/cli.md#gemini-cli) | [Extension manifest](gemini-extension.json) or [settings JSON](configs/gemini-cli.json) |
| Cursor | [MCP settings or this plugin](docs/clients/editors.md#cursor) | [JSON](configs/cursor.json) |
| VS Code with GitHub Copilot | [Add Server command or JSON](docs/clients/editors.md#vs-code-with-github-copilot) | [JSON](configs/vscode.json) |
| Devin Local / Devin CLI | [Current vendor setup](docs/clients/editors.md#devin-local-devin-cli-and-windsurf-documentation) | [JSON](configs/devin.json) |
| Windsurf users | [Vendor documentation transition](docs/clients/editors.md#devin-local-devin-cli-and-windsurf-documentation) | Check the installed client's format |
| Goose | [Remote extension setup](docs/clients/cli.md#goose) | Interactive configuration |
| Other MCP clients | [Transport and authorization requirements](docs/authentication.md#other-clients-and-custom-agents) | Streamable HTTP + OAuth |

Client instructions were checked against official documentation on **October 31, 2026**. Availability depends on the client's plan and workspace policies. See the [verification notes](docs/verification.md) for what was tested. These instructions describe custom connections; they do not claim approval in any client's public marketplace.

**Keep existing configuration:** merge the `iam360` entry into your client's file. Do not replace the whole file if it already contains other servers or settings. JSON keys differ by client; use the matching example.

### Gemini CLI extension

First [create your iAM360 account](https://app.iam360.ai), or sign in if you already have one. Then install the extension from your terminal and review Gemini CLI's confirmation prompt:

```sh
gemini extensions install https://github.com/iam360-ai/iam360-mcp-connector
```

Start a new Gemini CLI session, run `/mcp auth iam360`, complete the browser sign-in and choose **Allow**, then return to Gemini CLI. The extension uses the hosted server with OAuth; [the setup guide](docs/clients/cli.md#gemini-cli) covers verification and existing configurations.

## What you can do

| Area | Examples |
| --- | --- |
| Wearables and progress | Read sleep, recovery, HRV, training load, goal progress and recorded patterns |
| Nutrition | Read meals and targets; log, correct or delete a meal |
| Workouts | Search exercises, review history, log sessions, add feedback and save an approved routine |
| Challenges | Review challenges, start one after approval, check off tasks or change its status |
| Life events | Record or correct events such as travel, caffeine or sauna |
| Journal | Read a requested date range; append to or correct a day's entry |

See the [27-tool capability map](docs/tools.md) for each tool, its effect on data and its detailed reference.

Example prompts:

- “Compare my sleep duration over the last seven days with the previous seven.”
- “Show my recent bench press sets and weights.”
- “Log lunch: rice and chicken, 650 calories, 45 g protein, 70 g carbs and 18 g fat.”
- “Show the meal you would delete and ask me to confirm before deleting it.”
- “List my current challenge tasks without changing their completion.”

Missing wearable values are unknown, not zero. Pattern associations are not proof of causation. iAM360's MCP outputs provide fitness records and calculations; the tools do not establish a medical diagnosis.

## Access, cost and control

The `fitness` authorization covers both reads and writes, including supported deletion actions. There is currently no separate server-side read-only scope. Keep your client's tool confirmations enabled and use its tool restrictions where available. [Understand OAuth and permissions](docs/authentication.md).

The connector files are free and open source. An iAM360 account is required. Some hosted AI features—meal nutrition estimates and saving workout routines—require an [iAM360 plan in the app](https://app.iam360.ai/plans). Logging a meal with nutrition values you supply and other non-AI features do not require that AI plan. Your assistant provider may have separate charges or plan requirements.

Turn off a connection in [iAM360 → Settings → AI agents](https://app.iam360.ai/dashboard/settings/agents) to block future tool calls within a minute. This does not erase records already received by the assistant. [Data controls and revocation](docs/authentication.md#disconnect-and-manage-your-data).

## Use the right URL

| Purpose | URL |
| --- | --- |
| **MCP endpoint — paste this into assistants** | `https://app.iam360.ai/api/mcp` |
| Human-readable tool documentation | [app.iam360.ai/docs/mcp](https://app.iam360.ai/docs/mcp) |
| Machine-readable documentation index | [app.iam360.ai/docs/llms.txt](https://app.iam360.ai/docs/llms.txt) |
| Complete machine-readable reference | [app.iam360.ai/docs/llms-full.txt](https://app.iam360.ai/docs/llms-full.txt) |
| Public connector package | [github.com/iam360-ai/iam360-mcp-connector](https://github.com/iam360-ai/iam360-mcp-connector) |
| Product website | [www.iam360.ai](https://www.iam360.ai) |

The documentation, website and GitHub URLs are not MCP endpoints. Seeing `clerk.iam360.ai` during OAuth is expected: it is iAM360's authorization issuer, not the connector's display name.

## Registry and package

The server is [listed in the official MCP Registry](https://registry.modelcontextprotocol.io/v0.1/servers/ai.iam360.app%2Fiam360/versions/1.0.0) as `ai.iam360.app/iam360`, version `1.0.0`. Registry indexing and curated marketplace review are separate processes.

This repository contains the remote connector, logo, client configurations and documentation. The hosted application's source code is not part of this package. The [Cursor manifest](.cursor-plugin/plugin.json) references [mcp.json](mcp.json), and the [Gemini CLI manifest](gemini-extension.json) configures the same hosted endpoint. Neither adds local execution hooks.

## Help and contributing

- [Troubleshooting](docs/troubleshooting.md): sign-in, missing tools, empty data, timeouts and duplicate records.
- [Security guidance and private reporting](SECURITY.md).
- [Contributing and validation](CONTRIBUTING.md).
- General support: [GitHub issues](https://github.com/iam360-ai/iam360-mcp-connector/issues).
- [Privacy policy](https://app.iam360.ai/privacy) and [service terms](https://app.iam360.ai/terms).

For general documentation issues, [open an issue](https://github.com/iam360-ai/iam360-mcp-connector/issues). Keep passwords, tokens, account details and fitness records out of public issues.

Follow iAM360: [Instagram](https://www.instagram.com/iam360_evolved/) · [X](https://x.com/iAM360_Evolved) · [LinkedIn](https://www.linkedin.com/company/iam360-evolved/) · [YouTube](https://www.youtube.com/@iAM360-Official) · [TikTok](https://www.tiktok.com/@iam360_performance_coach)

## License

The files in this repository are available under the [MIT license](LICENSE). The hosted service is governed by its own terms. iAM360 branding remains a trademark of its owner.
