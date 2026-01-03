import streamlit as st
import json
from openai import OpenAI

# Initialize client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="AI Log Analyzer", layout="centered")
st.title("🔍 AI Log Analyzer")

st.write("Paste your system or application logs below. The AI will analyze errors, causes, and fixes.")

log_input = st.text_area("Log input", height=250)

analyze = st.button("Analyze Logs")

SYSTEM_PROMPT = """
You are an expert DevOps and Software Engineer.
Analyze the provided logs and return a structured JSON response with:
- error_summary
- probable_root_causes (list)
- suggested_fixes (list)
- severity_level (Low, Medium, High, Critical)
- reliability_risks (list)

Respond ONLY in valid JSON.
"""

if analyze and log_input.strip():
    with st.spinner("Analyzing logs..."):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": log_input}
            ],
            temperature=0.2
        )

        try:
            result = json.loads(response.choices[0].message.content)
            st.subheader("🧾 Analysis Result")
            st.json(result)
        except json.JSONDecodeError:
            st.error("Model returned invalid JSON. Try again.")
