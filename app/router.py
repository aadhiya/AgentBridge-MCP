

from app.tasks import echo, get_time, summarize_text, send_email, personalize_email

task_map = {
    "echo": echo.run,
    "get_time": get_time.run,
    "summarize_text": summarize_text.run,
    "send_email": send_email.run,
    "personalize_email": personalize_email.run
}



def dispatch_task(task: str, payload: dict):
    if task in task_map:
        return task_map[task](payload)
    return {"error": "Unknown task"}
