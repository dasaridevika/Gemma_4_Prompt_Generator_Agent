import streamlit as st
import os
from google import genai
from google.genai import types

# Configure the page layout
st.set_page_config(page_title="Gemma 4 Mega-Prompt Generator", page_icon="⚡", layout="centered")

st.title("⚡ Gemma 4 Mega-Prompt Generator")
st.caption("Transform raw ideas into production-ready system prompts instantly using Google AI Studio.")

# --- PERSISTENT API KEY MANAGEMENT ---
# Initialize session state for the API key if it doesn't exist
if "api_key" not in st.session_state:
    # Fallback check: see if it was set via local terminal environment variables
    st.session_state.api_key = os.environ.get("GEMINI_API_KEY", "")

# Sidebar UI for API Key management
st.sidebar.header("Configuration")

if not st.session_state.api_key:
    # If key is missing, display the input field
    input_key = st.sidebar.text_input("Enter Google AI Studio API Key", type="password", help="Your key will be saved for this active session.")
    if input_key:
        st.session_state.api_key = input_key
        st.rerun()  # Refresh immediately to update the UI state
else:
    # If key exists, lock it in and show a success status with a reset option
    st.sidebar.success("🔒 API Key Active & Locked")
    if st.sidebar.button("Reset / Change Key"):
        st.session_state.api_key = ""
        st.rerun()

# Model picker configuration
model_variant = st.sidebar.selectbox(
    "Select Gemma 4 Model",
    ["gemma-4-31b-it", "gemma-4-26b-a4b-it"],
    index=0
)

# --- SYSTEM METAPROMPT DEFINITION ---
SYSTEM_PROMPT = """
Role: You are a Master Prompt Engineer and AI Agent Architect. Your sole task is to take a raw, basic user idea and turn it into a world-class, highly robust, production-ready System Prompt (Mega-Prompt) immediately.

Structure your final output beautifully using markdown exactly like this:
- ## Role & Objective: Define exactly who the AI is and its primary goal.
- ## Context & Background: Explain why this task matters and the setting.
- ## Step-by-Step Instructions: A sequential breakdown of how the AI should think and process information.
- ## Constraints & Guardrails: Explicit rules to prevent hallucination, scope creep, or bad formatting.
- ## Output Format: Specify exactly how the final output should look (e.g., markdown, JSON, bullet points).

Be direct. Do not add any introductory or concluding conversational filler like "Here is your prompt:". Start directly with the first section.
"""

# Core user interface entry matrix
user_idea = st.text_area(
    "Enter your raw idea or task here:",
    placeholder="e.g., An AI that reviews resume text and gives constructive feedback...",
    height=150
)

if st.button("Generate Mega-Prompt 🔥", type="primary"):
    if not st.session_state.api_key:
        st.error("Authentication missing: Please provide your Google AI Studio API Key in the sidebar.")
    elif not user_idea.strip():
        st.warning("Payload empty: Please enter an infrastructure idea first.")
    else:
        with st.spinner("Gemma 4 is architecting your prompt via Google Cloud..."):
            try:
                # Initialize the client using the persistent session state key
                client = genai.Client(api_key=st.session_state.api_key)
                
                # Execute inference payload
                response = client.models.generate_content(
                    model=model_variant,
                    contents=f"Architect a massive, robust system prompt for this idea: {user_idea}",
                    config=types.GenerateContentConfig(
                        system_instruction=SYSTEM_PROMPT,
                        temperature=0.6
                    )
                )
                
                st.success("Compilation Successful!")
                st.write("### Your Optimized Mega-Prompt:")
                
                # st.code provides an automatic "Copy to Clipboard" button in the UI
                st.code(response.text, language="markdown")
                st.info("💡 Prompt compiled seamlessly. Use the native clipboard icon above to copy the matrix.")
                
            except Exception as e:
                st.error(f"Inference Failure: An error occurred during the API lifecycle call: {e}")