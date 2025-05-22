"""
Authentication module for AI Psychologist app
Handles user registration, login, and password management
"""

import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import bcrypt
import os
from config import USERS_FILE, DEFAULT_CONFIG, MIN_USERNAME_LENGTH, MIN_PASSWORD_LENGTH

def load_users():
    """Load user configuration from YAML file"""
    try:
        if os.path.exists(USERS_FILE):
            with open(USERS_FILE, 'r') as file:
                return yaml.load(file, Loader=SafeLoader)
        else:
            # Create default config if file doesn't exist
            save_users(DEFAULT_CONFIG)
            return DEFAULT_CONFIG
    except Exception as e:
        st.error(f"Error loading users: {e}")
        return None

def save_users(config):
    """Save user configuration to YAML file"""
    try:
        with open(USERS_FILE, 'w') as file:
            yaml.dump(config, file, default_flow_style=False)
        return True
    except Exception as e:
        st.error(f"Error saving users: {e}")
        return False

def hash_password(password):
    """Hash password using bcrypt"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def validate_password(password):
    """Validate password strength"""
    if len(password) < MIN_PASSWORD_LENGTH:
        return False, f"Password must be at least {MIN_PASSWORD_LENGTH} characters long"
    return True, "Password is valid"

def validate_username(username):
    """Validate username format"""
    if len(username) < MIN_USERNAME_LENGTH:
        return False, f"Username must be at least {MIN_USERNAME_LENGTH} characters long"
    if not username.replace('_', '').replace('-', '').isalnum():
        return False, "Username can only contain letters, numbers, hyphens, and underscores"
    return True, "Username is valid"

def create_account_page():
    """Render the create account page"""
    st.title("📝 Create New Account")
    
    with st.form("create_account_form"):
        new_name = st.text_input("Full Name", help="Your full name for personalization")
        new_username = st.text_input("Username", help="Choose a unique username")
        new_password = st.text_input("Password", type="password", help="At least 6 characters")
        create_button = st.form_submit_button("Create Account")
    
    if create_button:
        if not (new_name and new_username and new_password):
            st.error("Please fill in all fields.")
        else:
            # Validate inputs
            username_valid, username_msg = validate_username(new_username)
            password_valid, password_msg = validate_password(new_password)
            
            if not username_valid:
                st.error(username_msg)
            elif not password_valid:
                st.error(password_msg)
            else:
                config = load_users()
                if config is None:
                    st.error("Unable to load user configuration.")
                elif new_username in config['credentials']['usernames']:
                    st.error("Username already exists. Please choose another.")
                else:
                    hashed_pw = hash_password(new_password)
                    config['credentials']['usernames'][new_username] = {
                        'name': new_name,
                        'password': hashed_pw
                    }
                    if save_users(config):
                        st.success("Account created successfully! Please go to the login page.")
                        st.balloons()
                    else:
                        st.error("Failed to create account. Please try again.")

def authenticate_user():
    """Handle user authentication and return auth status, name, username"""
    config = load_users()
    if config is None:
        st.error("Cannot load user configuration. Please check your setup.")
        return None, None, None
    
    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days']
    )

    authenticator.login(location='main')
    
    # Access authentication status from session state
    auth_status = st.session_state.get('authentication_status')
    name = st.session_state.get('name')
    username = st.session_state.get('username')
    
    return auth_status, name, username, authenticator