"""
Global variables required for the game
"""
# import os
# import requests
# from game_logic import validate_word

# rapidapi_key = os.environ.get("RAPIDAPI_KEY")


# def generate_word():
#     """
#     Generates a random word for the player to guess.
#     """
#     global WORD
#     url = "https://random-words5.p.rapidapi.com/getMultipleRandom"
#     querystring = {
#         "count": "1",
#         "wordLength": "5"
#     }
#     headers = {
#         "X-RapidAPI-Host": "random-words5.p.rapidapi.com",
#         "X-RapidAPI-Key": rapidapi_key
#     }

#     response = requests.request("GET", url, headers=headers, params=querystring)
#     word = response.text[2:-2]
#     if validate_word(word):
#         WORD = response.text[2:-2]
#     else:
#         generate_word()


# def game_started(value):
#     """
#     Global variable started required for gameplay flow.
#     """
#     global STARTED
#     STARTED = value
