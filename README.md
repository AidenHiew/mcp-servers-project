# MCP Servers Project

Hands-on project built while following the **Claude Certified Architect** course. Covers the core concepts of the Model Context Protocol (MCP): tools, resources, prompts, completions, and client/server wiring.

## What's inside

### `cli_project/`

A command-line chat application that connects Claude to a local MCP server. Demonstrates:

- **Tools** — `read_doc_contents`, `edit_document`
- **Resources** — list and fetch documents over a `docs://` URI scheme
- **Prompts** — server-defined prompt templates (e.g. reformat a doc in markdown)
- **Completions** — tab-complete doc IDs inside prompt arguments
- **Multi-client** — `main.py` can connect to additional MCP servers passed as CLI arguments

See [`cli_project/README.md`](cli_project/README.md) for setup and usage.

## Tech stack

- Python 3.9+
- [Anthropic SDK](https://github.com/anthropics/anthropic-sdk-python)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) (`fastmcp`)
- [uv](https://github.com/astral-sh/uv) (package manager)
- [prompt-toolkit](https://github.com/prompt-toolkit/python-prompt-toolkit) (CLI UI)
