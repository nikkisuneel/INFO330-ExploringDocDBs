import random
from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

def fetch(pokemonid):
    return pokemonColl.find_one({"pokedex_number":pokemonid})

def battle(pokemon1, pokemon2):
    print("Let the Pokemon battle begin! ================")
    print("It's " + pokemon1['name'] + " vs " + pokemon2['name'])
    # Getting the score of the overall stats for each Pokemon only based on their combat stats
    pokemon_one_score = sum(pokemon1[stat] for stat in ['hp', 'attack', 'defense', 'speed', 'sp_attack', 'sp_defense'])
    pokemon_two_score = sum(pokemon2[stat] for stat in ['hp', 'attack', 'defense', 'speed', 'sp_attack', 'sp_defense'])

    # Comparing the scores of the pokemon to see who is winner
    if pokemon_one_score > pokemon_two_score:
        print(pokemon1['name'] + " wins!")
    elif pokemon_two_score > pokemon_one_score:
        print(pokemon2['name'] + " wins!")
    else:
        print("Yay, well that's a tie!")

    print("Stats comparison:")
    for stat in ['hp', 'attack', 'defense', 'speed', 'sp_attack', 'sp_defense']:
        # Then comparing a Pokemon's specific stats and what they have advantages over
        if pokemon1[stat] > pokemon2[stat]:
            print(pokemon1['name'] + " is better in their ability " + stat)
        elif pokemon2[stat] > pokemon1[stat]:
            print(pokemon2['name'] + "is better in their ability " + stat)
        else:
            print("The Pokemon share ability level on " + stat + " stat.")

def main():
    # Fetch two pokemon from the MongoDB database
    pokemon1 = fetch(random.randrange(801))
    pokemon2 = fetch(random.randrange(801))

    # Pit them against one another
    battle(pokemon1, pokemon2)

main()
