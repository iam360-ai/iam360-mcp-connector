# Editors and coding agents

[Back to the connector](../../README.md) · [Configuration files](../../configs/README.md) · [OAuth and permissions](../authentication.md)

**Before you connect:** [create an iAM360 account at app.iam360.ai](https://app.iam360.ai), or sign in if you already have one. Your assistant will ask you to authorize that account.

Merge the matching configuration into your existing file; do not overwrite other MCP servers. An editor can ask you to trust the server configuration, authenticate with iAM360 and approve individual tool calls. These are separate steps.

## Cursor

Merge [cursor.json](../../configs/cursor.json) into `~/.cursor/mcp.json` for your user, or `.cursor/mcp.json` for one project:

```json
{
  "mcpServers": {
    "iam360": {
      "url": "https://app.iam360.ai/api/mcp"
    }
  }
}
```

Open Cursor's **Customize / MCP** settings, enable iAM360 and complete the offered browser sign-in. Return to the editor and check its tool list.

Alternatively, use this repository as a local Cursor plugin. Clone it, place its contents under `~/.cursor/plugins/local/iam360/` and restart Cursor. The included `.cursor-plugin/plugin.json` discovers the root `mcp.json` and committed logo. Choose either the plugin or the manual configuration to avoid duplicate tools.

The plugin adds no local execution hooks. Its name may appear with a `plugin-` prefix in tool approval prompts. Installing it does not mean it has been approved for the public Cursor Marketplace.

Sources: [Cursor MCP guide](https://cursor.com/docs/mcp), [plugin installation](https://cursor.com/docs/plugins), [plugin manifest reference](https://cursor.com/docs/reference/plugins).

## VS Code with GitHub Copilot

Use the Command Palette:

1. Run **MCP: Add Server**.
2. Choose **HTTP** (some versions label it **HTTP or Server-Sent Events**).
3. Enter `https://app.iam360.ai/api/mcp`, name it `iam360` and choose your user profile or workspace.
4. Start/trust the server and finish its OAuth prompt.
5. In Copilot's agent/tool controls, enable the tools you want to use.

For a workspace file, merge [vscode.json](../../configs/vscode.json) into `.vscode/mcp.json`:

```json
{
  "servers": {
    "iam360": {
      "type": "http",
      "url": "https://app.iam360.ai/api/mcp"
    }
  }
}
```

Notice `servers`, not `mcpServers`. You do not need a manually registered client ID for the normal OAuth discovery flow. Organization policies can block MCP or require approval. For the standalone Copilot CLI, use its [separate guide and configuration](cli.md#github-copilot-cli).

Sources: [VS Code MCP setup](https://code.visualstudio.com/docs/agent-customization/mcp-servers), [configuration reference](https://code.visualstudio.com/docs/agents/reference/mcp-configuration).

## Devin Local, Devin CLI and Windsurf documentation

Windsurf's [official MCP documentation URL](https://docs.windsurf.com/windsurf/cascade/mcp) currently redirects to Devin Local documentation. The following is the current **Devin** configuration; it is not a claim that every older Windsurf build accepts it.

In current Devin clients:

```sh
devin mcp add -s user iam360 https://app.iam360.ai/api/mcp
devin mcp login iam360 --scopes fitness,offline_access
```

For the current file-based format, merge [devin.json](../../configs/devin.json) into `~/.config/devin/mcp_config.json`. Its entry uses `url` and `transport: http`. In Desktop, use **Customize → MCPs**, then authenticate when prompted.

For an older Windsurf installation, follow the help bundled with that version or update it. Do not mix legacy `serverUrl` examples with the current Devin schema or copy a different client's JSON unchanged.

Sources: [Devin Local customizations](https://docs.devin.ai/desktop/devin-local/customizations), [Devin MCP configuration](https://docs.devin.ai/cli/extensibility/mcp/configuration).
