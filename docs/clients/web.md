# Web and desktop assistants

[Back to the connector](../../README.md) · [OAuth and access](../authentication.md) · [Troubleshooting](../troubleshooting.md)

**Before you connect:** [create an iAM360 account at app.iam360.ai](https://app.iam360.ai), or sign in if you already have one. Your assistant will ask you to authorize that account.

Use this **MCP endpoint** in every connector form:

```text
https://app.iam360.ai/api/mcp
```

Use your own iAM360 account for sign-in. The assistant's login and your iAM360 login are separate accounts; they do not need to use the same email. Do not enter your iAM360 password into a connector configuration field.

## Claude web, Desktop and Cowork

1. Open **Customize → Connectors** in Claude, then **+ Add → Add custom connector**.
2. Name it **iAM360**, enter the endpoint above and continue.
3. Choose **Connect**, finish iAM360's OAuth sign-in and review the consent screen.
4. Enable the connector for the conversation and try a read request.

Use this remote-connector flow in Claude Desktop too. A local `claude_desktop_config.json` stdio entry is a different mechanism; this server needs no local process or desktop extension.

Claude currently documents custom remote connectors on Free, Pro, Max, Ultra, Team and Enterprise; Free is limited to one custom connector. Team/Enterprise administrators must make the connector available first, then each member connects their own account. Remote requests originate from Anthropic's infrastructure, including when used in Desktop or Cowork.

Source: [Claude's custom remote connector guide](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp).

## ChatGPT

1. On the web, open [ChatGPT Plugins](https://chatgpt.com/plugins).
2. Choose **+ → Add custom MCP server**.
3. Use the name **iAM360**, the MCP endpoint above and **OAuth**.
4. Review the server risk notice and create the plugin. Complete sign-in, review its tools and install it.
5. Start a new conversation and mention **@iAM360** when using it.

The current Plugins flow does **not** require a Developer Mode toggle. Creating custom connections is a web flow; do not look for the creation form in the mobile app.

Full read/write custom MCP support is documented for Business, Enterprise and Edu, subject to workspace permissions. Pro custom connections have read/fetch limits; do not assume all iAM360 write tools will be available. Creation and publication permissions differ by workspace role. If the option is absent, check your plan and administrator settings.

Sources: [OpenAI connection guide](https://developers.openai.com/plugins/deploy/connect-chatgpt), [current availability and permissions](https://help.openai.com/en/articles/12584461-connecting-custom-mcp-servers-in-chatgpt).

## Grok

1. Open [Grok Connectors](https://grok.com/connectors).
2. Choose **New Connector → Custom**.
3. Enter the MCP endpoint above and complete the OAuth flow.
4. Return to Grok and ask it to read a specific iAM360 record.

Grok documents connectors for all users. For Business/Enterprise, an administrator first adds the custom MCP server in the cloud console; members then connect their own accounts. Use the MCP endpoint in this form, not the GitHub repository or docs URL.

Sources: [Grok connectors](https://docs.x.ai/grok/connectors), [business connector management](https://docs.x.ai/grok/connector-management).

## Muse and other web assistants

For a client that exposes a custom remote MCP option, use the same endpoint and OAuth flow. The [iAM360 connection guide](https://app.iam360.ai/docs/mcp/connect) includes Muse. The client's account access and custom-connector availability still apply; this repository does not imply a public Muse listing or a completed Muse client test.

If the client accepts only an API key, or only local stdio servers, this endpoint is not directly compatible with that mode. See [custom-agent requirements](../authentication.md#other-clients-and-custom-agents) before trying a bridge.

## Confirm the connection

Ask: **“Use iAM360 to list today's meals without changing anything.”** Look for a real tool invocation such as `get_nutrition`, then compare the result with your account in iAM360. A successful connection can return an empty list when no meals are logged.

If a client has cached an older tool list, refresh its tools or reconnect. Current tools and schemas come from the live server, not this repository's version number.
