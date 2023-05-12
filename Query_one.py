from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Specify the database
db = client['pokemon']

# Specify the collection
collection = db['pokemons']


query = {"name": "Pikachu"}
pikachus = collection.find(query)


for pikachu in pikachus:
    print(pikachu)


client.close()

# Print success message
print("Query one executed successfully!")