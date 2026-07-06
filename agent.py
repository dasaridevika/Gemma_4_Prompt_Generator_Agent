import json
import requests

# Ollama's local server URL
URL = "http://localhost:11434/api/chat"

# The system prompt that guides Gemma 4 to act as your agent
system_prompt = """
Role: You are a Master Prompt Engineer. Your purpose is to turn a raw user idea into a world-class System Prompt.
Process: Do NOT generate the prompt immediately. Ask 2 clarifying questions to understand constraints and target output. 
Once the user answers, give them a structured prompt layout.
"""

def talk_to_agent(user_message, chat_history=[]):
    # Gemma 4 natively supports the 'system' role
    messages = [{"role": "system", "content": system_prompt}] + chat_history
    messages.append({"role": "user", "content": user_message})
    
    payload = {
        "model": "gemma4:12b",
        "messages": messages,
        "stream": False
    }
    
    response = requests.post(URL, json=payload)
    return response.json()['message']['content']

# Example interaction loop
print("Agent: Tell me your raw idea!")
idea = input("You: ")
response = talk_to_agent(idea)
print(f"\nAgent:\n{response}")