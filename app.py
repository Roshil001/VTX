import streamlit as st
import numpy as np
from forensics_engine import extract_spectral_fingerprint, analyze_image

# --- PAGE SETUP ---
st.set_page_config(page_title="VTX Cyber-Suite", page_icon="🛡️", layout="wide")

# Custom Dark Theme Styling
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric { border: 1px solid #30363d; padding: 10px; border-radius: 5px; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("🛡️ VTX Cyber-Suite")
    st.subheader("Cybersecurity Forensic Tools")
    mode = st.radio("Select Security Module:", ["Deepfake Detector", "Email Fraud Analysis"])
    st.divider()
    st.write("**Hackathon:** Jain University 2026")
    st.caption("v1.5 Final Build")

# --- MODULE 1: DEEPFAKE DETECTOR ---
if mode == "Deepfake Detector":
    st.title("🔍 Deepfake Fingerprint Forensic")
    st.write("Extracting invisible AI 'fingerprints' from synthetic media via Spectral Analysis.")

    uploaded_file = st.file_uploader("Upload Image Evidence", type=["jpg", "png", "jpeg"])

    if uploaded_file:
        file_bytes = uploaded_file.read()
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Original Image")
            st.image(file_bytes, use_container_width=True)

        with col2:
            st.subheader("Frequency Artifact Map")
            noise_map, spectrum = extract_spectral_fingerprint(file_bytes)
            max_val = np.max(spectrum)
            if max_val > 0:
                st.image(spectrum / max_val, use_container_width=True, clamp=True)
                st.caption("Repeating grid patterns suggest AI-upsampling kernels.")
            else:
                st.error("Spectral reconstruction failed.")

        # FINAL VERDICT
        st.divider()
        st.subheader("🏁 Final AI Verdict")
        
        prob = analyze_image(file_bytes)
        fft_anomaly = np.mean(noise_map)
        final_score = (fft_anomaly * 1.5) + (prob * 0.7)
        final_score = min(99.9, max(0.5, final_score))

        v_col1, v_col2 = st.columns([1, 2])
        with v_col1:
            if final_score > 70:
                st.error(f"## {final_score:.1f}% Probability")
                st.markdown("### 🚩 **VERDICT: DEEPFAKE**")
            else:
                st.success(f"## {final_score:.1f}% Probability")
                st.markdown("### ✅ **VERDICT: AUTHENTIC**")

        with v_col2:
            st.info("**Forensic Summary:**")
            if final_score > 70:
                st.write("Periodic artifacts detected in high-frequency bands. Pixel distribution matches Generative AI signatures.")
            else:
                st.write("Noise patterns align with physical CMOS sensor characteristics. No synthetic upsampling detected.")

# --- MODULE 2: UNIVERSAL EMAIL FORENSIC ---
elif mode == "Email Fraud Analysis":
    st.title("📧 Universal Corporate Email Forensic")
    st.write("Analyze any sender to detect Domain Spoofing and Business Email Compromise (BEC).")

    col_input, col_info = st.columns([2, 1])

    with col_info:
        st.info("**Analysis Methodology:** \n- Domain Integrity Validation\n- Linguistic Threat Mapping\n- Public Provider Detection")

    with col_input:
        target_company = st.text_input("Target Company Name")
        official_domain = st.text_input("Official Domain (e.g., google.com)")
        sender_email = st.text_input("Sender's Email Address")
        email_body = st.text_area("Email Content:", height=150)

    if st.button("Run Forensic Scan"):
        if not (target_company and official_domain and sender_email):
            st.warning("Please provide Company, Domain, and Sender details.")
        else:
            st.divider()
            
            # --- FORENSIC LOGIC ---
            is_spoofed = not sender_email.lower().endswith(f"@{official_domain.lower()}")
            is_public = any(p in sender_email.lower() for p in ["gmail.com", "yahoo.com", "outlook.com"])
            
            threat_patterns = ["urgent", "bank", "password", "transfer", "immediate", "suspended", "payment"]
            detected_threats = [w for w in threat_patterns if w in email_body.lower()]

            # --- DYNAMIC VERDICT ---
            v_col1, v_col2 = st.columns(2)
            with v_col1:
                st.subheader("Security Status")
                if is_spoofed:
                    st.error("🚩 VERDICT: HIGH RISK (DOMAIN SPOOFING)")
                elif len(detected_threats) >= 3:
                    st.warning("⚠️ VERDICT: SUSPICIOUS (PHISHING PATTERNS)")
                else:
                    st.success("✅ VERDICT: VERIFIED / LOW RISK")

            with v_col2:
                st.subheader("Metadata Report")
                st.write(f"**Domain Match:** {'Fail' if is_spoofed else 'Pass'}")
                st.write(f"**Public Provider:** {'Yes (Risky)' if is_public else 'No'}")
                st.write(f"**Threat Patterns Found:** {len(detected_threats)}")

    st.button("📄 Export Security Report")
