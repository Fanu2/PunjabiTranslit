import streamlit as st

st.set_page_config(page_title="Punjabi Transliteration Tools", layout="wide")

st.title("Punjabi Transliteration Tools")
st.markdown("""
This app allows working with **Gurmukhi** and **Shahmukhi** scripts.
Use the text boxes below to input text and see transliterations.
""")

# Input text areas
gurmukhi_text = st.text_area("Gurmukhi Input", "", height=150)
shahmukhi_text = st.text_area("Shahmukhi Input", "", height=150)

# Dummy processing (replace with your transliteration functions)
if st.button("Transliterate Gurmukhi → Shahmukhi"):
    st.success(f"Shahmukhi Output (simulated): {gurmukhi_text[::-1]}")

if st.button("Transliterate Shahmukhi → Gurmukhi"):
    st.success(f"Gurmukhi Output (simulated): {shahmukhi_text[::-1]}")

st.markdown("---")
st.info("This is a starter template. Add your real Punjabi language tools in place of dummy logic.")
