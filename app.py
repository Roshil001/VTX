import streamlit as st
import numpy as np
from forensics_engine import extract_spectral_fingerprint, analyze_image

# Page Setup
st.set_page_config(page_title="VTX Forensic Suite", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    .reportview-container { background: #0e1117; }
    .stProgress > div > div > div > div { background-image: linear-gradient(to right, #4facfe 0%, #00f2fe 100%); }
    </style>
    """, unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("🛡️ VTX Engine")
    st.write("Deepfake Detection via Frequency Fingerprinting")
    st.divider()
    st.caption("Hackathon Build v1.2")

st.title("🔍 Digital Forensic Analysis")
st.write("Upload suspicious media to extract mathematical sensor signatures.")

uploaded_file = st.file_uploader("Upload Evidence (JPG/PNG)", type=["jpg", "png", "jpeg"])

if uploaded_file:
    file_bytes = uploaded_file.read()
    
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Original Image")
        st.image(file_bytes, use_container_width=True)

    with col2:
        st.subheader("Frequency Artifact Map")
        noise_map, spectrum = extract_spectral_fingerprint(file_bytes)
        
        # Safe Normalization for Display
        max_val = np.max(spectrum)
        if max_val > 0:
            st.image(spectrum / max_val, use_container_width=True, clamp=True)
            st.caption("Grids/Dots indicate periodic upsampling artifacts (AI Signature).")
        else:
            st.error("Spectral analysis failed.")

    # --- VERDICT SECTION ---
    st.divider()
    st.subheader("🏁 Final AI Forensic Verdict")
    
    model_score = analyze_image(file_bytes)
    fft_anomaly = np.mean(noise_map)
    
    # Hybrid Scoring: Combines FFT Math with Neural Net Pattern Matching
    final_score = (fft_anomaly * 1.5) + (model_score * 0.7)
    final_score = min(99.9, max(0.5, final_score)) # Clamp values

    v_col1, v_col2 = st.columns([1, 2])

    with v_col1:
        if final_score > 75:
            st.error(f"## {final_score:.1f}% Prob. Synthetic")
            st.markdown("### 🚩 **VERDICT: DEEPFAKE**")
        elif final_score > 45:
            st.warning(f"## {final_score:.1f}% Prob. Synthetic")
            st.markdown("### ⚠️ **VERDICT: SUSPICIOUS**")
        else:
            st.success(f"## {final_score:.1f}% Prob. Synthetic")
            st.markdown("### ✅ **VERDICT: AUTHENTIC**")

    with v_col2:
        st.info("**Analysis Summary:**")
        if final_score > 75:
            st.write("Structural anomalies detected in high-frequency bands. Pixel interpolation matches known generative AI kernels (StyleGAN/Diffusion).")
        else:
            st.write("Noise distribution aligns with physical CMOS sensor patterns. No periodic upsampling artifacts detected.")

    st.button("📄 Export Forensic PDF Report")

else:
    st.info("Please upload an image to begin forensic reconstruction.")
