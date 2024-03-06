from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS, cross_origin
from bson.objectid import ObjectId
from config import MONDO_URI
import json
import os
import dotenv
from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from fetch_news import fetch_news_api_v2, fetch_top_news_by_location, fetch_top_news_by_site, fetch_news_by_category, fetch_news, fetch_top_news

dotenv.load_dotenv()
api_key = os.getenv("RAPIDAPI_KEY")

port = 5000

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

app.config["MONGO_URI"] = MONDO_URI

mongo = PyMongo(app)
my_collection = mongo.db['news']

def add_news_to_db():
    news = fetch_news_api_v2()
    for new in news:
        new['date'] = datetime.strptime(new['date'], '%a, %d %b %Y %H:%M:%S %Z')
    news_collection = mongo.db['news']
    news_collection.insert_many(news)


scheduler = BackgroundScheduler()
scheduler.add_job(func=add_news_to_db, trigger="interval", days=1)
scheduler.start()

@app.route('/fetch_by_id/<id>', methods=['GET'])
@cross_origin()
def fetch_by_id(id):
    try:
        id = ObjectId(id)
        news = my_collection.find_one({'_id': id})
        if news:
            news['_id'] = str(news['_id'])
        print(news)
        return jsonify({
            'news': news
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
# home route
@app.route('/fetch_by_date_dsc', methods=['GET'])
@cross_origin()
def fetch_by_date_dsc():
    try:
        # Access a specific collection by its name

        # Now you can use my_collection to interact with the collection
        latest_document_cursor = my_collection.find().sort('date', -1)
        latest_document = list(latest_document_cursor)
        for doc in latest_document:
            doc['_id'] = str(doc['_id'])
        # Return some data to the client
        return jsonify({
            'news': latest_document
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
# fetch_by_date_asc
@app.route('/fetch_by_date_asc', methods=['GET'])
@cross_origin()
def fetch_by_date_asc():
    try:
        latest_document_cursor = my_collection.find().sort('date', 1)
        latest_document = list(latest_document_cursor)
        for doc in latest_document:
            doc['_id'] = str(doc['_id'])
        return jsonify({
            'news': latest_document
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# insert_many_news
@app.route('/add_many_news', methods=['POST'])
@cross_origin()
def insert_many_news():
    try:
        data = request.get_json()
        print(data)
        news_collection = mongo.db['news']
        for news in data:
            news['date'] = datetime.strptime(news['date'], '%a, %d %b %Y %H:%M:%S %Z')

        data = request.get_json()
        result = news_collection.insert_many(data)
        return json.dumps({
            "Success": 200, 
            "Inserted": len(result.inserted_ids)
            }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
if __name__ == '__main__':
    app.run(debug=True, port=5000)