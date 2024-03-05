import dotenv
import os
dotenv.load_dotenv()
username = os.getenv("MONGODB_USERNAME")
password = os.getenv("MONGODB_PASSWORD")

cluster = os.getenv("MONGODB_CLUSTER")
db = os.getenv("MONGODB_DB")

MONDO_URI = f"mongodb+srv://{username}:{password}@{cluster}.3pezwmp.mongodb.net/{db}?retryWrites=true&w=majority"

#MONDO_URI = f"mongodb+srv://<username>:<password>@media-archive-db.3pezwmp.mongodb.net/?retryWrites=true&w=majority&appName=Media-archive-DB"