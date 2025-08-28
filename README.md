[![MseeP.ai Security Assessment Badge](https://mseep.net/pr/talismanic-cleanuri-url-shortener-mcp-badge.png)](https://mseep.ai/app/talismanic-cleanuri-url-shortener-mcp)

# URL Shortener MCP Tool

[![smithery badge](https://smithery.ai/badge/@Talismanic/cleanuri-url-shortener-mcp)](https://smithery.ai/server/@Talismanic/cleanuri-url-shortener-mcp)

<a href="https://glama.ai/mcp/servers/@Talismanic/cleanuri-url-shortener-mcp">
  <img width="380" height="200" src="https://glama.ai/mcp/servers/@Talismanic/cleanuri-url-shortener-mcp/badge" alt="URL Shortener MCP server" />
</a>

This project provides a simple URL shortening tool using the [CleanURI API](https://cleanuri.com/) and is designed to run as a [FastMCP](https://github.com/multiprompt/fastmcp) server tool.

## ✨ Features

- Shortens any given URL using the CleanURI API.
- Exposes the functionality as a tool via FastMCP.
- Includes proper error handling and response validation.
- Designed to run via `stdio` transport for integration with agent or tool-based systems.

## 🚀 Usage

### 1. Requirements

- Python 3.10+
- `httpx`
- `fastmcp`

## 2. Installation

### Installing via Smithery

To install URL Shortener Tool for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@Talismanic/cleanuri-url-shortener-mcp):

```bash
npx -y @smithery/cli install @Talismanic/cleanuri-url-shortener-mcp --client claude
```

### Manual Installation
```bash
uv add httpx 'mcp[cli]'
```
### Docker Installation:
```
docker build -t url-shortener .
```
### 3. Running
```
uv run main.py
```
For docker based use, we dont need to do anything here.


### 4. Adding in Claude Desktop

#### With the uv
```
{
  "mcpServers": {
    "url-shortener": {
      "command": "/Users/{userName}/.local/bin/uv",
      "args": [
        "--directory",
        "{path_to_repo}/cleanuri-url-shortener-mcp",
        "run",
        "main.py"
      ]
    }
  }
}
```

#### With Docker
```
{
  "mcpServers": {
    "url-shortener": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "--init",
        "-e",
        "DOCKER_CONTAINER=true",
        "url-shortener"
      ]
    }
  }
}
```