import streamlit as st
import numpy as np
import re
from forensics_engine import extract_spectral_fingerprint, analyze_image

# --- PAGE SETUP ---
st.set_page_config(page_title="VTX Cyber-Suite", page_icon="🛡️", layout="wide")

# --- MOCK COMPANY HISTORY DATA ---
# In a real app, this would be a database/API call
COMPANY_DB = {
    "Google": {"domain": "google.com", "tone": "Professional", "last_contact": "2 days ago"},
    "Microsoft": {"domain": "microsoft.com", "tone": "Technical", "last_contact": "1 week ago"},
    "Jain University": {"domain": "jainuniversity.ac.in", "tone": "Academic", "last_contact": "5 hours ago"}
}

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("🛡️ VTX Cyber-Suite")
    mode = st.radio("Select Security Module:", ["Deepfake Detector", "Email Fraud Analysis"])
    st.divider()
    st.caption("Developed for Jain University Hackathon 2026")

# --- MODULE 1: DEEPFAKE DETECTOR ---
if mode == "Deepfake Detector":
    st.title("🔍 Deepfake Fingerprint Forensic")
    uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

    if uploaded_file:
        file_bytes = uploaded_file.read()
        col1, col2 = st.columns(2)
        with col1:
            st.image(file_bytes, caption="Evidence", use_container_width=True)
        with col2:
            noise, spectrum = extract_spectral_fingerprint(file_bytes)
            max_val = np.max(spectrum)
            st.image(spectrum / (max_val if max_val > 0 else 1), caption="FFT Spectrum", use_container_width=True)
        
        # Final Verdict Logic
        prob = analyze_image(file_bytes)
        st.divider()
        if prob > 70:
            st.error(f"### Verdict: DEEPFAKE ({prob:.1f}%)")
        else:
            st.success(f"### Verdict: AUTHENTIC ({100-prob:.1f}%)")

# --- MODULE 2: EMAIL FRAUD ANALYSIS ---
elif mode == "Email Fraud Analysis":
    st.title("📧 Corporate Email Forensic (CEV)")
    st.write("Analyse emails against corporate history to detect spoofing and phishing.")

    col_input, col_hist = st.columns([2, 1])

    with col_hist:
        st.subheader("📜 Known Company History")
        st.json(COMPANY_DB)

    with col_input:
        company_name = st.selectbox("Select Company to Validate Against:", list(COMPANY_DB.keys()))
        sender_email = st.text_input("Sender Email Address (e.g., hr@google.com)")
        email_body = st.text_area("Paste Email Content Here:", height=200)

    if st.button("Analyse Email Security"):
        if sender_email and email_body:
            # 1. Domain Check
            expected_domain = COMPANY_DB[company_name]["domain"]
            is_domain_valid = sender_email.endswith(f"@{expected_domain}")

            # 2. Urgency/Fraud Detection (NLP Lite)
            fraud_keywords = ["urgent", "immediately", "bank details", "suspended", "password", "transfer"]
            detected_keywords = [word for word in fraud_keywords if word in email_body.lower()]
            
            # 3. Final Scoring
            st.divider()
            if not is_domain_valid:
                st.error("🚩 CRITICAL: DOMAIN SPOOFING DETECTED")
                st.write(f"The sender's domain does not match {company_name}'s official record.")
            elif len(detected_keywords) > 2:
                st.warning("⚠️ SUSPICIOUS: HIGH-URGENCY PHISHING PATTERNS")
                st.write(f"Detected suspicious keywords: {', '.join(detected_keywords)}")
            else:
                st.success("✅ VERIFIED: EMAIL MATCHES CORPORATE PROFILE")
        else:
            st.info("Please enter sender email and body text.")
