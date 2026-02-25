import git
def run(action: str, message: str = ""):
    repo = git.Repo(".")
    if action == "commit":
        repo.index.add("*")
        repo.index.commit(message)
        return "Committed successfully"
    return "Git action completed"
