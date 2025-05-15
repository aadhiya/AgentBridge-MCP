import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv
import base64

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASS")

def run(payload: dict):
    msg = EmailMessage()
    msg["Subject"] = payload.get("subject", "No Subject")
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = payload.get("to")
    msg.set_content(payload.get("body", ""))

    # Handle attachments
    attachments = payload.get("attachments", [])
    for file in attachments:
        try:
            name = file["filename"]
            content = base64.b64decode(file["data"])
            mime_type = file.get("mime_type", "application/octet-stream")
            maintype, subtype = mime_type.split("/", 1)
            msg.add_attachment(content, maintype=maintype, subtype=subtype, filename=name)
        except Exception as e:
            return {"status": "failed", "error": f"Attachment failed: {str(e)}"}

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        return {"status": "sent"}
    except Exception as e:
        return {"status": "failed", "error": str(e)}
