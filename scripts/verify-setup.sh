#!/bin/bash
export PATH="$HOME/.local/bin:$PATH"
export PYTHONPATH="/usr/local/lib/python3.12/dist-packages:.:${PYTHONPATH:-}"
cd "$HOME/peak-ai"
LOGFILE="$HOME/peak-ai/peak-ai-boot.log"
./scripts/test-full-features.sh | tee -a "$LOGFILE" || true
echo "Boot verification completed with possible warnings" >> "$LOGFILE"
