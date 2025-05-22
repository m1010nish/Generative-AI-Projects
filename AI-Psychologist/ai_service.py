"""
AI service module for AI Psychologist app
Handles communication with Ollama AI service
"""

import streamlit as st
import requests
import time

OLLAMA_API = "http://localhost:11434/api/generate"
AVAILABLE_MODELS = ["mistral:latest", "phi3", "llama2", "codellama"]

def get_ai_response(model, conversation_history, max_retries=3):
    """Get response from AI model with retry logic"""
    
    # Build conversation context
    full_convo = "\n".join(
        f"{'User' if m['role'] == 'user' else 'AI'}: {m['text']}"
        for m in conversation_history
    )
    
    prompt = f"""You are a caring, empathetic AI psychologist. Your role is to:
- Listen actively and respond with empathy
- Ask thoughtful follow-up questions when appropriate
- Provide supportive guidance while being non-judgmental
- Remember the conversation context
- Encourage professional help for serious issues

Important: You are not a replacement for professional mental health services.

Conversation so far:
{full_convo}

AI:"""
    
    for attempt in range(max_retries):
        try:
            response = requests.post(OLLAMA_API, json={
                "model": model,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0.7,
                    "top_p": 0.9
                }
            }, timeout=30)
            
            if response.status_code == 200:
                return response.json().get("response", "I apologize, but I couldn't generate a response.")
            else:
                if attempt == max_retries - 1:
                    return f"Error: Unable to connect to AI service (Status: {response.status_code})"
                time.sleep(1)  # Brief delay before retry
                
        except requests.exceptions.ConnectionError:
            if attempt == max_retries - 1:
                return "Error: Cannot connect to Ollama. Please ensure Ollama is running on localhost:11434"
            time.sleep(1)
        except requests.exceptions.Timeout:
            if attempt == max_retries - 1:
                return "Error: Request timed out. Please try again."
            time.sleep(1)
        except Exception as e:
            if attempt == max_retries - 1:
                return f"Error: {str(e)}"
            time.sleep(1)
    
    return "I apologize, but I'm having trouble responding right now. Please try again."

def test_ai_connection(model):
    """Test connection to AI service"""
    test_response = get_ai_response(model, [{"role": "user", "text": "Hello"}])
    return "Error" not in test_response

def render_ai_settings():
    """Render AI settings section"""
    st.markdown("### ⚙️ Settings")
    model = st.selectbox("Choose AI Model", AVAILABLE_MODELS, 
                       help="Select the AI model for responses")
    
    # Test connection
    if st.button("Test AI Connection"):
        with st.spinner("Testing connection..."):
            if test_ai_connection(model):
                st.success("✅ Connection successful")
            else:
                st.error("❌ Connection failed")
    
    return model