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
           ┌───────────────┐
           │  HTTP Client  │  (e.g. curl, frontend)
           └──────┬────────┘
                  │  POST /mcp
           ┌──────▼───────┐
           │   main.py    │  (FastAPI app)
           └──────┬───────┘
                  │
           ┌──────▼───────┐
           │  router.py   │  → Parses task key
           └──────┬───────┘
                  │
           ┌──────▼────────────────────────┐
           │ app/tasks/{task}.py           │  → Executes logic (e.g., datetime, echo, LLM)
           └────────────┬──────────────────┘
                        │
                 ┌──────▼───────┐
                 │ Response JSON│
                 └──────────────┘


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

## 🛠 How to Run the Email Agent System

# 🔧 1. Install dependencies
pip install -r requirements.txt

# 📡 2. Start the MCP server (backend task router)
uvicorn app.main:app --reload

# 🧠 3. Optional: Start Ollama if not running already
ollama run llama3

# 🖥️ 4. Launch the Streamlit UI
streamlit run streamlit_app.py
---

## 💡 What This System Does

    Upload a .csv of names and emails (columns: name,email)

    Set a subject and shared body for the outreach message

    Attach any files (pitch decks, PDFs, etc.)

    Ollama personalizes each email with greeting and sign-off

    MCP server dispatches email sending via Gmail SMTP
    ---
## 📁 File Requirements

Make sure .env is configured with:
EMAIL_USER=your@gmail.com
EMAIL_PASS=your_app_password   # from Gmail App Passwords

---

