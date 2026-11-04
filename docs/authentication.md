# Authentication, permissions and account control

[Back to the connector](../README.md) · [Client setup guides](../README.md#choose-your-assistant) · [Full OAuth reference](https://app.iam360.ai/docs/mcp/authentication)

## Start with your account

[Create an iAM360 account at app.iam360.ai](https://app.iam360.ai), or sign in to an existing one. Check that it contains the data you want your assistant to use. Wearable readings require a WHOOP or Oura connection in iAM360; the assistant does not receive your wearable sign-in credentials.

Your assistant account and your iAM360 account are separate. At consent, check which iAM360 account is signed in and switch accounts if needed. Each person should authorize their own account.

## Normal sign-in flow

1. The client connects to `https://app.iam360.ai/api/mcp`.
2. An unauthenticated request receives `401` with an OAuth discovery challenge. This is expected.
3. The client reads the protected-resource and authorization-server metadata, identifies itself and opens the browser.
4. You sign in to iAM360, review the client name and requested permissions, then allow or deny access.
5. The client stores its OAuth credentials and sends an access token on subsequent MCP calls. A refresh token lets it renew access without a new sign-in while the authorization remains valid.

The authorization issuer is **`https://clerk.iam360.ai`**. Clerk provides iAM360's sign-in infrastructure. The connector should still be named **iAM360**; do not rename the MCP endpoint to the issuer domain.

No static API key or shared client secret is supplied by this repository. Modern clients can discover and register using the metadata. Leave optional manual client credentials empty unless a specific integration has separately provisioned them.

## What access means

| Scope | Meaning |
| --- | --- |
| `fitness` | Read and change the authorized person's fitness records. Required for MCP tools. |
| `offline_access` | Request refresh support so the client can renew access without repeatedly signing in. |

The `fitness` scope includes **both read and write access**, including supported record deletion. There is no separate server-side read-only scope at present. If you want a read-only workflow, disable write tools in the client where supported and keep per-action approvals enabled. Client restrictions do not reduce the OAuth token's server-side authority.

Tools use the authenticated account; a caller cannot select another account by adding a user ID argument. Tools cannot change account settings or expose WHOOP/Oura login credentials. Calls can disclose fitness records—including private journal text—to the assistant provider, so only ask for the information needed for your task.

Some changes have effects beyond one field: replacing a routine changes the schedule; completing or abandoning a challenge affects related reminders and crew membership; deleting a workout reverses associated task completions. Review the [capability map](tools.md) and linked tool details before approving them.

## Disconnect and manage your data

- **Stop future calls:** open [iAM360 → Settings → AI agents](https://app.iam360.ai/dashboard/settings/agents) and choose **Turn off** for the connection. Calls are blocked within a minute.
- **Remove it from your assistant:** disconnect/remove its MCP entry in that client's settings. Also use the iAM360 switch when you want the server to block access.
- **Export or delete your iAM360 data:** use [Settings → Account → Your data](https://app.iam360.ai/dashboard/settings/account#settings-data), following the [public data-control instructions](https://app.iam360.ai/docs/mcp/connect).
- **Manage copies already shared:** use the assistant provider's privacy/data controls. Disabling iAM360 access does not erase information the provider already received.

Revoking a refresh token prevents new access tokens but does not instantly invalidate every previously issued access token. The iAM360 **Turn off** control is the documented way to block calls promptly. Details: [authentication](https://app.iam360.ai/docs/mcp/authentication) and [privacy policy](https://app.iam360.ai/privacy#connected-assistants).

## Other clients and custom agents

A compatible client needs:

- Remote **Streamable HTTP** MCP at `https://app.iam360.ai/api/mcp`.
- MCP OAuth discovery, authorization-code flow with **PKCE S256**, and browser consent.
- The `fitness` scope; request `offline_access` when refresh support is needed.
- The exact MCP endpoint as the OAuth resource/audience.
- A supported client-identity mechanism: Dynamic Client Registration or a Client ID Metadata Document.
- A credential store and token refresh handling, rather than credentials in source files.

Useful public metadata:

| Document | URL |
| --- | --- |
| Protected resource | [Resource metadata](https://app.iam360.ai/.well-known/oauth-protected-resource/api/mcp) |
| Authorization server | [Issuer metadata](https://clerk.iam360.ai/.well-known/oauth-authorization-server) |
| Server Card (SEP-2127) | [Server Card](https://app.iam360.ai/api/mcp/server-card), listed in the [AI Catalog](https://app.iam360.ai/.well-known/ai-catalog.json) |
| Full integration reference | [Authentication docs](https://app.iam360.ai/docs/mcp/authentication) |

Use your MCP SDK's authorization implementation instead of hand-building authorization requests. This repository does not provide a stdio server, an API-key authentication mode, or an unattended service-account flow. A third-party bridge introduces its own installation, credential-storage and compatibility requirements; the documented clients here use native remote support.

Do not point an agent at the GitHub URL, marketing website or documentation page as its MCP transport. Keep tokens in authorization headers handled by the client, never in URLs, public config or logs.
