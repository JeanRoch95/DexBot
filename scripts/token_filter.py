import pandas as pd

# Appliquer les filtres de base (par exemple volume et liquidité)
def filter_tokens(df, min_volume=10000, min_liquidity=5000):
    filtered_df = df[(df['volumeUsd24h'] > min_volume) & (df['liquidityUsd'] > min_liquidity)]
    return filtered_df

if __name__ == "__main__":
    df = pd.read_csv('data/token_data.csv')
    filtered_df = filter_tokens(df)
    print(filtered_df)
