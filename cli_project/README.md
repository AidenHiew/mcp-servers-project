# MCP Chat

MCP Chat is a command-line interface application that enables interactive chat with Claude through the Anthropic API. It demonstrates core MCP (Model Context Protocol) concepts: tools, resources, prompts, and completions — all wired through a local MCP server.

## Architecture

```
main.py
  └── MCPClient          ← connects to mcp_server.py over stdio
  └── Claude             ← wraps the Anthropic API
  └── CliChat            ← routes user input to tools/resources/prompts
  └── CliApp             ← drives the interactive terminal UI

mcp_server.py (FastMCP)
  ├── Tools       read_doc_contents, edit_document
  ├── Resources   docs://documents, docs://documents/{doc_id}
  ├── Prompts     format
  └── Completion  tab-complete doc IDs in prompt arguments
```

When you type `@deposition.md`, `CliChat` reads the `docs://documents/deposition.md` resource and injects its content into the Claude request. When you type `/format`, it fetches the `format` prompt from the server and sends it to Claude, which then calls the `edit_document` tool to apply changes.

## Prerequisites

- Python 3.9+
- Anthropic API key
- A Claude model name (e.g. `claude-sonnet-4-6`)

## Setup

### Step 1: Configure environment variables

Create a `.env` file in the project root:

```
ANTHROPIC_API_KEY=""   # Your Anthropic API secret key
CLAUDE_MODEL=""        # e.g. claude-sonnet-4-6
```

Both variables are required. The app will exit immediately if either is missing.

### Step 2: Install dependencies

#### Option 1: uv (Recommended)

[uv](https://github.com/astral-sh/uv) is a fast Python package manager.

```bash
pip install uv
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -e .
uv run main.py
```

#### Option 2: Standard pip

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install anthropic python-dotenv prompt-toolkit "mcp[cli]==1.8.0"
python main.py
```

## Usage

### Basic chat

Type any message and press Enter.

### Document retrieval

Prefix a document ID with `@` to include its content in your query:

```
> Tell me about @deposition.md
```

This reads the `docs://documents/deposition.md` resource from the MCP server and passes the content to Claude.

### Prompts

Prefix a prompt name with `/` to invoke a server-defined prompt:

```
> /format deposition.md
```

Press **Tab** to auto-complete document IDs in prompt arguments.

## Development

### Adding documents

Add entries to the `docs` dict in `mcp_server.py`:

```python
docs = {
    "my-file.md": "Content of my file.",
    ...
}
```

### Testing with MCP Inspector

Use the MCP Inspector to interactively test tools, resources, and prompts without running the full CLI. See [how_to_run_MCP_inspector_terminal_command.md](how_to_run_MCP_inspector_terminal_command.md).
