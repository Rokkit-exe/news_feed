import os
from datetime import datetime, timedelta
import requests

base_url = "https://newsnow.p.rapidapi.com"
# News API v2 endpoint
endpoint = "newsv2"
# Top news by location endpoint
endpoint1 = "newsv2_top_news_location"
# News API v2 endpoint
endpoint2 = "newsv2_top_news_site"
# News API v2 endpoint
endpoint3 = "newsv2_top_news_cat"

# newsv2 by google
def fetch_news_api_v2(api_key, query="AI", location="us", language="en", page=1, days=7):
    url = "https://newsnow.p.rapidapi.com/newsv2"
    current_date = datetime.now()
    from_date = current_date - timedelta(days=days)
    payload = {
        "query": query,
        "time_bounded": True,
        "from_date": from_date.strftime("%d/%m/%Y"),
        "to_date": current_date.strftime("%d/%m/%Y"),
        "location": location,
        "language": language,
        "page": page
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "newsnow.p.rapidapi.com"
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

# newsv2 top news by location by google
def fetch_top_news_by_location(api_key, location="us", language="en", page=1):
    url = "https://newsnow.p.rapidapi.com/newsv2_top_news_location"
    payload = {
        "location": location,
        "language": language,
        "page": page
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "newsnow.p.rapidapi.com"
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

# newsv2 top news by site by google
def fetch_top_news_by_site(api_key, language="en", site="yahoo.com", page=1 ):
    url = "https://newsnow.p.rapidapi.com/newsv2_top_news_site"
    payload = {
        "language": language,
        "site": site,
        "page": page
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "newsnow.p.rapidapi.com"
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

# newsv2 news by category by google
def fetch_news_by_category(api_key, category="TECHNOLOGY", language="en", location="us", page=1 ):
    url = "https://newsnow.p.rapidapi.com/newsv2_top_news_cat"
    payload = {
        "category": category,
        "location": location,
        "language": language,
        "page": page
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "newsnow.p.rapidapi.com"
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

# news from Duck Duck Go
def fetch_news(api_key, text="Europe", region="wt-wt", max_results=25):
    url = "https://newsnow.p.rapidapi.com/"
    payload = {
        "text": text,
        "region": region,
        "max_results": max_results
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "newsnow.p.rapidapi.com"
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

# top news from Duck Duck Go
def fetch_top_news(api_key, region="wt-wt", max_results=25):
    url = "https://newsnow.p.rapidapi.com/"
    payload = {
        "text": "Top news",
        "region": region,
        "max_results": max_results
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "newsnow.p.rapidapi.com"
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()
