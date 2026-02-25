#!/bin/bash
export PATH="$HOME/.local/bin:$PATH"
export PYTHONPATH="/usr/local/lib/python3.12/dist-packages:.:${PYTHONPATH:-}"
cd "$HOME/peak-ai"
./scripts/test-full-features.sh | tee -a /var/log/peak-ai-boot.log || true
echo "Boot verification completed with possible warnings" >> /var/log/peak-ai-boot.log
