# data_loader.py
import pandas as pd
import os

class DataLoader:
    def __init__(self):
        self.df = self.load_expanded_database()
        self.compounds = self.df  # For compatibility with hybrid_recommender.py
    
    def load_expanded_database(self):
        """Load expanded ethnobotany + pharmaceutical database"""
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
            
            {"name": "Quercetin", "source": "Onions, Apples, Capers", "smiles": "OC1=CC(=C2C(=C1)OC(=C(C2=O)O)C3
