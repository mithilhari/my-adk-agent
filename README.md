To get the complete `README.md` file content, here is the full text, ready for you to copy and paste into the `README.md` file in your `my-adk-agent` repository.

-----

# ADK Fact-Checking Agent 🕵️

This repository contains an advanced AI agent built using the **Google Agent Development Kit (ADK)**. It utilizes the Gemini model to perform **fact-checking** by integrating the built-in **Google Search tool** and enforcing a **structured JSON output** via the Pydantic library.

The agent's core logic is defined in `greeter_agent/agent.py`.

-----

## 🚀 Complete Setup and Installation

Follow these three critical steps to set up the project, install dependencies, and configure your API key.

### Step 1: Clone the Repository

Clone the project using your GitHub repository URL and move into the directory:

```bash
git clone https://github.com/mithilhari/my-adk-agent.git
cd my-adk-agent
```

### Step 2: Environment and Dependencies

You **must** use a Python virtual environment (`.venv`) for isolated development.

1.  **Create and Activate the Environment:**

    ```bash
    # Create the virtual environment
    python -m venv .venv

    # Activate the environment (REQUIRED for all subsequent commands)
    # For macOS/Linux:
    source .venv/bin/activate
    # For Windows (Command Prompt):
    # .venv\Scripts\activate.bat
    # For Windows (PowerShell):
    # .venv\Scripts\Activate.ps1
    ```

2.  **Install Dependencies:**

    ```bash
    # This installs google-adk, pydantic, and other requirements
    pip install -r requirements.txt
    ```

### Step 3: API Key Configuration (Crucial\!)

The agent requires your Google AI API key to access the Gemini model and execute the Google Search tool.

1.  Create the environment file at: **`greeter_agent/.env`**
2.  Add your API key using the format below (replace `YOUR_API_KEY_HERE`):

<!-- end list -->

```ini
GOOGLE_API_KEY=YOUR_API_KEY_HERE
```

> ⚠️ **Security Note:** The `.gitignore` file is configured to exclude `greeter_agent/.env`, ensuring your secret key is **never** committed to GitHub.

-----

## 🧪 Running the Agent Locally

Once the setup is complete and your virtual environment is **active**, you can run the agent for a test fact-check.

### Execution Command

```bash
python greeter_agent/agent.py
```

### Expected Output

The agent is designed to verify the statement: `"The capital of Australia is Sydney."` The output will show the agent's logic, including the final structured result:

```
--- Running ADK Fact-Checker Agent Locally ---
User Statement: The capital of Australia is Sydney.
... (Internal agent reasoning and tool usage)

--- Agent Result (Parsed JSON Object) ---
Is Correct: False
Verified Fact: The capital city of Australia is Canberra.
Explanation: The agent used the Google Search tool and confirmed that while Sydney is Australia's largest city, the official capital is Canberra.
```

-----

## 🛑 Troubleshooting & Common Errors

### Error: `ModuleNotFoundError: No module named 'google.adk.runner'`

**Cause:** You did not activate the virtual environment (`.venv`) before running the script.

**Solution:** Always ensure your terminal prompt shows `(.venv)` or similar before running the script:

```bash
# Rerun this command
source .venv/bin/activate
python greeter_agent/agent.py
```

### Error: `error: src refspec main does not match any`

**Cause:** Your local Git branch is likely named `master`, but GitHub expects `main`.

**Solution:** Use these commands to fix the branch name and push successfully:

1.  **Ensure your files are committed:**

    ```bash
    git add .
    git commit -m "Finalizing ADK setup"
    ```

2.  **Rename the local branch to `main`:**

    ```bash
    git branch -M main
    ```

3.  **Push to the remote repository:**

    ```bash
    git push -u origin main
    ```
