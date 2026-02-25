import os
import re
from openai import OpenAI
from dotenv import load_dotenv
from datetime import datetime
from src.context_manager import build_context_prompt
from src.file_manager import write_file
from src.logger import logger
load_dotenv("config/.env")
def run(query: str, context: str = "", project: str = None):
    client = OpenAI(api_key=os.getenv("KIMI_API_KEY"), base_url="https://api.moonshot.ai/v1")
    SYSTEM_PROMPT = """You are KimiK2.5 inside Peak AI Tool System v7.9. Use tools when needed. Stay inside the system."""
    full_query = query + context
    response = client.chat.completions.create(model="kimi-k2.5", messages=[{"role": "system", "content": SYSTEM_PROMPT}, {"role": "user", "content": full_query}], max_tokens=800, temperature=1.0)
    result = (getattr(response.choices[0].message, 'reasoning_content', '') or '') + "\n\n" + (response.choices[0].message.content or "")
    if project and "```" in result:
        try:
            blocks = list(re.finditer(r"```(\w+)?\n(.*?)```", result, re.DOTALL))
            for i, match in enumerate(blocks):
                lang, code = match.group(1) or "txt", match.group(2)
                filename = f"generated_{lang}_{datetime.now().strftime('%H%M%S')}_{i}.{lang if lang != 'txt' else 'py'}"
                write_file(project, filename, code.strip())
                result += f"\n💾 Saved as projects/{project}/{filename}"
        except Exception as e:
            result += f"\n⚠️ File save skipped: {e}"
    logger.info(f"Kimi completed query for {project}")
    return result
