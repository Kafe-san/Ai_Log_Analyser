import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="AI Log Analyzer", layout="centered")
st.title("🔍 AI Log Analyzer")

# Initialize OpenAI client using Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.write("This step verifies OpenAI connectivity.")

if st.button("Test OpenAI connection"):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a test assistant."},
                {"role": "user", "content": "Say 'connection successful'."}
            ],
            temperature=0
        )

        st.success(response.choices[0].message.content)

    except Exception as e:
        st.error("OpenAI call failed")
        st.exception(e)
