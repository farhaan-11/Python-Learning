import os
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ConfigurationError


load_dotenv()


MONGO_URI = os.getenv("DB_STRING")

# jis database se kaam karna hai uska naam
DB_NAME = "fastapi_practice"

db = None

# agar .env me DB_STRING milta hi nahi to connect karne ki koshish bhi mat karo
if not MONGO_URI:
    print("DB_STRING .env file me nahi mili")
else:
    try:
        
        client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)

        # "ping" command bhej ke check kar rahe hai ki server tak pahunch rahe hai ya nahi
        client.admin.command("ping")

        # yaha tak agar error nahi aayi to matlab connection successful hai
        print("MongoDB se connection successful hua")

     
        db = client[DB_NAME]

    except ConnectionFailure as e:
        # server band hai ya reachable nahi hai (galat host/port, MongoDB service off, etc)
        print("MongoDB se connect nahi ho paya:", e)

    except ConfigurationError as e:
        # DB_STRING ka format hi galat hai
        print("MongoDB connection URI galat hai:", e)
