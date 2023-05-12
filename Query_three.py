from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Specify the database
db = client['pokemon']

# Specify the collection
collection = db['pokemon_data']

# Using the $in operator to check if the "abilities" field contains value "Overgrow" in its list
query = {"abilities": {"$in": ["Overgrow"]}}
pokemon_with_overgrow = collection.find(query)


for pokemon in pokemon_with_overgrow:
    print(pokemon)


client.close()

print("Query three was successful!!")

