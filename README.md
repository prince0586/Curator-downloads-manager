📂 Curator downloads: Agentic File Curator

An autonomous AI agent designed to monitor your downloads folder and intelligently organize files using the Gemini 1.5 Flash model and the Watchdog library.

 
Getting Started
Follow these steps to set up the environment and run the agent on your local machine.

1. Navigate to the Project Directory
Open your terminal and use the cd command to enter your project folder.

Bash

**cd path/to/your/Digital-Janitor-Project**
2. Set Up a Virtual Environment
It is recommended to use a virtual environment to manage dependencies safely.

Bash

# Create the virtual environment
**python -m venv .venv**

# Activate the environment

# On Windows:
**.venv\Scripts\activate**

# On macOS/Linux:
**source .venv/bin/activate**

3. Install Dependencies
Install the necessary libraries for file system monitoring and AI integration.

Bash

**pip install watchdog google-generativeai**

4. Configure Your API Key
The agent requires a Google AI Studio API key to analyze file types. Replace YOUR_API_KEY with your actual key.

you will find api key in google AI studio.
**Windows (CMD): set GOOGLE_API_KEY=YOUR_API_KEY**

**macOS/Linux: export GOOGLE_API_KEY='YOUR_API_KEY'**

OR

**set api key in .env file, then put it in .gitegnore in github**

5. Run the Agent
Execute the main script to start monitoring your downloads.

Bash

**python curator.py**
🛑 How to Stop
**To stop the agent from monitoring your files, return to the terminal and press: Ctrl + C**

🛠️ How it Works
Watchdog: Monitors the file system for "Created" or "Moved" events in real-time.

Agentic Logic: When a new file is detected, the agent sends metadata to the Gemini model to determine the most logical category (e.g., "Invoices," "Software," "Research Papers").

Automation: The agent autonomously moves the file into the corresponding subfolder without any manual input.
