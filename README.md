# iAM360 MCP connector

<img src="assets/iam360.png" width="128" height="128" alt="iAM360 logo" />

Connect an AI assistant to your own iAM360 fitness record. The remote MCP server provides wearable metrics, meals and nutrition targets, workouts, progress, challenges, patterns, life events and journal entries. It also supports recording and updating data when you request it.

This repository distributes the iAM360 connector configuration and brand asset. The hosted iAM360 service runs at [app.iam360.ai](https://app.iam360.ai).

## Connect in Cursor

Add the following configuration to Cursor's MCP settings (`.cursor/mcp.json` for a project, or your user MCP configuration):

```json
{
  "mcpServers": {
    "iam360": {
      "url": "https://app.iam360.ai/api/mcp"
    }
  }
}
```

Choose Connect or the sign-in action for iAM360. Sign in to your own iAM360 account in the browser, review the requested access and choose Allow. Cursor discovers the OAuth configuration from the server. No API key or password belongs in the configuration file.

The repository also contains a single Cursor plugin at `.cursor-plugin/plugin.json`, with its remote server in `mcp.json`. For local plugin installation, place this repository's contents under `~/.cursor/plugins/local/iam360/` and restart Cursor, following the [Cursor plugin documentation](https://cursor.com/docs/plugins). Use either the plugin or the manual MCP configuration to avoid duplicate connections.

## Other MCP clients

Use **Streamable HTTP** with the server URL:

```text
https://app.iam360.ai/api/mcp
```

Choose OAuth if your client asks for an authentication method. See [connection instructions](https://app.iam360.ai/docs/mcp/connect) and [authentication details](https://app.iam360.ai/docs/mcp/authentication).

## Example requests

- "Show my logged workouts for this week."
- "Summarize my sleep duration and recovery metrics from the last seven days."
- "What are my nutrition targets and today's logged meals?"

For changes, specify the record and values you want saved. Review changes before confirming actions that replace or delete existing records. The [tool reference](https://app.iam360.ai/docs/mcp) describes each tool's inputs and behavior.

## Account, access and data

An iAM360 account is required. Wearable data requires a supported wearable connected to that account. The fitness authorization includes read and write access, including deletion tools for supported records. The assistant receives the requested account data; review its own privacy controls as well as [iAM360's privacy policy](https://app.iam360.ai/privacy#connected-assistants).

To stop future tool access, open [Settings → AI agents](https://app.iam360.ai/dashboard/settings/agents) in iAM360 and turn the assistant off. This takes effect within a minute and does not delete existing records or copies already received by the assistant.

The connector configuration is free and open source. Some hosted iAM360 AI features, including nutrition estimates and saving workout routines, require an [iAM360 plan](https://app.iam360.ai/plans). Logging meals with nutrition values you provide and other non-AI features do not require that AI plan.

## Help

- [Documentation and tool reference](https://app.iam360.ai/docs/mcp)
- [Privacy policy](https://app.iam360.ai/privacy)
- [Terms of service](https://app.iam360.ai/terms)
- Support: [briandouglasfitonline@gmail.com](mailto:briandouglasfitonline@gmail.com)

Do not post passwords, access tokens or personal fitness records in public issues. Share account-specific support details privately.

## License

The connector files are available under the [MIT license](LICENSE). This license covers this repository; the hosted service is governed by its terms of service. iAM360 branding remains a trademark of its owner.
