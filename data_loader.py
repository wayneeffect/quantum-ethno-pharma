# data_loader.py
import pandas as pd
import os
import numpy as np

class DataLoader:
    def __init__(self):
        self.df = self.load_expanded_database()
        self.compounds = self.df
    
    def load_expanded_database(self):
        """Expanded ethnobotany + pharmaceutical database"""
        data = [
            {"name": "Curcumin", "source": "Turmeric (Curcuma longa)", 
             "smiles": "OC1=CC=C(C=C1)C=CC(=O)C2=CC(=C(C=C2)O)O", 
             "modalities": ["Anti-inflammatory", "Antioxidant", "Anticancer"], 
             "disease_associations": ["Type 2 Diabetes", "Inflammation", "Arthritis"], 
             "evidence": "High", "combined_score": 0.92},
            
            {"name": "Resveratrol", "source": "Japanese Knotweed, Grapes", 
             "smiles": "OC1=CC=C(C=C1)C=CC2=CC(=CC(=C2)O)O", 
             "modalities": ["Antioxidant", "Cardioprotective"], 
             "disease_associations": ["Type 2 Diabetes", "Cardiovascular"], 
             "evidence": "High", "combined_score": 0.88},
            
            {"name": "Artemisinin", "source": "Sweet Wormwood (Artemisia annua)", 
             "smiles": "CC1CCC2C(C)C(=O)OC3OC4(C)CCC1C32OO4", 
             "modalities": ["Antimalarial"], 
             "disease_associations": ["Malaria"], "evidence": "Very High", "combined_score": 0.95},
            
            {"name": "Quercetin", "source": "Onions, Apples, Capers", 
             "smiles": "OC1=CC(=C2C(=C1)OC(=C(C2=O)O)C3=CC=C(C=C3)O)O", 
             "modalities": ["Anti-inflammatory", "Antioxidant"], 
             "disease_associations": ["Inflammation", "Allergies"], "evidence": "High", "combined_score": 0.85},
            
            {"name": "Berberine", "source": "Goldenseal, Barberry", 
             "smiles": "COc1cc2c(cc1OC)c3c4c(c5c6c(cc(c6[nH]c5c4[nH]c3c2)OC)OC)OC", 
             "modalities": ["Antidiabetic", "Antimicrobial"], 
             "disease_associations": ["Type 2 Diabetes"], "evidence": "High", "combined_score": 0.89},
            
            {"name": "Ginsenoside Rg1", "source": "Panax Ginseng", 
             "smiles": "CC1(C)C(CCC2(C)C1CCC3C2(C)CCC4C3(C)CCC(O4)C5(C)OC(C(O)C(O)C5O)O)C(O)C(O)C(O)C(O)CO", 
             "modalities": ["Antidiabetic", "Adaptogenic"], 
             "disease_associations": ["Type 2 Diabetes"], "evidence": "High", "combined_score": 0.87},
            
            {"name": "Andrographolide", "source": "Andrographis paniculata", 
             "smiles": "CC1(C)C2CCC3C(C)(C)C(O)CCC3(C)C2C(=C)C(=O)OC1", 
             "modalities": ["Antimalarial", "Anti-inflammatory"], 
             "disease_associations": ["Malaria", "Inflammation"], "evidence": "High", "combined_score": 0.84},
            
            {"name": "Boswellic Acid", "source": "Frankincense (Boswellia serrata)", 
             "smiles": "CC1
