# styles.py
def apply_quantum_theme():
    """Apply the Quantum Ethno-Pharma custom theme"""
    
    css = """
    <style>
        /* ====================== QUANTUM ETHNO-PHARMA THEME ====================== */
        
        .stApp {
            background: linear-gradient(135deg, #0a0f1a 0%, #111827 100%);
            color: #e0f2e9;
        }
        
        /* Header */
        h1 {
            background: linear-gradient(90deg, #22c55e, #a855f7, #60a5fa);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 700;
            letter-spacing: -0.025em;
        }
        
        /* Main containers */
        .stCard, div[data-testid="stExpander"], .stMarkdown, div[data-testid="stVerticalBlock"] > div {
            background: rgba(15, 23, 42, 0.85) !important;
            border: 1px solid rgba(74, 222, 128, 0.25);
            border-radius: 16px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
        }
        
        /* Buttons */
        .stButton > button {
            background: linear-gradient(90deg, #22c55e, #4ade80);
            color: #0f172a;
            font-weight: 600;
            border-radius: 12px;
            border: none;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        .stButton > button:hover {
            transform: translateY(-3px);
            box-shadow: 0 0 25px rgba(74, 222, 128, 0.6);
        }
        
        /* Inputs */
        .stTextInput > div > div > input,
        .stSelectbox > div > div > div,
        .stMultiselect > div > div > div,
        .stSlider > div {
            background: #1e2937 !important;
            border: 1px solid #4ade80 !important;
            border-radius: 10px;
            color: #e0f2e9;
        }
        
        /* Metrics */
        .stMetric {
            background: rgba(16, 185, 129, 0.08);
            border: 1px solid #4ade80;
            border-radius: 12px;
            padding: 12px;
        }
        
        /* Sidebar */
        section[data-testid="stSidebar"] {
            background: #0f172a;
            border-right: 2px solid #22c55e;
        }
        
        section[data-testid="stSidebar"] .stMarkdown {
            border: none;
        }
        
        /* Quantum glow */
        .quantum-title {
            text-shadow: 0 0 20px #a855f7,
                         0 0 40px #60a5fa;
        }
        
        /* Scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
            height: 8px;
        }
        ::-webkit-scrollbar-thumb {
            background: linear-gradient(#22c55e, #4ade80);
            border-radius: 10px;
        }
        
        /* Dataframes */
        .stDataFrame {
            border-radius: 12px;
            overflow: hidden;
        }
    </style>
    """
    
    return css
