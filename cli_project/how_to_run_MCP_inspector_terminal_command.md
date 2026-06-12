# How to Run the MCP Inspector

## Steps

**1. Open the VS Code terminal**
Press `Ctrl + `` ` `` to open a new terminal panel.

**2. Navigate to your project folder**
```bash
cd your-mcp-project
```

**3. Run the MCP Inspector — directly in the terminal**
```bash
uv run mcp dev mcp_server.py
```

**4. Inspector opens in your browser**
The terminal will show:
```
MCP Inspector running at http://localhost:5173
```
Your browser opens automatically to the Inspector UI.

---

## Common mistake to avoid

| Wrong | Correct |
|---|---|
| `uv run main.py` → then type `mcp dev mcp_server.py` at the `>` prompt | `uv run mcp dev mcp_server.py` directly in the terminal |

Typing the command inside `main.py` sends it to Claude as a **chat message**, not a terminal command.