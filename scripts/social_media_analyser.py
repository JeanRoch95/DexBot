import requests

# Exemple pour Twitter (nécessite une clé API)
TWITTER_API_URL = "https://api.twitter.com/2/tweets/search/recent"

def analyze_social_media(token_symbol, twitter_bearer_token):
    headers = {
        'Authorization': f'Bearer {twitter_bearer_token}'
    }
    params = {
        'query': f'#{token_symbol}',
        'tweet.fields': 'public_metrics',
    }
    response = requests.get(TWITTER_API_URL, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        return data['meta']['result_count']  # Nombre de tweets récents
    else:
        print(f"Erreur : {response.status_code}")
        return None

if __name__ == "__main__":
    token_symbol = "SOL"
    twitter_bearer_token = "your_twitter_api_bearer_token"
    print(f"Nombre de tweets pour {token_symbol}: {analyze_social_media(token_symbol, twitter_bearer_token)}")
