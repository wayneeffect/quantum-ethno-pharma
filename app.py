import streamlit as st
from hybrid_recommender import HybridRecommender

st.set_page_config(page_title="Quantum Ethno-Pharma", layout="wide")
st.title("🌿 Quantum Ethnobotany & Pharma Drug Recommender")
st.markdown("**Hybrid Classical + Quantum ML** — Natural products & synthetic drugs for any disease")

recommender = HybridRecommender()

disease = st.text_input("Enter Disease (e.g., Type 2 Diabetes, Inflammation, Malaria)", 
                       "Type 2 Diabetes Mellitus")

col1, col2 = st.columns(2)
with col1:
    top_k = st.slider("Number of recommendations", 5, 30, 15)
with col2:
    use_quantum = st.checkbox("Use Quantum VQA Oracle", value=True)

if st.button("Get Recommendations"):
    with st.spinner("Querying classical models + quantum oracle..."):
        result = recommender.recommend(disease, top_k, use_quantum)
        
        for i, rec in enumerate(result['recommendations'], 1):
            score = rec.get('combined_score', 0.5)
            st.subheader(f"#{i} — {rec['name']} ({rec['source']})")
            st.metric("Hybrid Score", f"{score:.3f}")
            st.write(f"**Modalities**: Anti-inflammatory, Antioxidant, etc.")  # Expand with real labels
            st.caption(f"SMILES: {rec['smiles'][:80]}...")

st.sidebar.warning("⚠️ Research tool only. Not medical advice.")
