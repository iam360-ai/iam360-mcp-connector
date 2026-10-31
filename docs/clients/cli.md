# Command-line assistants

[Back to the connector](../../README.md) · [Configuration files](../../configs/README.md) · [Troubleshooting](../troubleshooting.md)

**Before you connect:** [create an iAM360 account at app.iam360.ai](https://app.iam360.ai), or sign in if you already have one. Your assistant will ask you to authorize that account.

These commands assume the named client is already installed and current. They register a remote endpoint; they do not install an iAM360 server locally. Complete OAuth in a browser before asking the agent to use account data. Keep tool approvals enabled.

## Claude Code

Add a connection for your user account:

```sh
claude mcp add --transport http --scope user iam360 https://app.iam360.ai/api/mcp
claude mcp login iam360
claude mcp get iam360
```

Inside Claude Code, `/mcp` also provides connection status and sign-in. If your installed version does not have `mcp login`, use that interactive panel or update the client.

For a shared project configuration, merge [claude-code.json](../../configs/claude-code.json) into `.mcp.json` and approve it when Claude asks. The JSON contains the endpoint, not your credentials; each person authenticates separately.

`claude mcp logout iam360` clears the client's OAuth connection. Also turn it off in [iAM360's agent settings](https://app.iam360.ai/dashboard/settings/agents) when you want the server to block future calls.

Source: [Claude Code MCP documentation](https://code.claude.com/docs/en/mcp).

## Codex

```sh
codex mcp add iam360 --url https://app.iam360.ai/api/mcp
codex mcp login iam360 --scopes fitness,offline_access
codex mcp list
```

Start Codex and use `/mcp` to check tools. The OAuth login opens your browser. No experimental MCP flag or static bearer token is needed.

Alternatively, merge [codex.toml](../../configs/codex.toml) into `~/.codex/config.toml`:

```toml
[mcp_servers.iam360]
url = "https://app.iam360.ai/api/mcp"
scopes = ["fitness", "offline_access"]
```

A trusted project's `.codex/config.toml` can also hold this configuration. Do not create two TOML tables with the same name. Managed workspace policies may restrict which servers can be added. A local Codex configuration does not publish a ChatGPT plugin.

Sources: [Codex MCP guide](https://learn.chatgpt.com/docs/extend/mcp), [Codex MCP command reference](https://learn.chatgpt.com/docs/developer-commands#codex-mcp).

## Gemini CLI

First [create your iAM360 account](https://app.iam360.ai), or sign in if you already have one. Install this repository as an extension from your terminal:

```sh
gemini extensions install https://github.com/iam360-ai/iam360-mcp-connector
gemini
```

Review the installation confirmation. Start a new Gemini CLI session if one was already running, then authenticate and check the connection:

```text
/mcp auth iam360
/mcp list
```

Complete iAM360's browser sign-in, review the requested access and choose **Allow**, then return to Gemini CLI. The [extension manifest](../../gemini-extension.json) requests `fitness` and `offline_access` and contains only the remote MCP configuration. It does not install a local iAM360 server or add execution hooks.

As an alternative to the extension, merge [gemini-cli.json](../../configs/gemini-cli.json) into `~/.gemini/settings.json`. It provides the same endpoint and scopes. Use one configuration path: an existing `mcpServers.iam360` entry in your settings takes precedence over the extension. Preserve other servers and settings.

The `httpUrl` field selects Streamable HTTP; Gemini's `url` field selects SSE. OAuth discovery supplies the endpoints and client registration. A local browser and working loopback callback are needed; SSH/headless environments can require additional client setup. Keep tool approvals enabled.

To update the extension, run `gemini extensions update iam360-mcp-connector` and start a new session. This setup does not imply approval in Google's Connected Apps catalog. Gemini CLI's gallery separately crawls public repositories tagged `gemini-cli-extension` daily and lists extensions that pass validation.

Sources: [Gemini CLI extension reference](https://geminicli.com/docs/extensions/reference/), [MCP and OAuth documentation](https://geminicli.com/docs/tools/mcp-server/), [extension gallery indexing](https://geminicli.com/docs/extensions/releasing/).

## GitHub Copilot CLI

```sh
copilot mcp add --transport http iam360 https://app.iam360.ai/api/mcp
```

In an interactive Copilot session, use:

```text
/mcp auth iam360
```

The alternative file is `~/.copilot/mcp-config.json`; merge [copilot-cli.json](../../configs/copilot-cli.json). It uses `mcpServers` and a remote entry with `type: http`, `url` and `tools: ["*"]`. The wildcard exposes all server tools to the client; it does not remove the need for authorization or tool approval.

This is a different schema from VS Code's `.vscode/mcp.json`, which uses `servers`. Do not copy the VS Code file into the Copilot CLI configuration.

Sources: [Copilot CLI MCP setup](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-mcp-servers), [OAuth command reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference#oauth-re-authentication).

## Goose

For a persistent connection, run:

```sh
goose configure
```

Choose **Add Extension → Remote Extension (Streamable HTTP)**, name it **iAM360** and enter `https://app.iam360.ai/api/mcp`. Complete the browser OAuth prompt. If configuring requested scopes, use `fitness` and `offline_access`.

For a connection limited to one session:

```sh
goose session --with-streamable-http-extension "https://app.iam360.ai/api/mcp"
```

Goose supports native OAuth discovery and client registration for this transport. You do not need a local `mcp-remote` process for the documented path.

Source: [Goose extensions guide](https://goose-docs.ai/docs/getting-started/using-extensions/).

## Start with a read

After sign-in, ask the agent to use `get_nutrition` for today or `get_workouts` for a specific date. Verify the data against iAM360. Empty records are a valid result. For write actions, specify the intended record and values, review the action and verify the saved result.
