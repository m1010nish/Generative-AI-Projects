"""
UI components module for AI Psychologist app
Contains reusable UI components and styling
"""

import streamlit as st

def apply_custom_css():
    """Apply custom CSS styling to the app"""
    st.markdown("""
    <style>
        .user-message {
            text-align: left;
            background-color: #444444;
            padding: 10px;
            border-radius: 10px;
            margin: 10px 0;
            border-left: 4px solid #0c5460;
            width: 80%;
            margin-left: auto; /* Pushes to the right */
        }

        .ai-message {
            text-align: left;
            background-color: #252525;
            padding: 10px;
            border-radius: 10px;
            margin: 10px 0;
            border-left: 4px solid #495057;
            width: 80%;
            margin-right: auto; /* Pushes to the left */
        }

        .stButton > button {
            width: 100%;
        }
    </style>
    """, unsafe_allow_html=True)

def render_disclaimer():
    """Render the disclaimer section"""
    with st.expander("⚠️ Important Disclaimer", expanded=True):
        st.markdown("""
        **This AI is not a licensed therapist or mental health professional.**
        
        - For crisis situations, contact emergency services
        - For professional help, visit [findahelpline.com](https://findahelpline.com)
        - This tool is for supportive conversation only
        """)

def render_chat_header():
    """Render the chat header"""
    st.markdown("<h1 style='text-align: center;'>🧠 AI Psychologist</h1>", 
               unsafe_allow_html=True)

def render_chat_input():
    """Render the chat input form and return user input and send button status"""
    with st.form("chat_form", clear_on_submit=True):
        user_input = st.text_area("Share what's on your mind...", 
                                height=80, 
                                placeholder="Type your message here...")
        send_button = st.form_submit_button("Send Message")
    
    return user_input, send_button