import requests
import os
if os.path.exists("env.py"):
    import env


rapidapi_key = os.environ.get("RAPIDAPI_KEY")


def generate_word():
    '''
    Generates a random word for the player to guess
    '''
    url = "https://random-words5.p.rapidapi.com/getMultipleRandom"
    querystring = {
        "count": "1",
        "wordLength": "5"
    }
    headers = {
        "X-RapidAPI-Host": "random-words5.p.rapidapi.com",
        "X-RapidAPI-Key": rapidapi_key
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text[2:-2]
