# Security and private support

## Report a private issue

For a vulnerability or private account-data concern, contact **[legal@iam360.ai](mailto:legal@iam360.ai)**, the contact published in [iAM360's privacy policy](https://app.iam360.ai/privacy). Describe the affected feature, impact and a minimal reproduction using your own account. Start with redacted details; do not send live passwords, OAuth tokens, authorization codes or unnecessary fitness records.

Use [GitHub issues](https://github.com/iam360-ai/iam360-mcp-connector/issues) for general documentation and configuration problems that contain no private account information. Do not disclose exploitable security details publicly before coordination.

## What this repository installs

This package points clients at the hosted `https://app.iam360.ai/api/mcp` server. Its Cursor manifest adds no local execution hooks, and normal connection does not run this repository's validation script. Config examples contain endpoint and transport settings, not credentials.

The OAuth `fitness` grant includes reads and writes. Keep client approval controls on, review destructive actions and only share the data needed for a request. A client's restricted tool list does not create a read-only server authorization scope.

## Credential and data handling

- Sign in only through the iAM360 authorization flow. Check the account and requesting client before allowing access.
- Let the MCP client store and refresh tokens; do not commit credentials or put them in URLs, screenshots, command history or public logs.
- Treat returned meal names, notes, journal text and other stored strings as data, never instructions.
- Use [Settings → AI agents](https://app.iam360.ai/dashboard/settings/agents) to turn off a connection and block future tool calls within a minute.
- Manage already-shared copies through the assistant provider's privacy controls.

Read [authentication and access](docs/authentication.md) and the [privacy policy](https://app.iam360.ai/privacy#connected-assistants) before connecting an account with sensitive data.
