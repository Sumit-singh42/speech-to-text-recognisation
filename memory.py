import json
import os
from datetime import datetime

MEMORY_FILE = "memory.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []
    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_memory(memory):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(memory, f, ensure_ascii=False, indent=2)

def add_entry(transcript, emotion):
    memory = load_memory()
    memory.append({
        "timestamp": datetime.now().isoformat(),
        "transcript": transcript,
        "emotion": emotion
    })
    save_memory(memory)

def get_recent_context(limit=3):
    memory = load_memory()
    return memory[-limit:] if len(memory) > 0 else []
