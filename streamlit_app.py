import streamlit as st
import json
from google import genai

# -------------------------------
# Page configuration
# -------------------------------
st.set_page_config(
    page_title="AI Log Analyzer",
    layout="centered"
)

st.title("🔍 AI Log Analyzer")
st.write(
    "Paste system or application logs below. "
    "The AI provides advisory analysis only."
)

# -------------------------------
# Initialize Gemini client
# -------------------------------
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

# -------------------------------
# Input
# -------------------------------
log_input = st.text_area(
    "Log input",
    height=250,
    placeholder="Paste logs here..."
)

# -------------------------------
# Prompt (STRICT JSON)
# -------------------------------
PROMPT = """
You are an expert DevOps and Software Engineer.

Analyze the logs below and return ONLY valid JSON.
Do NOT include explanations, markdown, or extra text.

The JSON MUST match this schema exactly:

{
  "error_summary": "string",
  "probable_root_causes": ["string"],
  "suggested_fixes": ["string"],
  "severity_level": "Low | Medium | High | Critical",
  "reliability_risks": ["string"]
}
"""

# -------------------------------
# Action
# -------------------------------
if st.button("Analyze Logs") and log_input.strip():
    with st.spinner("Analyzing logs..."):
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash-lite",
                contents=PROMPT + "\n\nLOGS:\n" + log_input
            )

            raw_output = response.text.strip()

            try:
                result = json.loads(raw_output)

                st.subheader("🧾 Analysis Result")
                st.json(result)

            except json.JSONDecodeError:
                st.error("The model did not return valid JSON.")
                st.subheader("🔎 Raw Model Output")
                st.code(raw_output)

        except Exception as e:
            st.error("Analysis failed due to an unexpected error.")
            st.exception(e)

# -------------------------------
# Footer / Disclaimer
# -------------------------------
st.markdown("---")
st.caption(
    "⚠️ This tool provides advisory analysis only. "
    "No logs are stored. Do not submit sensitive data."
)
