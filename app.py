import requests
import os
if os.path.exists("env.py"):
    import env


rapidapi_key = os.environ.get("RAPIDAPI_KEY")


def generate_word():
    '''
    Generates a word
    '''
    url = "https://random-words5.p.rapidapi.com/getMultipleRandom"
    querystring = {
        "count": "1",
        "wordLength": "6"
    }
    headers = {
        "X-RapidAPI-Host": "random-words5.p.rapidapi.com",
        "X-RapidAPI-Key": rapidapi_key
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)
    print(response.text[2:-2])


def validate_word(word):
    '''
    Takes the word generated or entered by user to check that it is a valid
    word using wordsapi.
    '''
    url = "https://wordsapiv1.p.rapidapi.com/words/" + word + "/typeOf"

    headers = {
        "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com",
        "X-RapidAPI-Key": rapidapi_key
    }

    response = requests.request("GET", url, headers=headers)
    data = response.text
    print(data)
    result = ""

    x = 2
    while x < 9:
        result += data[x]
        x += 1

    if result == 'success':
        print("Value Entered is not a word")
    else:
        print("that is a word")


generate_word()
