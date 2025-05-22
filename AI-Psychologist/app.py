"""
Main application file for AI Psychologist
Imports and orchestrates all modules
"""

import streamlit as st
from datetime import datetime

# Import custom modules
from auth import create_account_page, authenticate_user
from chat_manager import (
    ensure_directories, create_new_session, save_chat,
    render_chat_sidebar, render_chat_messages
)
from ai_service import get_ai_response, render_ai_settings
from ui_components import (
    apply_custom_css, render_disclaimer, 
    render_chat_header, render_chat_input
)

def initialize_session_state():
    """Initialize session state variables"""
    if "current_chat" not in st.session_state:
        st.session_state.current_chat = create_new_session()
        st.session_state.chat_history = []

def main():
    """Main application function"""
    st.set_page_config(
        page_title="AI Psychologist", 
        layout="wide",
        page_icon="🧠",
        initial_sidebar_state="expanded"
    )
    
    # Apply custom styling
    apply_custom_css()
    
    # Ensure required directories exist
    ensure_directories()
    
    # Navigation
    page = st.sidebar.selectbox("Navigation", ["Login", "Create Account"])
    
    # ===================== CREATE ACCOUNT PAGE =====================
    if page == "Create Account":
        create_account_page()

    # ===================== LOGIN & CHAT PAGE =====================
    elif page == "Login":
        auth_status, name, username, authenticator = authenticate_user()

        if auth_status:
            # Successful login
            st.sidebar.success(f"Welcome {name}!")
            authenticator.logout('Logout', 'sidebar')
            
            # Initialize session state
            initialize_session_state()
            
            # Main layout
            left_col, right_col = st.columns([1, 3])
            
            # ===================== LEFT SIDEBAR =====================
            with left_col:
                # Chat management
                render_chat_sidebar(username)
                
                # AI settings
                model = render_ai_settings()
                
                # Disclaimer
                render_disclaimer()
            
            # ===================== RIGHT CHAT AREA =====================
            with right_col:
                # Chat header
                render_chat_header()
                
                # Chat display area
                chat_container = st.container()
                with chat_container:
                    render_chat_messages()
                
                # Chat input area
                user_input, send_button = render_chat_input()
                
                # Handle message sending
                if send_button and user_input.strip():
                    # Add user message
                    st.session_state.chat_history.append({
                        "role": "user", 
                        "text": user_input.strip(),
                        "timestamp": datetime.now().isoformat()
                    })
                    
                    # Show spinner while getting AI response
                    with st.spinner("AI is thinking..."):
                        ai_response = get_ai_response(model, st.session_state.chat_history)
                    
                    # Add AI response
                    st.session_state.chat_history.append({
                        "role": "ai", 
                        "text": ai_response,
                        "timestamp": datetime.now().isoformat()
                    })
                    
                    # Save chat
                    save_chat(username, st.session_state.current_chat, st.session_state.chat_history)
                    st.rerun()

        elif auth_status is False:
            st.error("❌ Username or password is incorrect")
        elif auth_status is None:
            st.info("👋 Please enter your username and password to continue")

if __name__ == "__main__":
    main()