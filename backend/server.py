from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from config import MONDO_URI
import os
import dotenv
from datetime import datetime, timedelta
from fetch_news import fetch_news_api_v2, fetch_top_news_by_location, fetch_top_news_by_site, fetch_news_by_category, fetch_news, fetch_top_news
dotenv.load_dotenv()
api_key = os.getenv("RAPIDAPI_KEY"),

port = 5000

app = Flask(__name__)

app.config["MONGO_URI"] = MONDO_URI

mongo = PyMongo(app)

# home route
@app.route('/', methods=['GET'])
def index():
    try:
        # Access a specific collection by its name
        my_collection = mongo.db['news']

        print(my_collection)

        # Now you can use my_collection to interact with the collection
        data = my_collection.find_one()
        print(data)
        # Return some data to the client
        return {'name': data['name']}
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# sentiment analysis route
@app.route('/sentiment', methods=['POST'])
def fetch_news():
    try:
        data = request.get_json()
        print(data['text'])
        output = jsonify({
            "Success": 200,
            "request": "POST /sentiment",
            "model": data['model'],
            "data": data["text"]
        })
        return output
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
if __name__ == '__main__':
    app.run(debug=True, port=5000)
    api_v2 = fetch_news_api_v2(api_key, query="AI", location="us", language="en", page=1, days=7)
    news_by_location = fetch_top_news_by_location(api_key, location="us", language="en", page=1)
    news_by_site = fetch_top_news_by_site(api_key, language="en", site="yahoo.com", page=1 )
    news_by_category = fetch_news_by_category(api_key, category="TECHNOLOGY", language="en", location="us", page=1 )
    news = fetch_news(api_key, language="en", page=1)
    top_news = fetch_top_news(api_key, language="en", page=1)