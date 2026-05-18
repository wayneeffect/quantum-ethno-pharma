import os
import requests
from dotenv import load_dotenv
import time

load_dotenv()

class QuantumOracleClient:
    def __init__(self):
        self.base_url = os.getenv("QUANTUM_ORACLE_URL")
        self.timeout = 30

    def score_compounds(self, features_list: list, disease: str):
        """Call your VQA oracle"""
        try:
            payload = {
                "features": features_list,  # List of feature vectors
                "disease": disease,
                "objective": "binding_affinity_proxy"
            }
            response = requests.post(
                f"{self.base_url}/hybrid_vqe_qaoa",  # Adjust endpoint as needed
                json=payload,
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json().get("scores", [0.5] * len(features_list))
        except Exception as e:
            print(f"Quantum oracle failed: {e}. Using fallback.")
            return [0.5] * len(features_list)  # Classical fallback
