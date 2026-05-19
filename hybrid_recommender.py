import os
from quantum_client import QuantumOracleClient
from data_loader import DataLoader
from models.classical import ClassicalRanker
import numpy as np

class HybridRecommender:
    def __init__(self):
        self.loader = DataLoader()
        self.classical = ClassicalRanker()
        self.quantum = QuantumOracleClient()
        
        # Fixed: Import os at the top
        self.quantum_weight = float(os.getenv("QUANTUM_WEIGHT", 0.55))

    def recommend(self, disease: str, top_k: int = 15, use_quantum: bool = True):
        df = self.loader.compounds
        features = self.loader.featurize(df['smiles'].tolist())

        # Supervised Classical Scores
        classical_scores = self.classical.predict_scores(features)

        # Quantum Enhancement
        quantum_scores = self.quantum.score_compounds(features, disease) if use_quantum else [0.5] * len(features)

        # Hybrid Fusion
        combined_scores = (1 - self.quantum_weight) * np.array(classical_scores) + \
                          self.quantum_weight * np.array(quantum_scores)

        df = df.copy()
        df['combined_score'] = combined_scores
        df = df.sort_values('combined_score', ascending=False)

        recommendations = df.head(top_k).to_dict('records')

        return {
            "disease": disease,
            "recommendations": recommendations,
            "metadata": {
                "quantum_used": use_quantum,
                "quantum_weight": self.quantum_weight
            }
        }
