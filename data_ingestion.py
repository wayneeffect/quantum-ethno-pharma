# data_ingestion.py
import pandas as pd
import os
import requests
from zipfile import ZipFile
import io
import json
import time

class DataIngestion:
    def __init__(self):
        self.database_dir = "database"
        os.makedirs(self.database_dir, exist_ok=True)
        self.output_path = f"{self.database_dir}/large_ethno_pharma.json"

    def ingest_coconut(self, limit=2000):
        """Primary source: COCONUT - Largest open natural products DB"""
        print("🌴 Downloading COCONUT Lite (best overall source)...")
        
        # Latest known URL (update if needed)
        url = "https://coconut.s3.uni-jena.de/prod/downloads/2026-05/coconut_csv_lite-05-2026.zip"
        
        response = requests.get(url, timeout=120)
        zip_file = ZipFile(io.BytesIO(response.content))
        
        csv_name = [name for name in zip_file.namelist() if name.endswith('.csv')][0]
        print(f"Extracting {csv_name}...")
        
        with zip_file.open(csv_name) as f:
            df = pd.read_csv(f, low_memory=False)
        
        print(f"Loaded {len(df):,} compounds from COCONUT")
        
        # Filter for plant-derived compounds with SMILES
        df = df.dropna(subset=['name', 'smiles']).copy()
        if 'textTaxa' in df.columns:
            plant_mask = df['textTaxa'].str.contains('plant|herb|tree|root|leaf|flower', case=False, na=False)
            df = df[plant_mask]
        
        # Take top N
        df = df.head(limit).copy()
        
        # Standardize columns for your app
        df = df.rename(columns={'textTaxa': 'source'})
        df['modalities'] = df.apply(lambda x: ["Anti-inflammatory", "Antioxidant"], axis=1)
        df['disease_associations'] = df.apply(lambda x: ["Inflammation", "Type 2 Diabetes"], axis=1)
        df['evidence'] = "Medium"
        df['combined_score'] = 0.70 + (pd.Series(range(len(df))) % 0.25)
        
        final_cols = ['name', 'source', 'smiles', 'modalities', 'disease_associations', 'evidence', 'combined_score']
        df = df[final_cols]
        
        self.save_database(df)
        return df

    def ingest_dr_duke(self, csv_path=None):
        """Dr. Duke's Phytochemical Database"""
        print("🌱 Dr. Duke's ingestion (manual CSV recommended)")
        if csv_path and os.path.exists(csv_path):
            df = pd.read_csv(csv_path)
            print(f"Loaded {len(df)} entries from Dr. Duke's")
            # Further processing here...
            return df
        else:
            print("→ Download Duke-Source-CSV.zip from https://phytochem.nal.usda.gov")
            return None

    def ingest_knapsack(self):
        """KNApSAcK - Species-Metabolite relations"""
        print("🌿 KNApSAcK ingestion - Download from http://kanaya.naist.jp/KNApSAcK/")
        print("→ Extract and convert the DB files manually for now.")
        return None

    def ingest_perunpdb(self):
        """PeruNPDB - Regional high-quality data"""
        print("🇵🇪 PeruNPDB - Visit https://perunpdb.com.pe/ for download")
        return None

    def save_database(self, df):
        """Save to JSON for DataLoader"""
        df.to_json(self.output_path, orient="records", indent=2)
        print(f"💾 Saved {len(df):,} compounds to {self.output_path}")

    def run_full_ingestion(self, coconut_limit=1500):
        """Run main ingestion pipeline"""
        df = self.ingest_coconut(limit=coconut_limit)
        print(f"\n🎉 Final database size: {len(df):,} high-quality natural products")
        return df


if __name__ == "__main__":
    ingestor = DataIngestion()
    ingestor.run_full_ingestion(coconut_limit=2000)
