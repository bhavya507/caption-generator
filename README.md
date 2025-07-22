# 🚀 Social Media Caption Generator

An AI-powered Streamlit app that generates catchy, emoji-rich, and platform-ready captions for social media. Designed to assist creators, marketers, and brands in crafting quick and engaging content.

---

## 🎯 Features

- ✅ Generate **5 unique captions** per keyword
- 🎭 Select **Tone** (funny, formal, sarcastic, etc.)
- 💭 Choose a **Mood** to influence language style
- 🧵 Add your own **Custom Hashtags**
- 🤖 **GPT-2 Toggle** for smarter AI-powered generation
- 📱 Platform targeting: Instagram, LinkedIn, Twitter
- 📋 **Copy to clipboard** or download captions as `.txt`
- 🎨 Emoji support and hashtag formatting included

---

## 🖥️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python + Hugging Face Transformers (GPT-2)
- **Libraries**: `transformers`, `streamlit`, `torch`, `pandas`, `emoji`, `re`

---

## ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/bhavya507/caption-generator.git
cd caption-generator

# (Optional) Create a virtual environment
python -m venv venv
venv\Scripts\activate   # On Windows
# OR
source venv/bin/activate  # On macOS/Linux

# Install required packages
pip install -r requirements.txt

# Run the app
streamlit run caption_app.py
