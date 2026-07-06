import streamlit as st
from google import genai
from google.genai import types

# Configure the page layout
st.set_page_config(page_title="Gemma 4 Mega-Prompt Generator", page_icon="⚡", layout="centered")

st.title("⚡ Gemma 4 Mega-Prompt Generator")
st.caption("Transform raw ideas into production-ready system prompts instantly using Google AI Studio.")

# Securely grab your API Key 
# Best practice: Enter it in the sidebar or set it as an environment variable
api_key = st.sidebar.text_input("Enter Google AI Studio API Key", type="password")

# Model picker for Gemma 4 variants available in AI Studio
model_variant = st.sidebar.selectbox(
    "Select Gemma 4 Model",
    ["gemma-4-31b-it", "gemma-4-26b-a4b-it"],
    index=0
)

# Define the instant generation instructions for Gemma 4
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

# Text input for the user's raw idea
user_idea = st.text_area(
    "Enter your raw idea or task here:",
    placeholder="e.g., An AI that reviews resume text and gives constructive feedback based on tech industry standards...",
    height=150
)

if st.button("Generate Mega-Prompt 🔥", type="primary"):
    if not api_key:
        st.error("Please enter your Google AI Studio API Key in the sidebar!")
    elif not user_idea.strip():
        st.warning("Please enter an idea first!")
    else:
        with st.spinner("Gemma 4 is architecting your prompt via Google Cloud..."):
            try:
                # Initialize the official Google GenAI Client
                client = genai.Client(api_key=api_key)
                
                # Send request using Gemma 4 native system instructions
                response = client.models.generate_content(
                    model=model_variant,
                    contents=f"Architect a massive, robust system prompt for this idea: {user_idea}",
                    config=types.GenerateContentConfig(
                        system_instruction=SYSTEM_PROMPT,
                        temperature=0.6
                    )
                )
                
                st.success("Prompt Generated Successfully!")
                st.write("### Your Optimized Mega-Prompt:")
                
                # st.code provides an automatic "Copy to Clipboard" button in the UI
                st.code(response.text, language="markdown")
                st.info("💡 Click the copy icon in the top-right corner of the box above to copy your prompt instantly.")
                
            except Exception as e:
                st.error(f"An error occurred while calling the Gemini API: {e}")