# data_loader.py
import pandas as pd
import os

def load_expanded_database():
    """Load significantly expanded ethnobotany + pharmaceutical database"""
    
    data = [
        # === HIGH-IMPACT NATURAL PRODUCTS ===
        {"name": "Curcumin", "source": "Turmeric (Curcuma longa)", "smiles": "OC1=CC=C(C=C1)C=CC(=O)C2=CC(=C(C=C2)O)O", 
         "modalities": ["Anti-inflammatory", "Antioxidant", "Anticancer"], 
         "disease_associations": ["Type 2 Diabetes", "Inflammation", "Arthritis"], 
         "evidence": "High", "combined_score": 0.92},
        
        {"name": "Resveratrol", "source": "Japanese Knotweed, Grapes", "smiles": "OC1=CC=C(C=C1)C=CC2=CC(=CC(=C2)O)O", 
         "modalities": ["Antioxidant", "Cardioprotective", "Anti-aging"], 
         "disease_associations": ["Type 2 Diabetes", "Cardiovascular"], 
         "evidence": "High", "combined_score": 0.88},
        
        {"name": "Artemisinin", "source": "Sweet Wormwood (Artemisia annua)", "smiles": "CC1CCC2C(C)C(=O)OC3OC4(C)CCC1C32OO4", 
         "modalities": ["Antimalarial"], 
         "disease_associations": ["Malaria"], "evidence": "Very High", "combined_score": 0.95},
        
        {"name": "Quercetin", "source": "Onions, Apples, Capers", "smiles": "OC1=CC(=C2C(=C1)OC(=C(C2=O)O)C3=CC=C(C=C3)O)O", 
         "modalities": ["Anti-inflammatory", "Antioxidant", "Antihistamine"], 
         "disease_associations": ["Inflammation", "Allergies"], "evidence": "High", "combined_score": 0.85},
        
        {"name": "Berberine", "source": "Goldenseal, Barberry", "smiles": "COc1cc2c(cc1OC)c3c4c(c5c6c(cc(c6[nH]c5c4[nH]c3c2)OC)OC)OC", 
         "modalities": ["Antidiabetic", "Antimicrobial"], 
         "disease_associations": ["Type 2 Diabetes"], "evidence": "High", "combined_score": 0.89},
        
        # === MORE TRADITIONAL ETHNOBOTANICALS ===
        {"name": "Ginsenoside Rg1", "source": "Panax Ginseng", "smiles": "CC1(C)C(CCC2(C)C1CCC3C2(C)CCC4C3(C)CCC(O4)C5(C)OC(C(O)C(O)C5O)O)C(O)C(O)C(O)C(O)CO", 
         "modalities": ["Antidiabetic", "Adaptogenic", "Anti-inflammatory"], 
         "disease_associations": ["Type 2 Diabetes", "Fatigue"], "evidence": "High", "combined_score": 0.87},
        
        {"name": "Andrographolide", "source": "Andrographis paniculata (King of Bitters)", "smiles": "CC1(C)C2CCC3C(C)(C)C(O)CCC3(C)C2C(=C)C(=O)OC1", 
         "modalities": ["Antimalarial", "Anti-inflammatory", "Immunomodulatory"], 
         "disease_associations": ["Malaria", "Inflammation"], "evidence": "High", "combined_score": 0.84},
        
        {"name": "Azadirachtin", "source": "Neem (Azadirachta indica)", "smiles": "COC(=O)C1=C(C)C2C3C(OC4OCC5C4C6(C)C(C7C(C)(C)C(OC(=O)C)C(O)C7O6)OC5)C2C1O", 
         "modalities": ["Antimalarial", "Antimicrobial"], 
         "disease_associations": ["Malaria"], "evidence": "High", "combined_score": 0.82},
        
        {"name": "Momordicin", "source": "Bitter Melon (Momordica charantia)", "smiles": "CC1(C)C2CCC3(C)C(C)(C)CCC4C5(C)CCC(O)C(C)(C)C5CCC43C2C1O", 
         "modalities": ["Antidiabetic"], 
         "disease_associations": ["Type 2 Diabetes"], "evidence": "High", "combined_score": 0.86},
        
        {"name": "Fenugreek Saponins", "source": "Fenugreek (Trigonella foenum-graecum)", "smiles": "CC1OC(OC2C(O)C(O)C(OC3C(O)C(O)C(O)C(CO)O3)C2O)C(O)C(O)C1O", 
         "modalities": ["Antidiabetic", "Hypolipidemic"], 
         "disease_associations": ["Type 2 Diabetes"], "evidence": "High", "combined_score": 0.83},
        
        {"name": "Moringa Flavonoids", "source": "Moringa oleifera", "smiles": "OC1=CC(=C2C(=C1)OC(=C(C2=O)O)C3=CC=C(C=C3)O)O", 
         "modalities": ["Antidiabetic", "Antioxidant"], 
         "disease_associations": ["Type 2 Diabetes", "Inflammation"], "evidence": "High", "combined_score": 0.81},
        
        # === MORE ANTI-INFLAMMATORY & PAIN ===
        {"name": "Boswellic Acid", "source": "Frankincense (Boswellia serrata)", "smiles": "CC1(C)C2CCC3C(C)(C)C(O)CCC3(C)C2C(=C)C(=O)OC1", 
         "modalities": ["Anti-inflammatory"], 
         "disease_associations": ["Arthritis", "Inflammation"], "evidence": "High", "combined_score": 0.88},
        
        {"name": "Capsaicin", "source": "Chili Peppers (Capsicum)", "smiles": "CC(C)C1=CC=C(C=C1)C=CC(=O)NCC2=CC(=C(C=C2)O)OC", 
         "modalities": ["Analgesic", "Anti-inflammatory"], 
         "disease_associations": ["Pain", "Inflammation"], "evidence": "High", "combined_score": 0.85},
        
        # === SYNTHETICS WITH NATURAL ORIGINS ===
        {"name": "Metformin", "source": "Synthetic (Biguanide)", "smiles": "CN(C)C(=N)N=C(N)N", 
         "modalities": ["Antidiabetic"], 
         "disease_associations": ["Type 2 Diabetes"], "evidence": "Very High", "combined_score": 0.94},
        
        {"name": "Aspirin", "source": "Synthetic (from Willow Bark)", "smiles": "CC(=O)OC1=CC=CC=C1C(=O)O", 
         "modalities": ["Anti-inflammatory", "Analgesic"], 
         "disease_associations": ["Inflammation", "Pain"], "evidence": "Very High", "combined_score": 0.91},
        
        {"name": "Chloroquine", "source": "Synthetic (from Cinchona bark inspiration)", "smiles": "CCN(CC)CCCC(C)NC1=CC=NC2=C1C=CC=C2Cl", 
         "modalities": ["Antimalarial"], 
         "disease_associations": ["Malaria"], "evidence": "Very High", "combined_score": 0.90},
    ]
    
    # You can keep adding more here easily
    
    df = pd.DataFrame(data)
    return df


def save_database(df, path="database/expanded_ethno_pharma.json"):
    """Save database for persistence"""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_json(path, orient="records", indent=2)
    print(f"✅ Database saved to {path} ({len(df)} compounds)")
