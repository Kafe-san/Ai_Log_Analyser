import streamlit as st
import json
from google import genai
import re

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
# Removes Markdown code
# -------------------------------

def extract_json(text: str) -> str:
    """
    Extracts a JSON object from LLM output, even if wrapped in Markdown fences.
    """
    # Remove markdown code fences (```json or ```)
    text = re.sub(r"```(?:json)?", "", text, flags=re.IGNORECASE)
    text = text.replace("```", "")

    # Extract JSON object
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        raise ValueError("No JSON object found")

    return match.group(0)
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

            raw_output = response.text

            try:
                clean_json = extract_json(raw_output)
                result = json.loads(clean_json)

                st.subheader("🧾 Analysis Result")
                st.json(result)
            except Exception:
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
