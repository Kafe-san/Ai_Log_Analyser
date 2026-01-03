AI Log Analyzer (GenAI Engineer Project)
📌 Overview

The AI Log Analyzer is a lightweight, cloud-deployed GenAI tool that analyzes system or application logs and provides advisory diagnostics. Using a large language model, the application identifies errors, probable root causes, suggested fixes, severity levels, and reliability risks from semi-structured log data.

This project was developed as an individual GenAI Engineer assignment, with a focus on technical feasibility, robustness, and responsible AI integration, rather than UI complexity.

🎯 Purpose & Scope

Modern system logs vary widely in structure and format, making rule-based analysis brittle and hard to maintain. This project explores how Generative AI can assist engineers by interpreting logs flexibly while remaining advisory and safe.

In scope:

Log analysis and interpretation

Structured diagnostic output

Cloud deployment using a free GenAI API

Out of scope:

Automatic remediation or system changes

Persistent data storage

Authentication or user management

⚙️ Technical Design
Architecture
User Input (Logs)
        ↓
 Prompt + Schema Enforcement
        ↓
   Gemini LLM (Free Tier)
        ↓
 Output Sanitization & Validation
        ↓
 Structured JSON Result

Technology Stack

Python 3.10

Streamlit Community Cloud

Google Gemini (google-genai SDK)

JSON-based structured output

🧠 Engineering Decisions
Why GenAI?

System logs are semi-structured and context-dependent. A generative model can interpret patterns and anomalies that are difficult to capture with static parsing rules.

Why Structured JSON Output?

Enables deterministic downstream handling

Reduces hallucination risk

Improves robustness and integration potential

Output Validation

LLM output is not assumed to be reliable by default. The application:

Sanitizes Markdown formatting (e.g. ```json fences)

Extracts and validates JSON defensively

Fails gracefully when output is malformed

Model Choice

The Gemini model was selected due to:

Free-tier availability

SDK compatibility

Sufficient performance for diagnostic tasks

🔐 Security, Privacy & Ethics

No logs are stored or persisted

API keys are managed via Streamlit Secrets

Users are advised not to submit sensitive data

Output is advisory only and requires human judgment

This ensures responsible and ethical use of GenAI in an engineering context.

📊 Reliability & Control

Graceful error handling prevents application crashes

Raw model output is exposed for debugging when parsing fails

The system degrades safely instead of producing invalid results

These measures demonstrate awareness of GenAI reliability risks.

🌱 Professional Practice

This project reflects:

Iterative development and troubleshooting

Applied research into SDK compatibility and model availability

Conscious scope limitation to ensure quality and clarity

Sustainable software choices (minimal infrastructure, free services)

🚀 How to Run (Cloud)

The application is deployed on Streamlit Community Cloud.

Required Files
app.py
requirements.txt
runtime.txt

Secrets (Streamlit Cloud)
GEMINI_API_KEY = "your-api-key-here"

📌 Disclaimer

⚠️ This tool provides advisory analysis only.
It must not be used as an automated decision-making or remediation system.

👤 Author
 <Marian Metin Constantin>