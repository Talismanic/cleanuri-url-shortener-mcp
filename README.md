# URL Shortener MCP Tool

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

### 2. Installation

```bash
uv add httpx 'mcp[cli]'
```

### 3. Running
```
uv run main.py
```

### 4. Adding in Claude Desktop
```
{
  "mcpServers": {
    "url-shortener": {
      "command": "/Users/mohammedmehedihasan/.local/bin/uv",
      "args": [
        "--directory",
        "/Users/mohammedmehedihasan/personal/codes/mcp-servers/cleanuri-url-shortener-mcp",
        "run",
        "main.py"
      ]
    }
  }
}```