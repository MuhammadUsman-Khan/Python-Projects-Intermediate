import requests

def get_news(api_key):
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        articles = data['articles']
        print("\nLatest News Headlines")
        for article in articles:
            print(f"- {article['title']}")
    
    else:
        print("Failed to retrieve data!")


def main():
    api_key = "***"
    get_news(api_key)
   


if __name__ == "__main__":
    main()