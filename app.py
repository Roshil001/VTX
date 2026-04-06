import streamlit as st
import numpy as np
import google.generativeai as genai
from forensics_engine import extract_spectral_fingerprint

# --- API CONFIGURATION ---
# It's safer to use st.secrets["GEMINI_KEY"] on GitHub
GEMINI_KEY = st.secrets.get("GEMINI_KEY", "AIzaSyDFLh_sZSfyHijTczwR78NvkXvQhJRCJG4")
genai.configure(api_key=GEMINI_KEY)

# --- PAGE SETUP ---
st.set_page_config(page_title="VTX Cyber-Suite", page_icon="🛡️", layout="wide")

# --- SIDEBAR ---
with st.sidebar:
    st.title("🛡️ VTX Engine")
    mode = st.radio("Switch Module:", ["Deepfake Detector", "Email Fraud Analysis"])
    st.divider()
    st.caption("Hackathon Build v2.0")

# --- MODULE 1: DEEPFAKE (MATH-BASED) ---
if mode == "Deepfake Detector":
    st.title("🔍 Spectral Forensic Lab")
    uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

    if uploaded_file:
        file_bytes = uploaded_file.read()
        col1, col2 = st.columns(2)
        
        with col1:
            st.image(file_bytes, caption="Original Evidence", use_container_width=True)
        
        with col2:
            noise_map, spectrum = extract_spectral_fingerprint(file_bytes)
            max_val = np.max(spectrum)
            st.image(spectrum / (max_val if max_val > 0 else 1), caption="FFT Spectrum", use_container_width=True)
        
        # Simple local heuristic for verdict
        anomaly_score = np.mean(noise_map)
        st.divider()
        if anomaly_score > 12:
            st.error(f"### Verdict: DEEPFAKE DETECTED (Score: {anomaly_score:.2f})")
        else:
            st.success(f"### Verdict: AUTHENTIC (Score: {anomaly_score:.2f})")

# --- MODULE 2: EMAIL FRAUD (GEMINI API) ---
elif mode == "Email Fraud Analysis":
    st.title("📧 Gemini AI Email Guard")
    st.write("Using LLM context-awareness to detect Phishing and Social Engineering.")

    target_company = st.text_input("Target Company Name")
    official_domain = st.text_input("Official Domain (e.g., microsoft.com)")
    sender_email = st.text_input("Sender's Email Address")
    email_body = st.text_area("Paste Email Content:", height=200)

    if st.button("Analyze with Gemini AI"):
        if not (sender_email and email_body):
            st.warning("Please provide the sender email and content.")
        else:
            with st.spinner("Gemini is analyzing intent and metadata..."):
                # Constructing a high-quality prompt for the AI
                prompt = f"""
                You are a Cybersecurity Forensic Expert. Analyze this email for fraud:
                Target Company: {target_company}
                Official Domain: {official_domain}
                Sender Email: {sender_email}
                Email Content: {email_body}

                Provide:
                1. RISK LEVEL (Low, Medium, High, or Critical)
                2. SENSITIVE PATTERNS: (e.g., Domain Spoofing, Urgency Bias, Financial Coercion)
                3. VERDICT: A 2-sentence explanation of why it is or isn't fraud.
                """
                
                try:
                    model = genai.GenerativeModel('gemini-2.5-flash')
                    response = model.generate_content(prompt)
                    
                    st.divider()
                    st.subheader("🏁 Gemini Forensic Report")
                    st.markdown(response.text)
                    
                except Exception as e:
                    st.error(f"API Error: {str(e)}")
