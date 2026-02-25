import gradio as gr
from src.orchestrator import main as run_orchestrator
def chat(message, history):
    response = run_orchestrator(message)
    return history + [[message, response]]
gr.ChatInterface(chat, title="Peak AI v7.9", description="Multi-modal chat with file upload and image preview").launch(server_name="0.0.0.0", server_port=7860)
