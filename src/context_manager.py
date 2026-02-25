import json
import os
from datetime import datetime
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
model = SentenceTransformer('all-MiniLM-L6-v2')
def load_memory(project_name: str):
    path = os.path.join("projects", project_name, "memory.json")
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return {"summary": "", "key_decisions": [], "important_factors": [], "history": [], "logs": [], "last_updated": None, "vector_index": None}
def save_memory(project_name: str, memory: dict):
    os.makedirs(os.path.join("projects", project_name), exist_ok=True)
    path = os.path.join("projects", project_name, "memory.json")
    memory["last_updated"] = datetime.now().isoformat()
    with open(path, "w") as f:
        json.dump(memory, f, indent=2)
def build_context_prompt(memory: dict) -> str:
    return f"\n\n=== PROJECT SUMMARY ===\n{memory.get('summary', 'No summary')}\n\n=== KEY DECISIONS ===\n" + "\n".join(memory.get("key_decisions", [])) + "\n=== END CONTEXT ==="
