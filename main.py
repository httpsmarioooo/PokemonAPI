import requests

def mostrarMenu():
    print("\n--- MENU POKÉMON ---")
    print("1. Buscar Pokémon")
    print("2. Batalla Pokémon")
    print("3. Salir de la PokeAventura")

def obtenerDatosPokemon(pokemonName):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemonName.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        nombrePokemon = data['name'].capitalize()

        hp = next(stat['base_stat'] for stat in data['stats'] if stat['stat']['name'] == "hp")
        #! stats se llama el grupo
        #! base stat = es el valor en este caso pika tiene un ataque de 55
        #! stat es el subgrupo en donde esta:
            #! name es el nombre, en este ejemplo attack
        ataque = next(stat['base_stat'] for stat in data['stats'] if stat['stat']['name'] == "attack")
        defensa = next(stat['base_stat'] for stat in data['stats'] if stat['stat']['name'] == "defense")
        tipos = [tipo["type"]["name"].capitalize() for tipo in data["types"]]
        habilidades = [habili["ability"]["name"].capitalize() for habili in data["abilities"]] 
        
        return {"nombre": nombrePokemon, "hp": hp, "ataque": ataque, "defensa": defensa, "tipos": tipos, "habilidades": habilidades}
    else:
        return 

def main():
    while True:
        mostrarMenu()
        opcion = input("Ingrese su Pokeopción: ").strip()

        if opcion == "1":
            pokemonName = input("Ingrese el nombre del Pokémon: ").strip().lower()
            datos = obtenerDatosPokemon(pokemonName)

            if datos:
                print(f"\n🔍 Información de {datos['nombre']}:")
                print(f"Tipos: {', '.join(datos['tipos'])}")
                print(f"HP: {datos['hp']}")
                print(f"Ataque: {datos['ataque']}")
                print(f"Defensa: {datos['defensa']}")
                print(f"Habilidades: {datos['habilidades']}")
            else:
                print("❌ Error: Pokémon no encontrado. Verifica el nombre.")

        elif opcion == "2":
            print("\n🔥 ¡Batalla Pokémon! 🔥")
            pokemonA = input("Ingrese el nombre del primer Pokémon: ").strip().lower()
            datosPokemonA = obtenerDatosPokemon(pokemonA)
            pokemonB = input("Ingrese el nombre del segundo Pokémon: ").strip().lower()
            datosPokemonB = obtenerDatosPokemon(pokemonB)

            print(f"\n⚔️ {datosPokemonA['nombre']} VS {datosPokemonB['nombre']} ⚔️")
            print(f"{datosPokemonA['nombre']} (Ataque: {datosPokemonA['ataque']}) vs {datosPokemonB['nombre']} (Ataque: {datosPokemonB['ataque']})")

            if datosPokemonA['ataque'] > datosPokemonB['ataque']:
                print(f"🏆 {datosPokemonA['nombre']} gana la batalla!")
            elif datosPokemonB['ataque'] > datosPokemonA['ataque']:
                print(f"🏆 {datosPokemonB['nombre']} gana la batalla!")
            else:
                print("⚔️ ¡Es un Pokeempate!")

        elif opcion == "3":
            print("👋 PokeAdiós, Entrenador Pokémon!")
            break

        else:
            print("❌ PokeOpción inválida, intenta de nuevo.")

if __name__ == "__main__":
    main()
