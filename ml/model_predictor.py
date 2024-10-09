import pandas as pd
import pickle

# Charger le modèle
with open('models/model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Charger les données des nouveaux tokens
new_tokens_df = pd.read_csv('data/token_data.csv')

# Prédire les tokens à fort potentiel
X_new = new_tokens_df[['volumeUsd24h', 'liquidityUsd']]
predictions = model.predict(X_new)

# Afficher les prédictions
new_tokens_df['is_explosive'] = predictions
print(new_tokens_df[new_tokens_df['is_explosive'] == 1])  # Affiche uniquement les tokens "explosifs"
