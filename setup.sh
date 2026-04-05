#!/bin/bash
set -e

REPO_URL="https://github.com/OhadRubin/jexpand.git"
INSTALL_DIR="$HOME/.jexpand"

echo "Installing jexpand..."

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "uv not found. Installing uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.local/bin:$PATH"
fi

# Clone or update repo
if [ -d "$INSTALL_DIR" ]; then
    echo "Updating existing installation..."
    cd "$INSTALL_DIR"
    git pull
else
    echo "Cloning jexpand..."
    git clone "$REPO_URL" "$INSTALL_DIR"
fi

# Install with uv tool
echo "Installing jexpand globally..."
uv tool install -e "$INSTALL_DIR" --force

# Check if ~/.local/bin is in PATH
if [[ ":$PATH:" != *":$HOME/.local/bin:"* ]]; then
    echo ""
    echo "Add this to your shell profile (~/.bashrc or ~/.zshrc):"
    echo '  export PATH="$HOME/.local/bin:$PATH"'
    echo ""
fi

echo "Done! Run 'jexpand --help' to get started."
