# Troubleshooting

[Back to setup](../README.md#connect-in-three-steps) · [Authentication](authentication.md) · [Service errors and limits](https://app.iam360.ai/docs/mcp/errors)

First, [create or sign in to your iAM360 account](https://app.iam360.ai) and check that its data is available in the app. Then confirm the client uses **`https://app.iam360.ai/api/mcp`**, Streamable HTTP and OAuth.

| Symptom | What to check |
| --- | --- |
| Opening the endpoint in a browser shows an error or `401` | The endpoint speaks MCP, not HTML. Unauthenticated requests are expected to receive an OAuth challenge. Add it through the client's MCP flow. |
| No Add custom connector / MCP option | Check the client's current plan, version and workspace policies. A workspace admin may need to allow the server first. |
| Configuration loads no tools | Use the correct schema: VS Code has `servers`; most others here use `mcpServers`; Codex uses TOML. Gemini Streamable HTTP uses `httpUrl`. Reload/start the server, authenticate and enable its tools. |
| Sign-in opens `clerk.iam360.ai` | This is iAM360's expected authorization issuer. The MCP endpoint remains on `app.iam360.ai`, and its display name is iAM360. |
| Browser sign-in succeeds but the client stays disconnected | Return to the client, complete any trust prompt and retry connection. Allow the client to open its callback. Remote/headless CLI environments may need the client's documented browser/callback flow. |
| `401` after previously connecting | The access token may be expired, invalid or issued for a different resource. Reauthenticate through the client; do not copy tokens into config or request URLs. |
| `403` / `insufficient_scope` | Authorize the required `fitness` scope. Where scopes are configurable, use `fitness` and `offline_access` for refresh support. |
| Access turned off | Open [iAM360's AI agent settings](https://app.iam360.ai/dashboard/settings/agents). Re-enable only the connection you intend to use. |
| Wrong or empty account data | Check the iAM360 account shown in the consent window and the date/timezone requested. Empty lists can be correct. Disconnect and authorize the intended account if needed. |
| Missing wearable metrics | Check the provider and sync history in iAM360. Missing readings are not zero. The current service reports a WHOOP/Oura conflict if both are connected. |
| AI plan required | Some tools need hosted AI access. Use supplied calories/protein for meal logging, or review [your plan in the app](https://app.iam360.ai/plans). This is separate from the assistant provider's subscription. |
| Rate-limit message | Slow down and request less at once. The documented general limit is about 120 tool calls per person per minute; workout-plan saves have a separate hourly limit. |
| Read times out | Retry a smaller range or section. Repeated failures should be reported with redacted context. |
| Write times out | Do not immediately repeat it. Read the saved data first because the change may already have completed. |
| `duplicate` or `alreadyLogged` result | The server recognized a repeated record. Review the returned existing record; do not force another entry unless that is the user's actual intent. |
| Tool name/schema error | Refresh the tool list, then use the live schema. Do not guess parameters or substitute internal application tool names. |
| HTTP `200`, but nothing was saved | Inspect the MCP result for `isError: true`, `ok: false` or an error message. Transport success is not application success. |
| The same tools appear twice | Remove either the manual MCP entry or the plugin entry; keep one connection path. |

## A safe first check

Ask your assistant: **“Use iAM360 to read today's nutrition. Do not change anything.”** Confirm a tool invocation and compare it with the app. This verifies an authenticated read; it does not test every tool or prove that writes are enabled in that client.

## Public metadata checks

These requests contain no credentials and read only public metadata:

```sh
curl --fail --silent --show-error   https://app.iam360.ai/.well-known/oauth-protected-resource/api/mcp

curl --fail --silent --show-error   https://clerk.iam360.ai/.well-known/oauth-authorization-server
```

The resource document should identify the MCP endpoint and iAM360 authorization issuer. The authorization document describes registration, PKCE and token endpoints. Reaching these URLs alone does not test a signed-in tool call.

## What to include in a report

For a general connection/configuration problem, [open a GitHub issue](https://github.com/iam360-ai/iam360-mcp-connector/issues) with:

- Client name/version and operating system.
- The failing step, approximate time and sanitized error text.
- Whether the problem occurs before or after consent.
- The relevant server entry with all credentials removed.

Never attach passwords, OAuth codes/tokens, full callback URLs, session files, journal entries or fitness records. For private account-data or security issues, follow [private reporting](../SECURITY.md). Documentation and client-interface problems do not require posting personal health information.
