import docker
def run(code: str):
    try:
        client = docker.from_env()
        result = client.containers.run("python:3.12-slim", f"python -c '{code}'", remove=True)
        return result.decode().strip()
    except Exception as e:
        return f"Execution failed: {e}"
