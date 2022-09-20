'''
Validates word generated to guess and also the word entered by the player.
Functions held here to prevent import loops.
'''
import os
import requests
if os.path.exists("env.py"):
    import env


rapidapi_key = os.environ.get("RAPIDAPI_KEY")


def validate_word(value):
    '''
    Takes the word generated or entered by user to check that it is a valid
    word using wordsapi.
    '''
    if len(value) != 5:
        return False
    return True
    # url = "https://wordsapiv1.p.rapidapi.com/words/" + value + "/typeOf"

    # headers = {
    #     "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com",
    #     "X-RapidAPI-Key": rapidapi_key
    # }

    # response = requests.request("GET", url, headers=headers)
    # data = response.text
    # result = ""

    # x = 2
    # while x < 9:
    #     result += data[x]
    #     x += 1

    # if result == 'success':
    #     return False
    # else:
    #     return True


def alpha_dict():
    """
    Creates a dictionary of the alphabet for the Game class instantiation.
    This is updated with the hint values throughout the game and used to
    render the keyboard with hints
    """
    chars = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
    chars_dict = {}
    for item in chars:
        chars_dict.update({item: '0'})  # blank

    return chars_dict
