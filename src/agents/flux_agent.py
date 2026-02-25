import os
import fal_client
from dotenv import load_dotenv
load_dotenv("config/.env")
def run(query: str):
    os.environ["FAL_KEY"] = f"{os.getenv('FAL_KEY_ID')}:{os.getenv('FAL_KEY_SECRET')}"
    result = fal_client.run("fal-ai/flux/schnell", arguments={"prompt": query, "image_size": "square", "num_inference_steps": 4})
    return f"✅ Image generated: {result['images'][0]['url']}"
