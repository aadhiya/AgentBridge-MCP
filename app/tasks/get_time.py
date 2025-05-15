from datetime import datetime

def run(payload: dict):
    return {"response": datetime.now().isoformat()}
