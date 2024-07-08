#!/bin/bash

# Ensure zsh is installed
if ! command -v zsh &> /dev/null; then
    echo "zsh is not installed. Installing zsh..."
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # Install zsh on macOS using Homebrew
        if ! command -v brew &> /dev/null; then
            echo "Homebrew is not installed. Installing Homebrew first..."
            /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
        fi
        brew install zsh
    else
        echo "Please install zsh manually."
        exit 1
    fi
fi

# Change the default shell to zsh
if [[ "$SHELL" != "/bin/zsh" ]]; then
    echo "Changing default shell to zsh..."
    chsh -s /bin/zsh
    echo "Default shell changed to zsh. Please log out and log back in for the change to take effect."
fi

# Prompt the user for the project directory path
read -p "Please enter the full path to your project directory: " PROJECT_DIR

# Check if the entered path is valid
if [ ! -d "$PROJECT_DIR" ]; then
    echo "The directory $PROJECT_DIR does not exist. Please check the path and try again."
    exit 1
fi

# Set PROJECT_DIR environment variable in .zshrc
ZSHRC_PATH="$HOME/.zshrc"

if grep -q "export PROJECT_DIR=" "$ZSHRC_PATH"; then
    echo "PROJECT_DIR is already set in .zshrc"
else
    echo "Adding PROJECT_DIR to .zshrc..."
    echo "export PROJECT_DIR=\"$PROJECT_DIR\"" >> "$ZSHRC_PATH"
    echo 'export PATH="$PROJECT_DIR/venv/bin:$PATH"' >> "$ZSHRC_PATH"
fi

# Reload .zshrc to apply changes
echo "Reloading .zshrc..."
source "$ZSHRC_PATH"

# Navigate to the project directory
cd "$PROJECT_DIR" || { echo "Directory $PROJECT_DIR does not exist."; exit 1; }

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    python -m venv venv
fi

# Activate the virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install or update dependencies
pip install -r requirements.txt

# Check for updates and install them
pip-review --auto

# Animation for fun
animation() {
    frames=(
        "🚀 Preparing for launch...       "
        "🚀 Preparing for launch..       "
        "🚀 Preparing for launch.       "
        "🚀 Ready to take off! 🚀       "
    )
    while :; do
        for frame in "${frames[@]}"; do
            echo -ne "\r$frame"
            sleep 0.5
        done
    done
}

# Run the animation in the background
animation &
ANIMATION_PID=$!

# Stop the animation after a delay
sleep 5
kill $ANIMATION_PID
echo -ne "\rSetup complete. Virtual environment is activated and dependencies are up to date.          \n"
echo "Please restart your terminal session or run 'zsh' to start using zsh."

# More inspirational message
cat << "EOF"
   _____  _                          _____                          _             
  / ____|| |                        / ____|                        (_)            
 | (___  | |_  _   _  _ __    ___  | |       _ __   ___   ___  ___  _  _ __   ___ 
  \___ \ | __|| | | || '_ \  / _ \ | |      | '__| / _ \ / __|/ __|| || '_ \ / __|
  ____) || |_ | |_| || | | ||  __/ | |____  | |   |  __/|__  \__  \| || | | | (__ 
 |_____/  \__| \__,_||_| |_| \___|  \_____| |_|    \___||___/|___/|_||_| |_|\___|
EOF

echo "Welcome Intro to Programming! 🚀"