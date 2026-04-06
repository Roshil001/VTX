import streamlit as st
from forensics_engine import extract_spectral_fingerprint

st.set_page_config(page_title="DeepForensic Lab", layout="wide")

st.title("🛡️ Deepfake Fingerprint Forensic Suite")
st.markdown("Analyzing invisible frequency artifacts in synthetic media.")

uploaded_file = st.file_uploader("Upload an Image...", type=["jpg", "png", "jpeg"])

if uploaded_file:
    file_bytes = uploaded_file.read()
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Original Evidence")
        st.image(file_bytes, use_container_width=True)

    with col2:
        st.subheader("Frequency Artifact Map")
        noise_map, spectrum = extract_spectral_fingerprint(file_bytes)
        # Normalize for display
        st.image(spectrum / np.max(spectrum), use_container_width=True)
        st.caption("Look for repeating 'star' patterns or grids—those are AI fingerprints.")

    # Simple Analysis Logic
    st.divider()
    if np.mean(noise_map) > 10: # Sample threshold for demo
        st.error("🚨 HIGH ANOMALY DETECTED: Mathematical fingerprints found.")
    else:
        st.success("✅ AUTHENTIC: Natural sensor noise detected.")
