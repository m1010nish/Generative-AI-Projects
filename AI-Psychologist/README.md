# 🧠 AI Psychologist - Mental Health Support Chatbot

A compassionate AI-powered mental health support application built with Streamlit and Ollama. This application provides a safe space for users to share their thoughts and receive empathetic responses from an AI trained to offer supportive guidance.

![AI Psychologist Demo](https://img.shields.io/badge/Status-Active-brightgreen)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28.0+-red)

## ✨ Features

- 🔐 **Secure Authentication**: User registration and login with password hashing
- 💬 **Chat Management**: Create, save, load, and delete chat sessions
- 🤖 **Multiple AI Models**: Support for various Ollama models (Mistral, Phi3, Llama2, etc.)
- 📱 **Responsive Design**: Clean, modern interface with dark theme
- 💾 **Persistent Storage**: Chat history saved locally with user isolation
- 🔒 **Privacy Focused**: All data stored locally, no external data sharing
- ⚡ **Real-time Responses**: Fast AI responses with retry logic and error handling
- 🎨 **Custom Styling**: Beautiful chat interface with user/AI message distinction

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- [Ollama](https://ollama.ai/) installed and running
- Git (for cloning the repository)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/m1010nish/Generative-AI-Projects.git
   cd Generative-AI-Projects/AI-Psychologist
   ```

2. **Create a virtual environment**
   ```bash
   conda create --name AI-Psychologist
   conda activate AI-Psychologist
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install and start Ollama**
   - Download Ollama from [https://ollama.ai/](https://ollama.ai/)
   - Install at least one model:
     ```bash
     ollama pull mistral:latest
     # or
     ollama pull phi3
     ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

6. **Open your browser**
   - Navigate to `http://localhost:8501`
   - Create an account and start chatting!

## 📁 Project Structure

```
ai-psychologist/
├── app.py                 # Main application entry point
├── auth.py               # Authentication and user management
├── chat_manager.py       # Chat session management
├── ai_service.py         # AI model integration
├── ui_components.py      # UI components and styling
├── config.py             # Configuration settings
├── requirements.txt      # Python dependencies
├── README.md            # Project documentation
├── users.yaml           # User credentials (auto-generated)
└── chat_sessions/       # User chat data (auto-generated)
    └── [username]/      # Individual user folders
        └── *.json       # Chat session files
```

## 🔧 Configuration

### AI Models

The application supports multiple Ollama models. You can configure available models in `config.py`:

```python
AVAILABLE_MODELS = ["mistral:latest", "phi3", "llama2", "codellama"]
```

### Authentication Settings

Update authentication settings in `config.py`:

```python
DEFAULT_CONFIG = {
    'cookie': {
        'name': 'ai_psychologist_auth',
        'key': 'your-secret-key-here',  # Change in production
        'expiry_days': 30
    }
}
```

### AI Response Configuration

Customize AI behavior:

```python
AI_TEMPERATURE = 0.7      # Response creativity (0.0-1.0)
AI_TOP_P = 0.9           # Response diversity (0.0-1.0)
AI_REQUEST_TIMEOUT = 30   # Request timeout in seconds
MAX_RETRIES = 3          # Retry attempts for failed requests
```

## 🖥️ Usage Guide

### Creating an Account

1. Launch the application
2. Select "Create Account" from the sidebar
3. Fill in your details:
   - Full Name
   - Username (3+ characters, alphanumeric)
   - Password (6+ characters)
4. Click "Create Account"

### Starting a Chat Session

1. Login with your credentials
2. Click "➕ New Chat" to start a new session
3. Type your message in the input area
4. Click "Send Message" or press Enter

### Managing Chat Sessions

- **Load Previous Chat**: Click on any chat from the "Recent Chats" list
- **Delete Chat**: Click the 🗑️ button next to any chat
- **Switch Models**: Use the dropdown in Settings to change AI models
- **Test Connection**: Use "Test AI Connection" to verify Ollama is running

## 🛡️ Privacy & Security

- **Local Storage**: All data is stored locally on your machine
- **Password Security**: Passwords are hashed using bcrypt
- **Session Management**: Secure session handling with cookies
- **No External Data**: No chat data is sent to external services
- **User Isolation**: Each user's chats are stored separately

## ⚠️ Important Disclaimer

**This AI is not a licensed therapist or mental health professional.**

### 🚨 India Emergency Mental Health Helplines

- **AASRA**: 9820466726 (24x7 Crisis Helpline)
- **Vandrevala Foundation**: 9999 666 555 (24x7)
- **iCall**: 9152987821 (Mon-Sat, 8 AM - 10 PM)
- **COOJ Mental Health Foundation**: 9152987821
- **Sneha Foundation**: 044-24640050 (Chennai)
- **Sumaitri**: 011-23389090 (Delhi)
- **Parivarthan**: 0877-2339999 (Vijayawada)
- **National Emergency Number**: 112

### 🏥 Professional Mental Health Resources (India)

- **NIMHANS**: [nimhans.ac.in](https://nimhans.ac.in) - National Institute of Mental Health
- **Government Mental Health Centers**: Available in all districts under DMHP
- **Ayushman Bharat**: Mental health services at primary care centers
- Licensed psychiatrists and psychologists in your area

### 📋 Legal Notice

- This tool is for supportive conversation only
- Not a substitute for professional medical advice or treatment
- Seek immediate professional help for serious mental health concerns
- Compliant with Indian healthcare regulations and Mental Healthcare Act, 2017

## 🔧 Troubleshooting

### Common Issues

**"Cannot connect to Ollama"**
- Ensure Ollama is installed and running
- Check if Ollama is accessible at `http://localhost:11434`
- Try: `ollama serve` in terminal

**"Authentication Error"**
- Delete `users.yaml` to reset user database
- Check file permissions in the project directory

**"Module not found"**
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Activate your virtual environment

**Chat not saving/loading**
- Check write permissions in the project directory
- Ensure `chat_sessions/` directory exists

### Performance Tips

- Use lighter models (phi3) for faster responses
- Reduce `AI_TEMPERATURE` for more consistent responses
- Increase `AI_REQUEST_TIMEOUT` for complex queries

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make your changes**
4. **Test thoroughly**
5. **Commit your changes**
   ```bash
   git commit -m "Add amazing feature"
   ```
6. **Push to the branch**
   ```bash
   git push origin feature/amazing-feature
   ```
7. **Open a Pull Request**

### Development Setup

```bash
# Clone your fork
git clone https://github.com/m1010nish/Generative-AI-Projects.git
cd Generative-AI-Projects/AI-Psychologist

# Create development environment
conda create --name AI-Psychologist
conda activate AI-Psychologist

# Install in development mode
pip install -r requirements.txt

# Start development server
streamlit run app.py
```

## 📋 Roadmap

- [ ] **Enhanced AI Models**: Support for more specialized therapy models
- [ ] **Export Conversations**: PDF/text export functionality
- [ ] **Mood Tracking**: Visual mood tracking over time
- [ ] **Crisis Detection**: Enhanced crisis detection and resource linking
- [ ] **Multi-language Support**: Support for multiple languages
- [ ] **Voice Integration**: Speech-to-text and text-to-speech
- [ ] **Therapist Dashboard**: Optional professional oversight features


## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) for the amazing web framework
- [Ollama](https://ollama.ai/) for local AI model serving
- [streamlit-authenticator](https://github.com/mkhorasani/Streamlit-Authenticator) for authentication
- The open-source community for inspiration and support

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/m1010nish/Generative-AI-Projects/issues)
- **Discussions**: [GitHub Discussions](https://github.com/m1010nish/Generative-AI-Projects/discussions)
- **Email**: manishsinghjnv11@gmail.com

## 🌟 Star History

If this project helped you, please consider giving it a star! ⭐

---

**Remember**: This is a supportive tool, not a replacement for professional mental health care. Always seek professional help when needed.

[![Made with ❤️ and Python](https://img.shields.io/badge/Made%20with-❤️%20and%20Python-red)](https://python.org)
