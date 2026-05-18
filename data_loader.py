import pandas as pd
from rdkit import Chem
from rdkit.Chem import AllChem, Descriptors

class DataLoader:
    def __init__(self):
        self.compounds = self._load_sample_data()

    def _load_sample_data(self):
        # In production: Load from Duke's, COCONUT CSV, DrugBank, ChEMBL
        # Example: pd.read_csv("coconut_lite.csv"), standardize SMILES with RDKit
        data = {
            'compound_id': ['NP1', 'NP2', 'DRUG1', 'NP3'],
            'name': ['Curcumin', 'Artemisinin', 'Metformin', 'Quercetin'],
            'smiles': [
                'O=C(C=Cc1ccc(O)c(OC)c1)CC(=O)C=Cc2ccc(O)c(OC)c2',  # Curcumin
                'CC1CCC2C(C)C(=O)OC3OC4C(C)CCC5C(C)C(=O)OC(O)C24C13', # Artemisinin (simplified)
                'CN(C)C(=N)N=C(N)N',  # Metformin
                'O=c1cc(O)c2c(c1O)c(O)c(O)c(O)c2'  # Quercetin simplified
            ],
            'source': ['Duke/COCONUT', 'Duke', 'DrugBank', 'COCONUT'],
            'modality_labels': [[1,0,1], [1,1,0], [0,1,0], [1,0,1]]  # e.g., anti-inflam, anti-malarial, etc.
        }
        return pd.DataFrame(data)

    def featurize(self, smiles_list):
        features = []
        for smiles in smiles_list:
            mol = Chem.MolFromSmiles(smiles)
            if mol:
                fp = AllChem.GetMorganFingerprintAsBitVect(mol, radius=2, nBits=2048)
                desc = [
                    Descriptors.MolWt(mol),
                    Descriptors.TPSA(mol),
                    Descriptors.NumHDonors(mol),
                    Descriptors.NumHAcceptors(mol)
                ]
                features.append(list(fp)[:256] + desc)  # Hybrid fingerprint + descriptors
            else:
                features.append([0]*260)
        return features
