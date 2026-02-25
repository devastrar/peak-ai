from src.agents.flux_agent import run as flux_run
def run(mermaid_code: str):
    prompt = f"Render this Mermaid diagram as a beautiful professional image: {mermaid_code}"
    return flux_run(prompt)
