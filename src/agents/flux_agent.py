import os
import fal_client
from dotenv import load_dotenv
load_dotenv(".env")
def run(query: str):
    falkey = os.getenv("FAL_API_KEY")
    if ':' in falkey:
        os.environ["FAL_KEY"] = falkey
    else:
        os.environ["FAL_KEY"] = f"{os.getenv('FAL_KEY_ID')}:{os.getenv('FAL_KEY_SECRET')}"
    result = fal_client.run("fal-ai/flux/schnell", arguments={"prompt": query, "image_size": "square", "num_inference_steps": 4})
    return f"✅ Image generated: {result['images'][0]['url']}"
