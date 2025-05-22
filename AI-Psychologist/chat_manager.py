"""
Chat management module for AI Psychologist app
Handles chat session creation, loading, saving, and management
"""

import streamlit as st
import os
import json
from datetime import datetime

CHAT_SESSIONS_DIR = 'chat_sessions'

def ensure_directories():
    """Ensure required directories exist"""
    os.makedirs(CHAT_SESSIONS_DIR, exist_ok=True)

def get_user_chat_dir(username):
    """Get user-specific chat directory"""
    user_dir = os.path.join(CHAT_SESSIONS_DIR, username)
    os.makedirs(user_dir, exist_ok=True)
    return user_dir

def user_chat_path(username, filename):
    """Get full path to user's chat file"""
    return os.path.join(get_user_chat_dir(username), filename)

def list_chats(username):
    """List all chat files for a user"""
    try:
        user_dir = get_user_chat_dir(username)
        files = [f for f in os.listdir(user_dir) if f.endswith(".json")]
        return sorted(files, reverse=True)
    except Exception:
        return []

def format_filename(filename):
    """Format filename for display"""
    try:
        dt = datetime.strptime(filename.replace("chat_", "").replace(".json", ""), "%Y%m%d_%H%M%S")
        return dt.strftime("%d-%m-%Y %H:%M:%S")
    except ValueError:
        return filename.replace(".json", "")

def load_chat(username, filename):
    """Load chat history from file"""
    try:
        with open(user_chat_path(username, filename), "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        st.error(f"Error loading chat: {e}")
        return []

def save_chat(username, filename, history):
    """Save chat history to file"""
    try:
        with open(user_chat_path(username, filename), "w", encoding="utf-8") as f:
            json.dump(history, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        st.error(f"Error saving chat: {e}")
        return False

def create_new_session():
    """Create new chat session filename"""
    return f"chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

def delete_chat(username, filename):
    """Delete a chat file"""
    try:
        os.remove(user_chat_path(username, filename))
        return True
    except Exception as e:
        st.error(f"Error deleting chat: {e}")
        return False

def render_chat_sidebar(username):
    """Render the chat sessions sidebar"""
    st.markdown("## 💬 Chat Sessions")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("➕ New Chat"):
            st.session_state.current_chat = create_new_session()
            st.session_state.chat_history = []
            st.rerun()
    
    # List existing chats
    chat_files = list_chats(username)
    if chat_files:
        st.markdown("### Recent Chats")
        for file in chat_files[:10]:  # Show only last 10 chats
            col1, col2 = st.columns([3, 1])
            with col1:
                if st.button(format_filename(file), key=f"load_{file}"):
                    st.session_state.current_chat = file
                    st.session_state.chat_history = load_chat(username, file)
                    st.rerun()
            with col2:
                if st.button("🗑️", key=f"delete_{file}", help="Delete chat"):
                    if delete_chat(username, file):
                        if st.session_state.current_chat == file:
                            st.session_state.current_chat = create_new_session()
                            st.session_state.chat_history = []
                        st.rerun()

def render_chat_messages():
    """Render chat messages in the chat area"""
    if not st.session_state.chat_history:
        st.markdown("""
        <div style='text-align: center; padding: 50px; color: #666;'>
        <h3>Welcome! How can I help you today?</h3>
        <p>Feel free to share what's on your mind. I'm here to listen and support you.</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        for entry in st.session_state.chat_history:
            role, text = entry["role"], entry["text"]
            if role == "user":
                st.markdown(f"""
                <div class='user-message'>
                <strong>You:</strong> {text}
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class='ai-message'>
                <strong>AI:</strong> {text}
                </div>
                """, unsafe_allow_html=True)