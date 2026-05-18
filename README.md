# Quantum Ethnobotany & Pharma Recommendation System

**A hybrid classical/quantum ML database that tells you what natural and pharmaceutical drugs can fight a specific disease.**

Built as part of Stanford CS229 (Machine Learning) by **Dr. Elden Wayne Whalen III, ShD**.

---

### ✨ Key Features

- **Multi-Source Intelligence**: Integrates Dr. Duke’s Phytochemical Database, COCONUT, DrugBank, ChEMBL, PubChem, and other ethnobotanical repositories.
- **Hybrid ML Architecture**:
  - Supervised models for ranking and modality prediction
  - Unsupervised embeddings and clustering for novel discovery
  - Reinforcement Learning module (in development) for hybrid analog optimization
- **Live Quantum Enhancement**: Powered by a custom **Variational Quantum Algorithm (VQA)** oracle via HTTP.
- **Rich Recommendations**: Natural products + synthetic drugs with predicted modalities, mechanisms, evidence levels, toxicity flags, and quantum-enhanced confidence scores.
- **Interactive Demo**: Streamlit/Gradio web interface for instant queries.

### Why This Matters

Natural products continue to inspire a massive portion of modern pharmaceuticals. This project bridges traditional ethnobotanical knowledge with cutting-edge AI and quantum computing to accelerate hypothesis generation in drug discovery, repurposing, and global health research.

**Important**: This is a **research tool only**. All outputs are computational predictions and **not medical advice**.

---

### Tech Stack

- **Backend**: FastAPI + Python
- **Classical ML**: XGBoost, PyTorch, scikit-learn, RDKit
- **Quantum**: Custom VQA Oracle ([Grok-Wayne Quantum Algorithm](https://github.com/wayneeffect/Grok-Wayne-s-Quantum-Algorithm))
- **Data**: PostgreSQL + pgvector, Neo4j (Knowledge Graph), Redis
- **Frontend**: Streamlit / Gradio
- **Deployment**: Docker, Render

---

### Quick Start

```bash
git clone https://github.com/wayneeffect/quantum-ethnobotany-pharma.git
cd quantum-ethnobotany-pharma
pip install -r requirements.txt
cp .env.example .env
streamlit run app.py
