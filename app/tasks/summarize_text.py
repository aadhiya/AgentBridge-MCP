def run(payload: dict):
    text = payload.get("text", "")
    return {"summary": text[:100] + "..."}  # Truncated summary stub
