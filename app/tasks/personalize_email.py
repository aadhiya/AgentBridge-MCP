import ollama

def run(payload: dict):
    name = payload.get("name", "Investor")
    base_body = payload.get("base_body", "")

    prompt = f"""You are writing a professional outreach email.
Add a greeting and sign-off around this body. Address the person by name: {name}.

---

{base_body}
"""

    try:
        response = ollama.chat(
            model="llama3",
            messages=[{"role": "user", "content": prompt}]
        )
        return {
            "subject": f"{name}, A2SPA is redefining agentic AI — Early access inside",
            "body": response['message']['content']
        }
    except Exception as e:
        return {"error": str(e)}
