# IAM360 for ChatGPT and Codex

**First [create your IAM360 account at app.iam360.ai](https://app.iam360.ai)**, or sign in if you already have one. This portable plugin bundles four Agent Skills and IAM360's remote MCP connection. Authenticate your own account through the client's OAuth flow after installation.

| Skill | Use it to |
| --- | --- |
| [Fitness review](skills/iam360-fitness-review/SKILL.md) | Review sleep, recovery and recorded fitness progress |
| [Nutrition](skills/iam360-nutrition/SKILL.md) | Read meals and totals, or log and correct meals you specify |
| [Workouts](skills/iam360-workouts/SKILL.md) | Review exercise history, record completed training and save approved routines |
| [Habits and journal](skills/iam360-habits-journal/SKILL.md) | Manage requested challenges, life events and private reflections |

Try: “Compare my IAM360 sleep over the last two weeks.” The assistant must run the connected tools to answer from your records. Missing measurements are unknown, not zero.

The plugin uses `https://app.iam360.ai/api/mcp` with OAuth. It contains instructions, display metadata, a logo and the remote connection configuration. It has no local server, execution hooks, passwords or API keys. OAuth allows reads and writes; installing a skill does not authorize every possible change. Keep your client's tool confirmations enabled. IAM360 provides fitness and general wellness records, not medical diagnosis or treatment.

## Packaging and availability

The `plugin.json`, `mcp.json`, `skills/` and `assets/` paths follow OpenAI's documented portable plugin layout. The skill instructions and metadata are exact copies of the repository's canonical skills. Other compatible clients can reuse those skill folders with their own remote MCP setup; plugin manifests and client configuration formats are not interchangeable.

This source bundle is version `1.1.0`. It does not establish approval or availability in OpenAI's public directory. A publisher uploads the complete contents of this directory as a ZIP to the existing IAM360 plugin when its update flow is available. Keep the files at the ZIP root, without an enclosing folder. Do not upload the entire repository or another client's plugin bundle.

For local skill installation and other clients, use the [IAM360 skill guide](https://github.com/iam360-ai/iam360-mcp-connector/blob/main/docs/skills.md). Package and skill instructions are free; client plans, organization policies and IAM360 feature entitlements still apply.

[Product and signup](https://app.iam360.ai) · [Website](https://www.iam360.ai) · [Connection help](https://app.iam360.ai/docs/mcp/connect) · [Tool reference](https://app.iam360.ai/docs/mcp) · [Privacy](https://app.iam360.ai/privacy) · [Terms](https://app.iam360.ai/terms)

Sources: [OpenAI plugin packaging](https://developers.openai.com/plugins/build/plugins), [OpenAI skills](https://developers.openai.com/plugins/build/skills), [submission and updates](https://developers.openai.com/plugins/deploy/submission).
