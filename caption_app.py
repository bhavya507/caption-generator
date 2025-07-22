import streamlit as st
from generate_captions import generate_captions
import base64

st.set_page_config(page_title="AI Caption Generator", layout="centered")

st.title("🤖 Social Media Caption Generator")
st.write("Generate catchy, emoji-rich captions with tone, mood, and GPT-2 magic!")

# ------------------ User Inputs ------------------ #
with st.form("caption_form"):
    theme = st.text_input("📌 Enter theme or keyword", max_chars=40)
    tone = st.selectbox("🎭 Select Tone", ["funny", "formal", "sarcastic"])
    mood = st.selectbox("💫 Mood", ["happy", "chill", "energetic", "romantic", "funny"])
    platform = st.selectbox("📱 Platform", ["Instagram", "Twitter", "LinkedIn"])
    custom_tags = st.text_input("🔖 Add custom hashtags (comma-separated, optional)", placeholder="motivation, growth, ai")
    use_gpt2 = st.checkbox("🧠 Use GPT-2 for smarter generation?")
    submitted = st.form_submit_button("🚀 Generate Captions")

# ------------------ Generate Output ------------------ #
if submitted and theme:
    st.subheader("📝 Captions")
    captions = generate_captions(theme, tone, mood, platform, custom_tags, use_gpt2)
    
    for i, caption in enumerate(captions):
        st.code(caption, language="markdown")
        st.button(f"📋 Copy Caption {i+1}", on_click=st.session_state.update, args=(f'copied_{i}', True), key=f'copy_btn_{i}')

    # Download All Captions
    all_text = "\n\n".join(captions)
    b64 = base64.b64encode(all_text.encode()).decode()
    href = f'<a href="data:file/txt;base64,{b64}" download="captions.txt">📥 Download All Captions</a>'
    st.markdown(href, unsafe_allow_html=True)
