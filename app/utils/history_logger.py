import os
import json
from datetime import datetime

log_dir = os.path.join("data", "logs")
log_file = os.path.join(log_dir, "chat_history.json")


os.makedirs(log_dir, exist_ok=True)


def log_event(event: dict):
    record = {
        "timestamp": datetime.utcnow().isoformat(timespec="seconds") + "Z",
        **event
    }

    with open(log_file, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")
