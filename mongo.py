#mongodb+srv://robertomartinperez:<password>@cluster0.haq5t30.mongodb.net/

import pymongo

client = pymongo.MongoClient("mongodb+srv://robertomartinperez:FLgIFtmfx5xtcyKN@cluster0.haq5t30.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.sample_mflix
collection = db.movies

items = collection.find().limit(5)

for item in items:
    print(item)