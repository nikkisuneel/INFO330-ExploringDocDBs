from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Specify the database
db = client['pokemon']

# Specify the collection
collection = db['pokemons']

# Using the $regex operator to find match documents where the "abilities" field has the substring "Overgrow"
query = {"abilities": {"$regex": ".*Overgrow.*"}}
pokemon_with_overgrow = collection.find(query)


for pokemon in pokemon_with_overgrow:
    print(pokemon)


client.close()

print("Query three was successful!!")

