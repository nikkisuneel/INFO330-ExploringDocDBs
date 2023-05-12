from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Specify the database
db = client['pokemon']

# Specify the collection
collection = db['pokemons']

# using "@gt" which is the MongoDb greater than
query = {"attack": {"$gt": 150}}
pokemon_with_attack = collection.find(query)


for pokemon in pokemon_with_attack:
    print(pokemon)


client.close()

print("Query two was executed successfully!")