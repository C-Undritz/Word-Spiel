import requests
import os
if os.path.exists("env.py"):
    import env


rapidapi_key = os.environ.get("RAPIDAPI_KEY")
start_rounds = 5


def start_game():
    '''
    Generates a new word and starts the game
    '''
    new_word = generate_word()
    print(new_word)
    print(length(new_word))
    ask_question(start_rounds, new_word)


def generate_word():
    '''
    Generates a random word for the player to guess
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
    # print(response.text)
    # print(response.text[2:-2])
    return response.text[2:-2]


def ask_question(rounds_remaining, word):
    '''
    Asks the user to enter a word and sets a number of start game variables
    '''
    # print(word)
    answer = input("please enter a word: ")
    win = False
    results = []
    determine_results(word, win, answer, results, rounds_remaining)


# def determine_results(word, win, answer, results, rounds_remaining):
#     '''
#     checks the user entered word to determine the win state and the hints array
#     '''
#     if validate_word(answer):
#         if answer == word:
#             win = True
#             print("You Win!") 
#             play_again()
#         else:
#             count = 0
#             for letter in answer:
#                 if letter in word:
#                     results.insert(count, "*")
#                     if letter in word[count]:
#                         results.pop(count)
#                         results.insert(count, "$")
#                     count += 1
#                 else:
#                     results.insert(count, "-")
#                     count += 1

#         current_round = rounds_remaining
#         rounds_remaining = rounds(current_round)

#         if rounds_remaining <= 0:
#             print("Your five chances have been used! Bad Luck!")
#             print("The word was: " + word)
#             play_again()
#         elif win is not True:
#             print(results)
#             ask_question(rounds_remaining, word)
#     else:
#         print("That is not word you FOOL!!!")
#         ask_question(rounds_remaining, word)


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
            while count < answer.len():
                print(word[count])
                print(answer[count])
                if word[count] == answer[count]:
                    results.insert(count, "$")
                elif functionX(word, answer, count):
                    results.insert(count, "*")
                else:
                    results.insert(count, "-")    
                count += 1
                print(results)

        print(results)
        current_round = rounds_remaining
        rounds_remaining = rounds(current_round)

        if rounds_remaining <= 0:
            print("Your five chances have been used! Bad Luck!")
            print("The word was: " + word)
            play_again()
        elif win is not True:
            print(results)
            ask_question(rounds_remaining, word)
    else:
        print("That is not word you FOOL!!!")
        ask_question(rounds_remaining, word)



def play_again():
    '''
    Determines options for comtinued play after completion of five rounds or 
    if the user wins
    '''
    continue_play = input("Would you like to play again? Enter Y or N: ")

    if continue_play == "Y" or continue_play == "y":
        start_game()
    elif continue_play == "N" or continue_play == "n":
        print("Thanks and come back soon")
    else:
        play_again()


def rounds(current_round):
    '''
    Keeps the count of rounds
    '''
    rounds_remaining = current_round - 1
    print(rounds_remaining)
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
    # print(data)
    result = ""

    x = 2
    while x < 9:
        result += data[x]
        x += 1

    if result == 'success':
        # print("Value Entered is not a word")
        return False
    else:
        # print("that is a word")
        return True


start_game()
