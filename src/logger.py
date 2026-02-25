import logging
import os
from datetime import datetime
os.makedirs("logs", exist_ok=True)
log_file = f"logs/peak-ai-{datetime.now().strftime('%Y-%m-%d')}.log"
logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s', handlers=[logging.FileHandler(log_file), logging.StreamHandler()])
logger = logging.getLogger("peak-ai")
