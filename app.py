import streamlit as st
import numpy as np
import cv2
from forensics_engine import extract_spectral_fingerprint

# Page Configuration
st.set_page_config(
    page_title="VTX | Deepfake Forensic Suite",
    page_icon="🛡️",
    layout="wide"
)

# Custom CSS for a "Cyber" look
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stMetric { background-color: #161b22; padding: 15px; border-radius: 10px; border: 1px solid #30363d; }
    </style>
    """, unsafe_allow_html=True)

# Sidebar for Hackathon Branding
with st.sidebar:
    st.title("🛡️ VTX Engine v1.0")
    st.subheader("Cybersecurity Track")
    st.info("Target: Frequency Domain Artifacts (FFT)")
    st.divider()
    st.write("**Developed for:** Jain University Hackathon")
    if st.button("Clear Cache"):
        st.rerun()

# Main Header
st.title("🔍 Deepfake Fingerprint Forensic Tool")
st.write("Upload an image to analyze invisible mathematical traces left by AI generators.")

uploaded_file = st.file_uploader("Choose an image file (JPG, PNG)...", type=["jpg", "png", "jpeg"])

if uploaded_file:
    file_bytes = uploaded_file.read()
    
    # Create Layout
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Original Evidence")
        st.image(file_bytes, use_container_width=True)

    with col2:
        st.subheader("Frequency Artifact Map")
        try:
            # Process the image
            noise_map, spectrum = extract_spectral_fingerprint(file_bytes)
            
            # SAFE NORMALIZATION: Prevents the division by zero error
            max_val = np.max(spectrum)
            if max_val > 0:
                # Scale spectrum to 0-1 for display
                display_spectrum = spectrum / max_val
                st.image(display_spectrum, use_container_width=True, clamp=True)
                st.caption("Dots or grid patterns here indicate AI-generated upsampling signatures.")
            else:
                st.error("Error: Could not extract frequency data. The image may be too small or corrupted.")
        
        except Exception as e:
            st.error(f"Analysis Failed: {str(e)}")

    # Analysis Results Section
    st.divider()
    res_col1, res_col2, res_col3 = st.columns(3)

    # Simple logic for demo purposes:
