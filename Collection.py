from pymongo import MongoClient

# Connect to MongoDB
mongoClient = MongoClient("mongodb://localhost/pokemon")

# Specify the database
pokemonDB = mongoClient['pokemondb']

# Specify the collection
pokemonColl = pokemonDB['pokemon_data']

# Fetch all Pokémon documents
pokemons = pokemonColl.find()

# Iterate over the documents
for pokemon in pokemons:
    # Create a new document with combat statistics only
    pokemon_data = {
        "_id": pokemon['_id'],
        "name": pokemon['name'],
        "pokedex_number": pokemon['pokedex_number'],
        "types": [pokemon['type1'], pokemon['type2']],
        "hp": pokemon['hp'],
        "attack": pokemon['attack'],
        "defense": pokemon['defense'],
        "speed": pokemon['speed'],
        "sp_attack": pokemon['sp_attack'],
        "sp_defense": pokemon['sp_defense'],
        "abilities": pokemon['abilities']
    }
    
    # Insert the new document into the "pokemon_data" collection
    pokemonDB['pokemon_data'].insert_one(pokemon_data)

print("The Data transformation is complete! Yay!")
