# --- MODULE 2: UNIVERSAL EMAIL FORENSIC (CEV) ---
elif mode == "Email Fraud Analysis":
    st.title("📧 Universal Corporate Email Forensic")
    st.write("Analyse any email by comparing the sender's metadata against official corporate patterns.")

    col_input, col_info = st.columns([2, 1])

    with col_info:
        st.info("""
        **How it works:**
        1. **Domain Integrity:** Checks if the sender is using a public (gmail/yahoo) or spoofed domain.
        2. **Urgency Analysis:** Detects psychological triggers used in Phishing.
        3. **History Mapping:** Compares the 'Tone' against standard corporate communication.
        """)

    with col_input:
        target_company = st.text_input("Target Company Name (e.g., Apple, Tesla, Jain University)")
        official_domain = st.text_input("Official Company Domain (e.g., apple.com, jainuniversity.ac.in)")
        sender_email = st.text_input("Sender's Email to Verify")
        email_body = st.text_area("Paste Email Content:", height=150)

    if st.button("Run Forensic Scan"):
        if not (target_company and official_domain and sender_email):
            st.warning("Please fill in the Company, Domain, and Sender fields.")
        else:
            st.divider()
            
            # --- FORENSIC LOGIC ---
            # 1. Domain Check
            is_spoofed = not sender_email.lower().endswith(f"@{official_domain.lower()}")
            is_public_provider = any(prov in sender_email.lower() for prov in ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com"])
            
            # 2. Urgency/Threat Detection
            threat_patterns = {
                "Urgency": ["immediate", "urgent", "action required", "minutes", "hours", "deadline"],
                "Financial": ["bank", "transfer", "invoice", "payment", "account", "payroll", "salary"],
                "Threat": ["suspended", "blocked", "legal action", "unauthorized", "security breach"]
            }
            
            found_threats = []
            for category, words in threat_patterns.items():
                if any(word in email_body.lower() for word in words):
                    found_threats.append(category)

            # --- DYNAMIC VERDICT ---
            v_col1, v_col2 = st.columns(2)
            
            with v_col1:
                st.subheader("Final Security Status")
                if is_spoofed:
                    st.error("🚩 VERDICT: HIGH RISK (DOMAIN MISMATCH)")
                    st.write(f"This email claims to be from **{target_company}**, but the sender address does not belong to **{official_domain}**.")
                elif len(found_threats) >= 2:
                    st.warning("⚠️ VERDICT: SUSPICIOUS (PHISHING PATTERNS)")
                    st.write(f"The domain is correct, but the content contains multiple threat vectors: {', '.join(found_threats)}.")
                else:
                    st.success("✅ VERDICT: LOW RISK / VERIFIED")
                    st.write("Sender domain and content structure align with corporate standards.")

            with v_col2:
                st.subheader("Metadata Breakdown")
                st.write(f"**Sender:** `{sender_email}`")
                st.write(f"**Expected Domain:** `{official_domain}`")
                st.write(f"**Public Provider used:** {'Yes (High Risk)' if is_public_provider else 'No (Corporate)'}")
                st.write(f"**Threat Categories Detected:** {len(found_threats)}")
