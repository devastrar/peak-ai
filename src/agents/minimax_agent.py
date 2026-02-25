import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv("config/.env")
def run(query: str, context: str = "", project: str = None):
    client = OpenAI(api_key=os.getenv("MINIMAX_API_KEY"), base_url="https://api.minimax.io/v1")
    response = client.chat.completions.create(model="MiniMax-M2.5", messages=[{"role": "user", "content": query + context}], max_tokens=800)
    result = response.choices[0].message.content
    return result
