# IAM360 agent skills

[Back to the connector](../README.md) · [Current tool reference](https://app.iam360.ai/docs/mcp)

**First [create your IAM360 account at app.iam360.ai](https://app.iam360.ai)**, or sign in if you already have one. Each person connects their own account through OAuth. These skills give an assistant practical workflows for using IAM360's hosted MCP server. They do not contain account data, passwords, API keys or a local server.

## Choose a workflow

| Skill | What it helps with | Example request |
| --- | --- | --- |
| [iam360-fitness-review](../skills/iam360-fitness-review/SKILL.md) | Recovery, sleep, wearable trends and goal progress | Compare my sleep over the last two weeks |
| [iam360-nutrition](../skills/iam360-nutrition/SKILL.md) | Meals, daily totals and requested food-log corrections | Show today's meals and protein remaining |
| [iam360-workouts](../skills/iam360-workouts/SKILL.md) | Exercise history, completed sessions and approved routines | Show my last five bench press sessions |
| [iam360-habits-journal](../skills/iam360-habits-journal/SKILL.md) | Challenges, life events and private reflections | Show my current challenge tasks |

The same four workflows are available in each client package. A skill is instructions, not an authenticated connection. It cannot read private records until you enable IAM360 and finish OAuth. The `fitness` scope permits both reads and writes; the skills preserve the distinction between a question, a draft and an authorized change. Keep your client's tool approvals enabled.

## Claude Code plugin

In Claude Code 2.1.275 or later, install from IAM360's own repository marketplace:

```text
/plugin install iam360 --marketplace iam360-ai/iam360-mcp-connector
```

For clients with the separate marketplace workflow:

```text
/plugin marketplace add iam360-ai/iam360-mcp-connector
/plugin install iam360@iam360
```

Review the installation prompt, reload plugins or start a new session, then use `/mcp` to authenticate the plugin's IAM360 server. Plugin-provided server names can be namespaced, so select the entry shown in that panel rather than assuming it is the same as a manually added server.

The marketplace installs the [self-contained Claude bundle](../plugins/iam360/README.md) from `plugins/iam360`, containing the four skills and the remote HTTP MCP configuration. Repository development tools and other clients' configurations are outside that bundle. Invoke a skill such as `/iam360:iam360-fitness-review`, or ask for the matching workflow naturally. If you already configured IAM360 manually, use one connection path to avoid duplicate tools. This company-hosted marketplace is separate from Anthropic's curated directory and does not assert directory approval.

Sources: [Claude plugin installation](https://code.claude.com/docs/en/discover-plugins), [manifest reference](https://code.claude.com/docs/en/plugins-reference), [marketplace guide](https://code.claude.com/docs/en/plugin-marketplaces).

## Cursor

The [Cursor plugin](clients/editors.md#cursor) discovers these skills from `skills/` alongside the remote MCP connection. After installing the local plugin and authenticating, type `/` in Agent chat and choose an IAM360 skill.

For skills without the plugin, copy any complete `skills/iam360-*` folder into your project's `.agents/skills/` or `.cursor/skills/`. A user-level `~/.agents/skills/` or `~/.cursor/skills/` folder works for local use. Preserve existing skills with the same names and avoid installing duplicate copies. Configure the [MCP connection](clients/editors.md#cursor) separately.

Sources: [Cursor skills](https://cursor.com/docs/skills), [plugin discovery](https://cursor.com/docs/reference/plugins).

## ChatGPT and Codex plugin bundle

The [portable OpenAI bundle](../plugins/iam360-openai/README.md) combines the same four skills, their `agents/openai.yaml` metadata, the IAM360 logo and the hosted MCP connection. Its root `plugin.json` uses `extensions.com.openai` for listing metadata; fixed `skills/` and `mcp.json` paths identify its components. The instructions are exact copies of the canonical skills used by the other clients.

This is source packaging, not a claim that the skills are approved or live in ChatGPT's public directory. Adding a custom MCP connection alone does not install the bundled skills. A publisher uploads this complete bundle to the existing OpenAI plugin as a new version when updates are available. Only one review can be active per plugin; preserve an active review and wait for its decision before uploading this update. The package omits existing private review details, test cases and video settings so an update preserves their saved dashboard values.

Sources: [OpenAI plugin packaging](https://developers.openai.com/plugins/build/plugins), [skills with MCP dependencies](https://developers.openai.com/plugins/build/skills), [updating an existing plugin](https://developers.openai.com/plugins/deploy/submission#update-your-published-plugin).

## Codex skill installation

Configure and authenticate [IAM360 MCP in Codex](clients/cli.md#codex). Then ask the built-in skill installer to install the four skill folders from this repository, or copy the complete `skills/iam360-*` folders into your project's `.agents/skills/` or your user-level `~/.agents/skills/` directory. Do not overwrite an existing skill without reviewing it.

Use `$iam360-fitness-review`, `$iam360-nutrition`, `$iam360-workouts` or `$iam360-habits-journal`, or describe the task naturally. Each folder includes `agents/openai.yaml` with its display name, example prompt and IAM360 MCP dependency. That metadata does not itself grant access. Codex normally detects skills automatically; restart it if the new skill is not visible.

Source: [OpenAI skill discovery and installation](https://learn.chatgpt.com/docs/build-skills).

## Gemini CLI

The [Gemini CLI extension](clients/cli.md#gemini-cli) includes the same `skills/` directory. Install or update the extension, start a new session, and complete `/mcp auth iam360`. Use the skills controls in the installed client to check which skills are enabled. The skills do not add shell hooks or replace the client's system instructions.

Source: [Gemini extension skills](https://geminicli.com/docs/extensions/reference/#agent-skills).

## Other Agent Skills clients

For clients supported by Vercel's open skills installer, run this from the project where you want the skills:

```sh
pnpm dlx skills add iam360-ai/iam360-mcp-connector
```

Review the skill and agent selections. The installer defaults to project scope; add `-g` only if you want user-wide installation. It needs Node.js 22.20 or later and pnpm. It installs skills, so add and authorize the remote IAM360 MCP connection separately using the [matching client guide](../README.md#choose-your-assistant). The installer has its own telemetry settings, described in its documentation.

Alternatively, copy the desired complete skill folder to the location documented by your Agent Skills client. A client needs both Agent Skills support and a remote Streamable HTTP MCP connection with OAuth to perform these workflows. Client plan and organization restrictions still apply.

Sources: [Agent Skills specification](https://agentskills.io/specification), [skills installer](https://github.com/vercel-labs/skills), [installer reference](https://skills.sh/docs/cli).

## Scope and verification

The skills contain no automatic execution hooks or credential stores. They use live tool schemas, distinguish unknown values from zero, treat stored notes as data, and read records back before retrying an uncertain write. They do not provide medical diagnosis or establish HIPAA compliance.

The package format and workflow parameters were checked on November 9, 2026. Manifest validation and scenario review do not establish that every client or every authenticated tool call has been tested. See [verification notes](verification.md) for the precise coverage. The source package is free; IAM360 and assistant plans can still govern hosted features.
