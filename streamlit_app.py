import streamlit as st

st.set_page_config(page_title="AI Log Analyzer", layout="centered")

st.title("🔍 AI Log Analyzer")
st.write("Paste logs below. This is a placeholder app to verify deployment.")

log_input = st.text_area("Log input", height=250)

if st.button("Analyze"):
    st.write("Analysis will appear here.")
