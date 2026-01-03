import streamlit as st
import json
from google import genai

st.set_page_config(page_title="AI Log Analyzer", layout="centered")
st.title("🔍 AI Log Analyzer")

# Initialize Gemini client (NEW SDK)
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

st.write("Paste system or application logs below.")

log_input = st.text_area("Log input", height=250)

PROMPT = """
You are an expert DevOps and Software Engineer.

Analyze the following logs and return ONLY valid JSON with:
- error_summary
- probable_root_causes (array)
- suggested_fixes (array)
- severity_level (Low, Medium, High, Critical)
- reliability_risks (array)
"""

if st.button("Analyze Logs") and log_input.strip():
    with st.spinner("Analyzing logs..."):
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash-lite",
                contents=PROMPT + "\n\nLOGS:\n" + log_input
            )

            result = json.loads(response.text)
            st.subheader("🧾 Analysis Result")
            st.json(result)

        except Exception as e:
            st.error("Analysis failed.")
            st.exception(e)
