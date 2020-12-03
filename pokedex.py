import json


def build_dex():
    try:
        with open("pokedex.json", "r") as file:
            data = json.load(file)

        print(json.dumps(data))
    except IOError:
        print("Error: pokedex.json file does not exist.")
        return


if __name__ == "__main__":
    build_dex()
