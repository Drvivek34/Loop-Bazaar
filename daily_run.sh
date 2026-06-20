#!/bin/bash
# Exit on any error
set -e

# Log date and run start
echo "=== Starting Daily Loop Library Update: $(date) ==="

# Go to the repository directory
cd /root/github-loop-library

# Load environment variables to ensure SSH keys and API keys are loaded in cron
if [ -f "$HOME/.profile" ]; then
    source "$HOME/.profile"
fi
if [ -f "$HOME/.bashrc" ]; then
    source "$HOME/.bashrc"
fi

# Ensure git is safe and updated
git checkout main
git pull origin main || echo "Pull failed (perhaps first run or no remote yet), continuing..."

# Run python update script
python3 update_library.py

echo "=== Finished Daily Loop Library Update: $(date) ==="
