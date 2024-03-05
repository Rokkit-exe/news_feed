from fetch_news import fetch_news_api_v2, fetch_top_news_by_location, fetch_top_news_by_site, fetch_news_by_category, fetch_news, fetch_top_news
import os 
import dotenv
import json
dotenv.load_dotenv()
api_key = "33ded9223fmsh566de0a1510ddc2p18533cjsn6ff22722e6b9"

api_v2 = fetch_news_api_v2(api_key)
if False:
    news_by_location = fetch_top_news_by_location(api_key)
    news_by_site = fetch_top_news_by_site(api_key)
    news_by_category = fetch_news_by_category(api_key)
    news = fetch_news(api_key)
    top_news = fetch_top_news(api_key)

with open('api_v2.json', 'w') as f:
    json.dump(api_v2, f)

if False:
    with open('news_by_location.json', 'w') as f:
        json.dump(news_by_location, f)

    with open('news_by_site.json', 'w') as f:
        json.dump(news_by_site, f)

    with open('news_by_category.json', 'w') as f:
        json.dump(news_by_category, f)

    with open('news.json', 'w') as f:
        json.dump(news, f)

    with open('top_news.json', 'w') as f:
        json.dump(top_news, f)