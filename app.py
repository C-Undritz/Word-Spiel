import requests
import os
if os.path.exists("env.py"):
    import env


rapidapi_key = os.environ.get("RAPIDAPI_KEY")
start_rounds = 5


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
    return response.text[2:-2]


def ask_question(rounds_remaining):
    '''
    Asks the user to enter a word
    '''
    # new_word = generate_word()
    print(new_word)
    answer = input("please enter a word: ")
    win = False
    results = []
    determine_results(new_word, win, answer, results, rounds_remaining)


def determine_results(word, win, answer, results, rounds_remaining):
    '''
    checks the user entered word to determine the win state and the hints array
    '''
    if validate_word(answer):
        if answer == word:
            win = True
            print("You Win!") 
            play_again()
        else:
            count = 0
            for letter in answer:
                if letter in word:
                    results.insert(count, "*")
                    if letter in word[count]:
                        results.pop(count)
                        results.insert(count, "$")
                    count += 1
                else:
                    results.insert(count, "-")
                    count += 1

        current_round = rounds_remaining
        rounds_remaining = rounds(current_round)

        if rounds_remaining <= 0:
            print("Your five chances have been used! Bad Luck!")
            play_again()
        elif win != True:
            print(results)
            ask_question(rounds_remaining)
    else:
        print("That is not word you FOOL!!!")


def play_again():
    continue_play = input("Would you like to play again? Enter Y or N: ")

    if continue_play == "Y" or continue_play == "y":
        ask_question(5)
    elif continue_play == "N" or continue_play == "n":
        print("Thanks and come back soon")
    else:
        play_again()


def rounds(current_round):
    print(current_round)
    rounds_remaining = current_round - 1
    return rounds_remaining


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
        return False
    else:
        print("that is a word")
        return True


ask_question(start_rounds)
