# URL Shortener MCP Tool

[![smithery badge](https://smithery.ai/badge/@Talismanic/cleanuri-url-shortener-mcp)](https://smithery.ai/server/@Talismanic/cleanuri-url-shortener-mcp)

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
or for Docker based installation:
### 3. Running
```
uv run main.py
```
or for dockers:
```
docker build -t url-shortener .
```

### 4. Adding in Claude Desktop

#### With the uv
```
{
  "mcpServers": {
    "url-shortener": {
      "command": "/Users/{userName}/.local/bin/uv",
      "args": [
        "--directory",
        "{patht_to_repo}/cleanuri-url-shortener-mcp",
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