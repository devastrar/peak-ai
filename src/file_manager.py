import os
def get_project_dir(project_name: str):
    path = f"projects/{project_name}"
    os.makedirs(path, exist_ok=True)
    return path
def write_file(project_name: str, filename: str, content: str):
    full_path = os.path.join(get_project_dir(project_name), filename)
    with open(full_path, "w") as f:
        f.write(content)
    return full_path
def read_file(project_name: str, filename: str):
    full_path = os.path.join(get_project_dir(project_name), filename)
    if os.path.exists(full_path):
        with open(full_path, "r") as f:
            return f.read()
    return None
