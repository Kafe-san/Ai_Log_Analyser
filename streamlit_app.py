import streamlit as st
import google.generativeai as genai
import json

st.set_page_config(page_title="AI Log Analyzer", layout="centered")
st.title("🔍 AI Log Analyzer")

# Configure Gemini
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

st.write("Paste system or application logs below.")

log_input = st.text_area("Log input", height=250)

SYSTEM_PROMPT = """
You are an expert DevOps and Software Engineer.
Analyze the provided logs and return a structured JSON response with:
- error_summary
- probable_root_causes (list)
- suggested_fixes (list)
- severity_level (Low, Medium, High, Critical)
- reliability_risks (list)

Respond ONLY with valid JSON.
"""

if st.button("Analyze Logs") and log_input.strip():
    with st.spinner("Analyzing logs..."):
        try:
            response = model.generate_content(
                SYSTEM_PROMPT + "\n\nLOGS:\n" + log_input
            )

            result = json.loads(response.text)
            st.subheader("🧾 Analysis Result")
            st.json(result)

        except Exception as e:
            st.error("Analysis failed.")
            st.exception(e)
