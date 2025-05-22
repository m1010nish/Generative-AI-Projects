"""
Configuration module for AI Psychologist app
Contains all configuration constants and settings
"""

# File paths
USERS_FILE = 'users.yaml'
CHAT_SESSIONS_DIR = 'chat_sessions'

# AI Service settings
OLLAMA_API = "http://localhost:11434/api/generate"
AVAILABLE_MODELS = ["mistral:latest", "phi3", "llama2", "codellama"]

# Authentication settings
DEFAULT_CONFIG = {
    'credentials': {'usernames': {}},
    'cookie': {
        'name': 'ai_psychologist_auth',
        'key': 'random_signature_key_12345',  # Change this in production
        'expiry_days': 30
    }
}

# UI settings
PAGE_CONFIG = {
    'page_title': "AI Psychologist",
    'layout': "wide",
    'page_icon': "🧠",
    'initial_sidebar_state': "expanded"
}

# AI prompt template
AI_SYSTEM_PROMPT = """You are a caring, empathetic AI psychologist. Your role is to:
- Listen actively and respond with empathy
- Ask thoughtful follow-up questions when appropriate
- Provide supportive guidance while being non-judgmental
- Remember the conversation context
- Encourage professional help for serious issues

Important: You are not a replacement for professional mental health services.

Conversation so far:
{conversation}

AI:"""

# Validation rules
MIN_USERNAME_LENGTH = 3
MIN_PASSWORD_LENGTH = 6

# API settings
AI_REQUEST_TIMEOUT = 30
MAX_RETRIES = 3
AI_TEMPERATURE = 0.7
AI_TOP_P = 0.9

# Chat settings
MAX_DISPLAYED_CHATS = 10