import streamlit as st
from hybrid_recommender import HybridRecommender
from styles import apply_quantum_theme   # ← New import

# ====================== PAGE CONFIG ======================
st.set_page_config(
    page_title="Quantum Ethno-Pharma",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ====================== APPLY THEME ======================
st.markdown(apply_quantum_theme(), unsafe_allow_html=True)

# ====================== HEADER ======================
st.markdown("""
    <h1 class="quantum-title" style="text-align: center; margin-bottom: 8px;">
        🌿 Quantum Ethno-Pharma
    </h1>
    <p style="text-align: center; color: #94a3b8; font-size: 1.15em; margin-top: 0;">
        Hybrid Classical + Quantum Intelligence for Ethnobotany & Drug Discovery
    </p>
""", unsafe_allow_html=True)

# ====================== MAIN APP ======================
recommender = HybridRecommender()

disease = st.text_input("Enter Disease (e.g., Type 2 Diabetes, Inflammation, Malaria)", 
                       "Type 2 Diabetes Mellitus")

col1, col2 = st.columns(2)
with col1:
    top_k = st.slider("Number of recommendations", 5, 30, 15)
with col2:
    use_quantum = st.checkbox("Use Quantum VQA Oracle", value=True)

if st.button("🚀 Get Recommendations", type="primary"):
    with st.spinner("Querying classical models + quantum oracle..."):
        result = recommender.recommend(disease, top_k, use_quantum)
        
        st.success(f"Found {len(result['recommendations'])} hybrid recommendations")
        
        for i, rec in enumerate(result['recommendations'], 1):
            score = rec.get('combined_score', 0.5)
            
            with st.container():
                st.subheader(f"#{i} — {rec['name']} ({rec['source']})")
                st.metric("Hybrid Score", f"{score:.3f}")
                st.write(f"**Modalities**: Anti-inflammatory, Antioxidant, etc.")  # TODO: Use real data
                st.caption(f"SMILES: {rec['smiles'][:80]}...")
                st.divider()

# ====================== SIDEBAR ======================
st.sidebar.warning("⚠️ Research tool only. Not medical advice.")
st.sidebar.info("Built with Classical ML + Quantum-Inspired Optimization")
