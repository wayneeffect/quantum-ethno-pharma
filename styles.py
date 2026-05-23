# styles.py
def apply_quantum_theme():
    """Apply Jungle / Ethnobotany Theme"""
    
    css = """
    <style>
        /* ====================== JUNGLE ETHNOBOTANY THEME ====================== */
        
        .stApp {
            background: linear-gradient(135deg, #0f1a14 0%, #1a2f21 100%);
            color: #e8f5e9;
        }
        
        /* Header */
        h1 {
            background: linear-gradient(90deg, #4ade80, #22c55e, #eab308);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 700;
            letter-spacing: -0.02em;
        }
        
        /* Containers & Cards */
        .stCard, div[data-testid="stExpander"], .stMarkdown, 
        div[data-testid="stVerticalBlock"] > div {
            background: rgba(16, 35, 25, 0.92) !important;
            border: 1px solid rgba(74, 222, 128, 0.35);
            border-radius: 18px;
            box-shadow: 0 10px 35px rgba(0, 0, 0, 0.5);
        }
        
        /* Buttons */
        .stButton > button {
            background: linear-gradient(90deg, #4ade80, #22c55e);
            color: #0f1a14;
            font-weight: 600;
            border-radius: 14px;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton > button:hover {
            transform: translateY(-3px);
            box-shadow: 0 0 25px rgba(74, 222, 128, 0.7);
        }
        
        /* Inputs */
        .stTextInput > div > div > input,
        .stSelectbox > div > div > div,
        .stMultiselect > div > div > div,
        .stSlider > div {
            background: #1a2f21 !important;
            border: 1px solid #4ade80 !important;
            border-radius: 12px;
            color: #e8f5e9;
        }
        
        /* Slider */
        .stSlider .stSliderTickBar {
            color: #86efac;
        }
        
        /* Metrics */
        .stMetric {
            background: rgba(74, 222, 128, 0.12);
            border: 1px solid #4ade80;
            border-radius: 14px;
        }
        
        /* Sidebar */
        section[data-testid="stSidebar"] {
            background: #0c1a14;
            border-right: 3px solid #4ade80;
        }
        
        /* Quantum / Jungle Glow */
        .quantum-title {
            text-shadow: 0 0 20
