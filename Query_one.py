from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Specify the database
db = client['pokemon']

# Specify the collection
collection = db['pokemon_data']

# Query for all Pokémon named "Pikachu"
query = {"name": "Pikachu"}
pikachus = collection.find(query)

# Print the results
for pikachu in pikachus:
    print(pikachu)

# Close the MongoDB connection
client.close()

# Print success message
print("Query executed successfully!")