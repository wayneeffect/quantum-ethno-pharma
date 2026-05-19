import os
import numpy as np

from quantum_client import QuantumOracleClient
from data_loader import DataLoader
from models.classical import ClassicalRanker


class HybridRecommender:
    def __init__(self):
        self.loader = DataLoader()
        self.classical = ClassicalRanker()
        self.quantum = QuantumOracleClient()
        
        # ✅ Fixed: os is now imported
        self.quantum_weight = float(os.getenv("QUANTUM_WEIGHT", 0.55))

    def recommend(self, disease: str, top_k: int = 15, use_quantum: bool = True):
        df = self.loader.compounds
        features = self.loader.featurize(df['smiles'].tolist())

        # Classical scores
        classical_scores = self.classical.predict_scores(features)

        # Quantum scores
        quantum_scores = self.quantum.score_compounds(features, disease) if use_quantum else [0.5] * len(features)

        # Hybrid score
        combined_scores = (1 - self.quantum_weight) * np.array(classical_scores) + \
                          self.quantum_weight * np.array(quantum_scores)

        # Add scores and sort
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
