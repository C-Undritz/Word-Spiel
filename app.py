import requests
import os
from flask import Flask
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

rapidapi_key = os.environ.get("RAPIDAPI_KEY")
start_rounds = 5


@app.route("/")
def hello():
    return"Hello World"


# def start_game():
#     '''
#     Generates a new word and starts the game
#     '''
#     new_word = generate_word()
#     print(new_word)
#     ask_question(start_rounds, new_word)


# def generate_word():
#     '''
#     Generates a random word for the player to guess
#     '''
#     url = "https://random-words5.p.rapidapi.com/getMultipleRandom"
#     querystring = {
#         "count": "1",
#         "wordLength": "6"
#     }
#     headers = {
#         "X-RapidAPI-Host": "random-words5.p.rapidapi.com",
#         "X-RapidAPI-Key": rapidapi_key
#     }

#     response = requests.request("GET", url, headers=headers, params=querystring)
#     return response.text[2:-2]


# def ask_question(rounds_remaining, word):
#     '''
#     Asks the user to enter a word and sets a number of start game variables
#     '''
#     answer = input("please enter a word: ")
#     win = False
#     results = []
#     determine_results(word, win, answer, results, rounds_remaining)


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
#             count_a = 0
#             word_array = []
#             answer_array = []
#             # First check loops through the player answer and determines any
#             # characters that are present in the word and are in the correct
#             # position.  For each or these a '3' is entered into the results
#             # array.  For any that are not then a '0' is entered into the
#             # results array.  Two new arrays are populated: word_array and
#             # answer_array, which are needed for the next checks.  These are
#             # populated with the characters from the word and answer, but
#             # where there is a correct answer at this stage a '0' is added,
#             # as this value has already been assessed and should not be
#             # included in the next stage of checks.
#             for letter in answer:
#                 if letter in word[count_a]:
#                     results.insert(count_a, "3")
#                     word_array.append("0")
#                     answer_array.append("0")
#                 else:
#                     results.insert(count_a, "0")
#                     word_array.append(word[count_a])
#                     answer_array.append(answer[count_a])
#                 count_a += 1

#             # Second check loops through the results array and populates the
#             # values based on checks of the remaining values within the
#             # word_array and answer array adding values 1, 2, or 4 as hints.
#             count_b = 0
#             for number in results:
#                 if number == "1" or number == "2" or number == "3" or number == "4":
#                     count_b += 1
#                 else:
#                     value = answer_array[count_b]
#                     word_array_value_count = count_values(word_array, value)
#                     answer_array_value_count = count_values(answer_array, value)
#                     if value not in word_array:
#                         results.pop(count_b)
#                         results.insert(count_b, "1")
#                         count_b += 1
#                     elif word_array_value_count >= answer_array_value_count:
#                         # if there is more or the same of the character value
#                         # in the word when compared to that value in the
#                         # answer then all instances of the character can be
#                         # marked as occuring in the word but not in the
#                         # correct position.
#                         for character in answer_array:
#                             if character == value:
#                                 results.pop(count_b)
#                                 results.insert(count_b, "2")
#                         count_b += 1
#                     elif word_array_value_count < answer_array_value_count:
#                         # if there is less of the character value in the word
#                         # when compared to that value in the answer then a
#                         # more complex check is required as not all instances
#                         # of the character can be marked as occuring in the
#                         # word.
#                         insert_count = 0
#                         count_c = 0
#                         for character in answer_array:
#                             if results[count_c] == "1" or results[count_c] == "2" or results[count_c] == "3" or results[count_c] == "4":
#                                 count_c += 1
#                             elif (character == value) and (insert_count == word_array_value_count):
#                                 results.pop(count_c)
#                                 results.insert(count_c, "4")
#                                 count_c += 1
#                             elif character == value:
#                                 results.pop(count_c)
#                                 results.insert(count_c, "2")
#                                 insert_count += 1
#                                 count_c += 1
#                             elif character != value:
#                                 results.pop(count_c)
#                                 results.insert(count_c, "0")
#                                 count_c += 1
#                         count_b += 1

#         print(results)
#         current_round = rounds_remaining
#         rounds_remaining = rounds(current_round)

#         if rounds_remaining <= 0:
#             print("Your five chances have been used! Bad Luck!")
#             print("The word was: " + word)
#             play_again()
#         elif win is not True:
#             ask_question(rounds_remaining, word)
#     else:
#         print("That is not word you FOOL!!!")
#         ask_question(rounds_remaining, word)


# def play_again():
#     '''
#     Determines options for comtinued play after completion of five rounds or
#     if the user wins
#     '''
#     continue_play = input("Would you like to play again? Enter Y or N: ")

#     if continue_play == "Y" or continue_play == "y":
#         start_game()
#     elif continue_play == "N" or continue_play == "n":
#         print("Thanks and come back soon")
#     else:
#         play_again()


# def rounds(current_round):
#     '''
#     Keeps the count of rounds
#     '''
#     rounds_remaining = current_round - 1
#     print(rounds_remaining)
#     return rounds_remaining


# def validate_word(word):
#     '''
#     Takes the word generated or entered by user to check that it is a valid
#     word using wordsapi.
#     '''
#     url = "https://wordsapiv1.p.rapidapi.com/words/" + word + "/typeOf"

#     headers = {
#         "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com",
#         "X-RapidAPI-Key": rapidapi_key
#     }

#     response = requests.request("GET", url, headers=headers)
#     data = response.text
#     result = ""

#     x = 2
#     while x < 9:
#         result += data[x]
#         x += 1

#     if result == 'success':
#         return False
#     else:
#         return True


# def count_values(array, value):
#     '''
#     Returns a count of how many times the value occurs in the array
#     '''
#     count = 0
#     for char in array:
#         if char == value:
#             count += 1

#     return count


# start_game()

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)