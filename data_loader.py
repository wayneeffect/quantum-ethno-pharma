# data_loader.py
import pandas as pd
import numpy as np

class DataLoader:
    def __init__(self):
        self.df = self.load_expanded_database()
        self.compounds = self.df
    
    def load_expanded_database(self):
        data = [
            {"name": "Curcumin", "source": "Turmeric", "smiles": "OC1=CC=C(C=C1)C=CC(=O)C2=CC(=C(C=C2)O)O", "modalities": ["Anti-inflammatory", "Antioxidant"], "disease_associations": ["Type 2 Diabetes"], "evidence": "High", "combined_score": 0.92},
            {"name": "Resveratrol", "source": "Grapes", "smiles": "OC1=CC=C(C=C1)C=CC2=CC(=CC(=C2)O)O", "modalities": ["Antioxidant"], "disease_associations": ["Type 2 Diabetes"], "evidence": "High", "combined_score": 0.88},
            {"name": "Artemisinin", "source": "Sweet Wormwood", "smiles": "CC1CCC2C(C)C(=O)OC3OC4(C)CCC1C32OO4", "modalities": ["Antimalarial"], "disease_associations": ["Malaria"], "evidence": "Very High", "combined_score": 0.95},
            {"name": "Quercetin", "source": "Onions", "smiles": "OC1=CC(=C2C(=C1)OC(=C(C2=O)O)C3=CC=C(C=C3)O)O", "modalities": ["Anti-inflammatory"], "disease_associations": ["Inflammation"], "evidence": "High", "combined_score": 0.85},
            {"name": "Berberine", "source": "Barberry", "smiles": "COc1cc2c(cc1OC)c3c4c(c5c6c(cc(c6[nH]c5c4[nH]c3c2)OC)OC)OC", "modalities": ["Antidiabetic"], "disease_associations": ["Type 2 Diabetes"], "evidence": "High", "combined_score": 0.89},
            {"name": "Metformin", "source": "Synthetic", "smiles": "CN(C)C(=N)N=C(N)N", "modalities": ["Antidiabetic"], "disease_associations": ["Type 2 Diabetes"], "evidence": "Very High", "combined_score": 0.94}
        ]
        return pd.DataFrame(data)
    
    def featurize(self, smiles_list):
        return np.random.rand(len(smiles_list), 64)
