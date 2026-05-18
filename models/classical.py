from sklearn.ensemble import RandomForestRegressor
import xgboost as xgb
import numpy as np

class ClassicalRanker:
    def __init__(self):
        self.model = xgb.XGBRegressor(n_estimators=200, learning_rate=0.1, random_state=42)
        self.is_trained = False

    def train(self, X, y):
        self.model.fit(X, y)
        self.is_trained = True

    def predict_scores(self, X):
        if not self.is_trained:
            return np.random.uniform(0.4, 0.9, len(X))
        return self.model.predict(X)
