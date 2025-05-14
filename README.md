# AgentBridge-MCP
MCP server for an AI assistant

# AgentBridge-MCP

A modular, extensible **Model Context Protocol (MCP)** server for secure and auditable AI agent task routing.

---

## 🔧 What is This?

This repo is a foundational **local MCP server** built with Python + FastAPI that:

- Accepts structured JSON requests for tasks
- Routes them to secure modular task handlers (e.g. email, CSV parsing, summarization)
- Can be extended for any AI agent or tool

---

## 🚀 What You Get Out of the Box

✅ FastAPI MCP server  
✅ Modular `task/` folder (e.g. echo, get_time)  
✅ Simple `POST /mcp` handler  
✅ Dispatch logic with task map  
✅ Ready for local testing & extension

---

## 💡 Why Use It?

This MCP server acts as the **command center** for AI agents.

It separates "what needs to be done" from "how it’s done" — enabling:
- 📦 Task modularity
- 🔐 A2SPA-compliant secure execution
- ⚡ Agent-Agnostic Logic (GPT, Claude, Ollama, etc.)

---

## 📁 Folder Structure

app/
├── main.py # FastAPI entry point
├── router.py # Dispatch logic
└── tasks/
├── echo.py
├── get_time.py
└── summarize_text.py

tests/
├── test_mcp.py

run.sh # Dev runner
requirements.txt # Dependencies



---
## 📊 Workflow Diagram

┌────────────┐
│ HTTP Client│
│ (e.g. curl,│
│  frontend) │
└─────┬──────┘
      │ POST /mcp
      ▼
┌───────────────┐
│   main.py     │
│ (FastAPI app) │
└─────┬─────────┘
      │
      ▼
┌────────────────────┐
│     router.py      │
│  → Parses task key │
│  → Dispatches to   │
│    correct module  │
└─────┬──────────────┘
      │
      ▼
┌────────────────────────┐
│ app/tasks/{task}.py    │
│ Executes logic (e.g.,  │
│ datetime, echo, LLM)   │
└──────────┬─────────────┘
           ▼
      Response JSON

---

## 📈 Coming Soon

This core server will soon power a Modular Investor Outreach AI Agent, with:

    CSV-based email flows

    Validation + personalization via MCP

    PKI-audited A2SPA security

    GPT/Ollama integration
---

🧠 Inspired By

    Anthropic’s Claude MCP architecture

    A2SPA Protocol (Agent-to-Agent Secure Protocol Architecture)

    ---

## 🛠 Example Request

```bash
curl -X POST http://localhost:8000/mcp \
    -H "Content-Type: application/json" \
    -d '{"task": "echo", "payload": {"msg": "hello"}}'
---

