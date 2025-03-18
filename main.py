import requests

def mostrarMenu():
    print("\n--- MENU POKÉMON ---")
    print("1. Buscar Pokémon")
    print("2. Batalla Pokémon")
    print("3. Salir de la PokeAventura")

def obtener_datos_pokemon(nombre):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        nombre_pokemon = data['name'].capitalize()
        hp = next(stat['base_stat'] for stat in data['stats'] if stat['stat']['name'] == "hp")
        ataque = next(stat['base_stat'] for stat in data['stats'] if stat['stat']['name'] == "attack")
        defensa = next(stat['base_stat'] for stat in data['stats'] if stat['stat']['name'] == "defense")
        tipos = [tipo["type"]["name"].capitalize() for tipo in data["types"]]
        habilidades = [habili["ability"]["name"].capitalize() for habili in data["abilities"]] 
        
        return {"nombre": nombre_pokemon, "hp": hp, "ataque": ataque, "defensa": defensa, "tipos": tipos, "habilidades": habilidades}
    else:
        return 

def main():
    while True:
        mostrarMenu()
        opcion = input("Ingrese su Pokeopción: ").strip()

        if opcion == "1":
            pokemonName = input("Ingrese el nombre del Pokémon: ").strip().lower()
            datos = obtener_datos_pokemon(pokemonName)

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
            pokemon_a = input("Ingrese el nombre del primer Pokémon: ").strip().lower()
            datos_a = obtener_datos_pokemon(pokemon_a)
            pokemon_b = input("Ingrese el nombre del segundo Pokémon: ").strip().lower()
            datos_b = obtener_datos_pokemon(pokemon_b)

            print(f"\n⚔️ {datos_a['nombre']} VS {datos_b['nombre']} ⚔️")
            print(f"{datos_a['nombre']} (Ataque: {datos_a['ataque']}) vs {datos_b['nombre']} (Ataque: {datos_b['ataque']})")

            if datos_a['ataque'] > datos_b['ataque']:
                print(f"🏆 {datos_a['nombre']} gana la batalla!")
            elif datos_b['ataque'] > datos_a['ataque']:
                print(f"🏆 {datos_b['nombre']} gana la batalla!")
            else:
                print("⚔️ ¡Es un Pokeempate!")

        elif opcion == "3":
            print("👋 PokeAdiós, Entrenador Pokémon!")
            break

        else:
            print("❌ PokeOpción inválida, intenta de nuevo.")

if __name__ == "__main__":
    main()
