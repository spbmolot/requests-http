# Задание 3
import requests
from pprint import pprint

def stackexchange_api():
    url = 'https://api.stackexchange.com/2.3/search/advanced?fromdate=1679184000&todate=1679356800&order=desc&sort=activity&tagged=python&site=stackoverflow'
    response = requests.get(url)
    return response.json()


if __name__ == "__main__":
    pprint(stackexchange_api())

