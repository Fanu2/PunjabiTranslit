import streamlit as st
import pandas as pd
from gtts import gTTS
from io import BytesIO

# Example transliteration mappings (basic)
gurmukhi_to_shahmukhi_map = {
    "ਅ": "ا", "ਆ": "آ", "ਇ": "اِ", "ਈ": "ای", "ਉ": "اُ",
    "ਏ": "ے", "ਐ": "ای", "ਓ": "و", "ਔ": "اؤ",
    "ਕ": "ک", "ਖ": "خ", "ਗ": "گ", "ਘ": "غ", "ਚ": "چ",
    "ਜ": "ج", "ਝ": "جھ", "ਟ": "ٹ", "ਠ": "ٹھ", "ਡ": "ڈ",
    "ਢ": "ڈھ", "ਣ": "ڻ", "ਤ": "ت", "ਥ": "تھ", "ਦ": "د",
    "ਧ": "دھ", "ਨ": "ن", "ਪ": "پ", "ਫ": "ف", "ਬ": "ب",
    "ਭ": "بھ", "ਮ": "م", "ਯ": "ی", "ਰ": "ر", "ਲ": "ل",
    "ਵ": "و", "ਸ": "س", "ਹ": "ھ", "ਾ": "ا", "ਿ": "ِ", "ੀ": "ی",
    "ੁ": "ُ", "ੂ": "و", "ੇ": "ے", "ੈ": "ے", "ੋ": "و", "ੌ": "اؤ"
}

def transliterate(text, mapping):
    result = ""
    for char in text:
        result += mapping.get(char, char)
    return result

st.set_page_config(page_title="Punjabi Language Tools", layout="wide")

st.title("Punjabi Language Tools 🖋️")
st.markdown("Tools for **Gurmukhi** and **Shahmukhi** scripts with transliteration, spell-check, TTS, and word analysis.")

tab1, tab2, tab3 = st.tabs(["Gurmukhi Tools", "Shahmukhi Tools", "Combined Tools"])

# ------------------------------
# Tab 1: Gurmukhi Tools
# ------------------------------
with tab1:
    st.header("Gurmukhi → Shahmukhi Transliteration")
    gurmukhi_input = st.text_area("Enter Gurmukhi text:")
    
    if st.button("Transliterate G→S"):
        shahmukhi_output = transliterate(gurmukhi_input, gurmukhi_to_shahmukhi_map)
        st.text_area("Shahmukhi Output:", value=shahmukhi_output, height=150)

    st.header("Text-to-Speech (Gurmukhi)")
    if st.button("Read Aloud Gurmukhi"):
        if gurmukhi_input.strip() != "":
            tts = gTTS(text=gurmukhi_input, lang='pa')
            audio_bytes = BytesIO()
            tts.write_to_fp(audio_bytes)
            audio_bytes.seek(0)
            st.audio(audio_bytes, format="audio/mp3")
        else:
            st.warning("Please enter Gurmukhi text first!")

# ------------------------------
# Tab 2: Shahmukhi Tools
# ------------------------------
with tab2:
    st.header("Shahmukhi → Gurmukhi Transliteration")
    shahmukhi_input = st.text_area("Enter Shahmukhi text:")

    # Reverse mapping
    shahmukhi_to_gurmukhi_map = {v: k for k, v in gurmukhi_to_shahmukhi_map.items()}

    if st.button("Transliterate S→G"):
        gurmukhi_output = transliterate(shahmukhi_input, shahmukhi_to_gurmukhi_map)
        st.text_area("Gurmukhi Output:", value=gurmukhi_output, height=150)

    st.header("Text-to-Speech (Shahmukhi)")
    if st.button("Read Aloud Shahmukhi"):
        if shahmukhi_input.strip() != "":
            tts = gTTS(text=shahmukhi_input, lang='pa')
            audio_bytes = BytesIO()
            tts.write_to_fp(audio_bytes)
            audio_bytes.seek(0)
            st.audio(audio_bytes, format="audio/mp3")
        else:
            st.warning("Please enter Shahmukhi text first!")

# ------------------------------
# Tab 3: Combined Tools
# ------------------------------
with tab3:
    st.header("Word Frequency Analysis")
    combined_text = st.text_area("Enter text (Gurmukhi/Shahmukhi):")
    if st.button("Analyze Words"):
        words = combined_text.split()
        freq = pd.Series(words).value_counts()
        st.table(freq)

    st.header("Upload Text File")
    uploaded_file = st.file_uploader("Upload .txt file", type="txt")
    if uploaded_file:
        file_text = uploaded_file.read().decode("utf-8")
        st.text_area("File Content:", value=file_text, height=200)
