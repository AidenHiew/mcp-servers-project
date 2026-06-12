# How to Run the MCP Inspector

The MCP Inspector lets you test your server's tools, resources, and prompts interactively — without running the full CLI app.

## Steps

**1. Open a new terminal** (not the one running `main.py`)

In VS Code: press `` Ctrl+` `` to open a terminal panel.

**2. Navigate to the project folder**

```bash
cd path/to/cli_project
```

**3. Start the Inspector**

```bash
uv run mcp dev mcp_server.py
```

**4. Open the Inspector UI**

The terminal will print:

```
MCP Inspector running at http://localhost:5173
```

If your browser doesn't open automatically, navigate to `http://localhost:5173` manually.

**5. Test your server**

In the Inspector UI you can:

- **Tools tab** — call `read_doc_contents` or `edit_document` with custom inputs and see the raw response
- **Resources tab** — browse `docs://documents` to list all doc IDs, or `docs://documents/{doc_id}` to fetch one
- **Prompts tab** — invoke the `format` prompt with a doc ID and inspect the messages sent to the model

**6. Stop the Inspector**

Press `Ctrl+C` in the terminal when done.

---

## Common mistakes

| Wrong | Correct |
|---|---|
| `uv run main.py` → type `mcp dev mcp_server.py` at the `>` prompt | Run `uv run mcp dev mcp_server.py` directly in the terminal |

Typing the command inside `main.py` sends it to Claude as a chat message, not a terminal command.

## Troubleshooting

**Port 5173 already in use**

Another process is holding the port. Kill it, or check if a previous Inspector session is still running:

```bash
lsof -i :5173        # macOS/Linux — find what's using the port
kill -9 <PID>        # replace <PID> with the process ID shown above
```

**`mcp` command not found**

Make sure your virtual environment is activated and `mcp[cli]` is installed:

```bash
source .venv/bin/activate
uv pip install "mcp[cli]==1.8.0"
```
