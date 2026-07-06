# ⚡ Gemma 4 Mega-Prompt Generator Agent

An agentic Streamlit web application that leverages Google's open-weight **Gemma 4** models via the Google AI Studio SDK to transform raw, basic ideas into highly structured, production-grade System Prompts (Mega-Prompts) instantly.

## 🚀 Features
- **Instant Generation:** Skips tedious back-and-forth chatter to output an immediate, actionable mega-prompt.
- **Structured Framework:** Outputs prompts adhering to elite prompt-engineering layouts (Role, Objective, Context, Instructions, Constraints, and Output Format).
- **One-Click Copy:** Leverages Streamlit's native code blocks to let you copy your prompt instantly with a single click.
- **Cloud-Powered:** Powered by Google AI Studio's free-tier infrastructure using advanced Gemma 4 model variants (`gemma-4-31b-it`).

---

## 🛠️ Project Architecture

The application acts as a middle-tier orchestration layer between the user interface and Google's LLM endpoint:

1. **User Interface (Streamlit):** Captures the user's raw intent and managing configurations (API keys, model selections).
2. **System Guardrails:** Wraps your raw text inside an internal "Meta-Prompt Instruction" matrix.
3. **Inference Engine (Google GenAI SDK):** Transmits payload to cloud-hosted Gemma 4 instances.
4. **Output Rendering:** Sanitizes the response and presents it inside an interactive clipboard container.

---

## ⚙️ Installation & Setup

### 1. Prerequisites
Ensure you have **Python 3.9 to 3.11** installed on your machine. 

### 2. Clone or Create the Files
Create a new directory on your machine and place `app.py` and `requirements.txt` inside it.

### 3. Install Dependencies
Open your terminal inside the project directory and install the required modules:
```bash
pip install -r requirements.txt