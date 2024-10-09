import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

# Charger les données historiques
df = pd.read_csv('data/historical_data.csv')

# Extraction des caractéristiques (features) et de la cible (target)
X = df[['volumeUsd24h', 'liquidityUsd']]  # Caractéristiques
y = df['is_explosive']  # Variable cible (1 pour explosif, 0 pour non explosif)

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entraîner un modèle de régression logistique
model = LogisticRegression()
model.fit(X_train, y_train)

# Sauvegarder le modèle entraîné
with open('models/model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)
