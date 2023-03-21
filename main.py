# Задание 1
import requests

def superhero_api():
    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url)
    return response.json()


def list():
    max_mind_hero = {}
    for superhero in superhero_api():
        if superhero["name"] == "Hulk" or superhero["name"] == "Captain America" or superhero["name"] == "Thanos":
            max_mind_hero[superhero["name"]] = superhero["powerstats"]["intelligence"]
    print(f'Самый умный: {" ".join([i for i , n in max_mind_hero.items() if n == max(max_mind_hero.values())])}')


if __name__ == "__main__":
    list()

