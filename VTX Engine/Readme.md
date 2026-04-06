# VTX: Multimodal Forensic Identity Suite

**VTX** is a high-performance cybersecurity suite designed to combat the $12B+ global threat of AI-driven fraud and Business Email Compromise (BEC). By unifying local mathematical forensics with cloud-based linguistic intelligence, VTX provides a "Zero-Trust" architecture that verifies both the **visual identity** and **linguistic intent** of digital communications.

---

## 🚀 Key Features

* **Spectral Artifact Mapping (SAM):** Executes **Fast Fourier Transforms (FFT)** locally to expose high-frequency "checkerboard" artifacts—the invisible mathematical fingerprints left by GANs and Diffusion models.
* **Linguistic DNA Analysis:** Leverages the **Gemini 3 Flash API** to detect social engineering patterns (urgency bias, financial coercion) that bypass traditional malware filters.
* **Domain Integrity Shield:** Real-time metadata cross-referencing to flag "Typosquatting" and display-name spoofing.
* **Unified Forensic Dashboard:** A single-pane-of-glass interface built on **Streamlit** for non-technical corporate staff to receive explainable security verdicts.

---

## 🏗️ System Architecture

VTX follows a **Modular Multimodal Pipeline** to balance speed with forensic depth:

1.  **Frontend (Streamlit):** Handles evidence ingestion and real-time risk visualization.
2.  **Forensic Engine (Local):** Uses **OpenCV** and **NumPy** for deterministic mathematical analysis (FFT), ensuring data privacy and indisputable proof.
3.  **Intelligence Layer (Cloud):** Powered by **Gemini 3 Flash** for agentic reasoning, intent classification, and metadata validation.

---

## 🛠️ Tech Stack

| Layer | Technology | Function |
| :--- | :--- | :--- |
| **Interface** | Streamlit | Zero-Trust UI & Dashboarding |
| **Forensics** | OpenCV & NumPy | Local FFT Spectral Analysis |
| **Intelligence** | Gemini 3 Flash | Linguistic & Behavioral Analysis |
| **Language** | Python 3.11+ | System Orchestration |
| **Deployment** | Streamlit Cloud | Live Demo Accessibility |

---

## 🚦 Getting Started

### Prerequisites
* Python 3.11+
* Gemini API Key (via [Google AI Studio](https://aistudio.google.com/))

### Installation
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/vtx-forensics.git](https://github.com/your-username/vtx-forensics.git)
    cd vtx-forensics
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Set up environment variables:**
    Create a `.env` file or use Streamlit Secrets:
    ```env
    GEMINI_API_KEY=your_api_key_here
    ```
4.  **Run the application:**
    ```bash
    streamlit run app.py
    ```

---

## 🔮 Future Scope
* **Real-Time Video Forensics:** Temporal analysis for live deepfake stream detection.
* **Voice Clone Detection:** Spectral audio analysis to identify synthetic vocal signatures.
* **Blockchain Provenance:** Immutable logging of forensic checks via decentralized ledgers.
* **Compliance Integration:** Automated reporting for the **EU AI Act** and ISO forensic standards.

---

## 👥 The Team
* **Adith P Nair** Forensic Engineer (OpenCV / Gemini API)
* **Devang Santhosh** Integration Lead (Streamlit / Python)
* **Roshil Ranjith** Product Strategist (Market Analysis / XAI Design)

---
> **"Local math for proof, Cloud AI for context."**
