import requests 
import pandas as pd

API_URL = "https://api.dexscreener.com/token-boosts/top/v1"

def get_sol_tokens():
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        # Si "tokens" est la clé contenant la liste de paires
        df = pd.DataFrame(data)  # Créer un DataFrame à partir de la liste
        return df
    else:
        print(f"Erreur : {response.status_code}")
        return None

# Sauvegarder les données dans un fichier CSV
def save_tokens_to_csv(df, filename='data/token_data.xls'):
    df.to_excel('data/token_data.xlsx', index=False, engine='openpyxl')

if __name__ == "__main__":
    tokens_df = get_sol_tokens()
    if tokens_df is not None:
        save_tokens_to_csv(tokens_df)
