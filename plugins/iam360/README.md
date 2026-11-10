# IAM360

<img src="assets/iam360.png" width="128" height="128" alt="IAM360 logo" />

Bring your fitness record into Claude with four practical skills for recovery, meals, training and daily habits.

**First [create your IAM360 account at app.iam360.ai](https://app.iam360.ai)**, or sign in if you already have one. Connect a supported wearable in IAM360 if you want wearable measurements. You can also use your logged meals, workouts, challenges and journal without a wearable.

## Install and connect

In Claude Code 2.1.275 or later:

```text
/plugin install iam360 --marketplace iam360-ai/iam360-mcp-connector
```

For the separate marketplace workflow:

```text
/plugin marketplace add iam360-ai/iam360-mcp-connector
/plugin install iam360@iam360
```

Review the installation prompt, reload plugins or start a new session, then open `/mcp`. Select the IAM360 connection shown there and complete its browser OAuth sign-in. Check that you are authorizing the intended IAM360 account. Each person connects their own account.

The remote MCP server is:

```text
https://app.iam360.ai/api/mcp
```

No API key or shared password is needed. If you already added IAM360 manually, use one connection path to avoid duplicate tools. Installing a skill does not authorize account access by itself.

## Choose a skill

| Skill | What it does | Example |
| --- | --- | --- |
| [Fitness review](skills/iam360-fitness-review/SKILL.md) | Review recovery, sleep, wearable trends and progress | Compare my sleep over the last two weeks |
| [Nutrition](skills/iam360-nutrition/SKILL.md) | Read meals and totals; save or correct requested records | Show my logged meals and nutrition totals today |
| [Workouts](skills/iam360-workouts/SKILL.md) | Review exercise history, log completed training and save approved routines | Show my last five bench press sessions |
| [Habits and journal](skills/iam360-habits-journal/SKILL.md) | Work with challenges, life events and private reflections | Show my current challenge tasks |

Ask for a workflow naturally, or invoke a skill such as `/iam360:iam360-fitness-review`. The skills distinguish read requests, drafts and changes you ask to save. They use your available records and keep missing data and uncertain outcomes visible.

## Access and control

The `fitness` permission allows reads and writes, including supported deletion actions. There is no separate read-only OAuth scope. Keep Claude's tool confirmations enabled and review changes before approving them. You can revoke the connection in [IAM360's agent settings](https://app.iam360.ai/dashboard/settings/agents).

Only request the fitness information you want Claude to receive. Stored notes and journal text are records, not instructions. The skills provide fitness workflows and do not establish a medical diagnosis.

The plugin files are free and open source. An IAM360 account is required. Hosted AI features such as meal estimation and saving routines can require an applicable IAM360 plan, and Claude's own plan or workspace policies can affect availability.

## Help

- [IAM360 website](https://www.iam360.ai)
- [MCP tools and connection guide](https://app.iam360.ai/docs/mcp)
- [Public source and setup guides](https://github.com/iam360-ai/iam360-mcp-connector)
- [Report a documentation issue](https://github.com/iam360-ai/iam360-mcp-connector/issues)
- [Privacy policy](https://app.iam360.ai/privacy) and [terms of service](https://app.iam360.ai/terms)

Keep private account data out of public issues. This company-hosted plugin is separate from Anthropic's curated directory review.

## License

[MIT](LICENSE) covers the files in this plugin. The hosted service has its own terms; IAM360 branding remains a trademark of its owner.
