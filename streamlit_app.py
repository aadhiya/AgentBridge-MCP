import streamlit as st
import requests
import pandas as pd
import base64
import mimetypes

st.set_page_config(page_title="Investor Email Agent", layout="centered")
st.title("📨 AI Email Agent with A2SPA Pitch")

# Upload inputs
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
attachments = st.file_uploader("Attach Files", type=["pdf", "docx", "jpg", "png"], accept_multiple_files=True)

# Subject and shared email body
default_subject = st.text_input("Subject Line", "A2SPA: The Protocol Powering the Future of AI Agents")

default_body = st.text_area("Shared Email Body", height=350, value="""
I wanted to personally introduce you to A2SPA – our breakthrough protocol powering AImodularity, the world’s first agentic AI platform built on personalized data, modular toggles, and secure agent-to-agent communication.

We’re not another AI SaaS.
We’re building a future where everyone controls their own AI, with plug-and-play agents that automate their life or business, all secured by our proprietary A2SPA layer.

🔐 A2SPA (Authenticated Agent-to-Secure Protocol Architecture) ensures:
	•	Encrypted agent identity and interaction
	•	Role-based access controls per module
	•	PKI-based agent signing
	•	Total security across autonomous agent communication

🧠 AImodularity.com is launching soon – and it’s already turning heads.

👇 Review our investor deck and secure your early position:
👉 [Insert Link to Deck]

👥 Join our private pre-launch now:
👉 [Insert Pre-Launch Signup Link]

I believe you’ll immediately see the potential. If this aligns with your thesis, let’s talk.
""")

# Send logic
if uploaded_file and st.button("📤 Send to All"):
    df = pd.read_csv(uploaded_file)
    df.rename(columns=lambda x: x.strip().lower(), inplace=True)

    # Encode attachments
    encoded_attachments = []
    for file in attachments:
        content = file.read()
        encoded = base64.b64encode(content).decode("utf-8")
        mime_type, _ = mimetypes.guess_type(file.name)
        encoded_attachments.append({
            "filename": file.name,
            "data": encoded,
            "mime_type": mime_type or "application/octet-stream"
        })

    # Iterate through contacts
    for index, row in df.iterrows():
        name = row["name"]
        email = row["email"]

        # Personalize via Ollama through MCP
        response = requests.post("http://localhost:8000/mcp", json={
            "task": "personalize_email",
            "payload": {
                "name": name,
                "base_body": default_body
            }
        }).json()

        subject = response.get("subject", default_subject)
        body = response.get("body", f"Hi {name},\n\n" + default_body)

        # Send via MCP
        send_response = requests.post("http://localhost:8000/mcp", json={
            "task": "send_email",
            "payload": {
                "name": name,
                "to": email,
                "subject": subject,
                "body": body,
                "attachments": encoded_attachments
            }
        })

        st.success(f"✅ Sent to {name} → {send_response.json().get('status')}")
