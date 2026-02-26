import sys
import argparse
import os
from dotenv import load_dotenv
from datetime import datetime
from src.config_manager import get_default_project, update_setting
from src.context_manager import load_memory, save_memory, build_context_prompt
from src.logger import logger
load_dotenv(".env")

def determine_agent(query: str):
    q = query.lower()
    if any(word in q for word in ["image", "picture", "photo", "generate", "draw", "art", "illustration", "flux", "visual"]):
        return "flux"
    elif any(word in q for word in ["fast", "quick", "summary", "short", "brief"]):
        return "minimax"
    return "kimi"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("query", nargs="+", help="Your request")
    parser.add_argument("--project", default=None)
    args = parser.parse_args()
    query = " ".join(args.query)
    project = args.project or get_default_project()

    if args.project:
        update_setting("default_project", project)

    memory = load_memory(project)
    context = build_context_prompt(memory)

    agent = determine_agent(query)
    logger.info(f"Orchestrator - Query: {query} - Project: {project} - Agent: {agent}")

    print(f"🚀 Peak AI Orchestrator v8.6")
    print(f"Query: {query}")
    print(f"Project: {project}")
    print(f"Selected agent: {agent.upper()}")

    if agent == "flux":
        from src.agents.flux_agent import run
        result = run(query)
    elif agent == "minimax":
        from src.agents.minimax_agent import run
        result = run(query, context, project)
    else:
        from src.agents.kimi_agent import run
        result = run(query, context, project)

    print(f"✅ {agent.upper()} response:\n{result}")

    if project:
        try:
            memory.setdefault("logs", []).append({"timestamp": datetime.now().isoformat(), "query": query, "response": result[:300]})
            save_memory(project, memory)
            logger.info(f"Context saved to projects/{project}/")
        except Exception as e:
            logger.error(f"Memory save error: {e}")

if __name__ == "__main__":
    main()
