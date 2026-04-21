🏙️ TownAi
TownAi is a specialized automation tool designed to assist with Townsend Press assignments using AI integration. It uses Playwright for browser automation and any OpenAI-compatible SDK (like DeepSeek) to analyze and answer questions in real-time.

✨ Features
AI-Powered Answers: Connects to DeepSeek (or OpenAI) to solve questions based on directions and options.

Smart History: Keeps track of previous questions in the session to maintain context.

Auto-Navigation: Automatically clicks the correct answers and moves to the next question.

Cool Terminal UI: Features ASCII art and a "typewriter" style loading sequence.

Token Verification: Automatically checks if your API key is valid before starting the browser.

🛠️ Prerequisites
Before running the code, ensure you have Python 3.8+ installed. You will also need to install the following libraries:

Bash
pip install playwright openai keyboard
playwright install chromium
🚀 How to Use
1. Configuration
Open the script and replace the placeholder values with your own credentials:

API Key: Change [ENCRYPTION_KEY] to your DeepSeek or OpenAI API key.

Login Credentials: Update the username.fill() and password.fill() lines with your Townsend Press login details.

2. Running the Script
Run the script via your terminal:

Bash
python main.py
3. The Process
Initialization: The script will print the TownAi logo and verify your API connection.

Browser Launch: A Chrome window will open and automatically log you into Townsend Press.

Manual Check: The terminal will say Press Enter to continue.... Stop here. * Manually navigate to the specific assignment you want to complete.

Once you are on the question page, go back to the terminal and press Enter.

Automation: The AI will now begin reading the questions, selecting the answers, and clicking "Continue" automatically.

⌨️ Controls
Manual Pause: You can interact with the browser at any time.

Stop Script: Press Ctrl + C in the terminal to safely shut down the automation.

⚠️ Disclaimer
Note: This tool is for educational and research purposes only. Using automation for school assignments may violate your institution's academic integrity policy. Use at your own risk.
