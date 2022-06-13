import requests
import os
import globals
from classes import Round
from validations import validate_word
if os.path.exists("env.py"):
    import env


rapidapi_key = os.environ.get("RAPIDAPI_KEY")


def determine_win(word, answer):
    '''
    Checks the user entered answer to determine whether user entered answer is
    correct.
    '''
    if answer == word:
        print("You Win!")
        return True
    else:
        return False


def determine_results(word, answer):
    '''
    Checks the user entered answer to determine how many letters are correct.
    Instantiates the instance of the Game class and determines the values for
    each attribute of the class
    '''
    current_round = Round(False, False, [])

    if not validate_word(answer):
        current_round.show(33)
        return current_round
    else:
        results = []
        current_round.answer_valid = True
        if determine_win(word, answer):
            current_round.win = True
            current_round.show(40)
            return current_round
        else:
            current_round.show(43)
            word_array = []
            answer_array = []
            # determines characters in the word and in the correct position.
            for count, letter in enumerate(answer):
                if letter == word[count]:
                    results.insert(count, "3")
                    word_array.append("0")
                    answer_array.append("0")
                else:
                    results.insert(count, "0")
                    word_array.append(word[count])
                    answer_array.append(answer[count])
            current_round.add_round_results({answer: results})
            current_round.show(64)
            return current_round

            # Second check loops through the results array and populates
            # the values based on checks of the remaining values within
            # the word_array and answer array adding values 1, 2, or 4
            # as hints.
            # count_b = 0
            # for number in results:
            #     if number == "1" or number == "2" or number == "3":
            #         count_b += 1
            #     else:
            #         value = answer_array[count_b]
            #         word_array_value_count = count_values(word_array, value)
            #         answer_array_value_count = count_values(answer_array, value)
            #         if value not in word_array:
            #             results.pop(count_b)
            #             results.insert(count_b, "1")
            #             count_b += 1
            #         elif word_array_value_count >= answer_array_value_count:
            #             # if there is more or the same of the character value
            #             # in the word when compared to that value in the
            #             # answer then all instances of the character can be
            #             # marked as occuring in the word but not in the
            #             # correct position.
            #             for character in answer_array:
            #                 if character == value:
            #                     results.pop(count_b)
            #                     results.insert(count_b, "2")
            #             count_b += 1
            #         elif word_array_value_count < answer_array_value_count:
            #             # if there is less of the character value in the word
            #             # when compared to that value in the answer then a
            #             # more complex check is required as not all instances
            #             # of the character can be marked as occuring in the
            #             # word.
            #             insert_count = 0
            #             count_c = 0
            #             for character in answer_array:
            #                 if results[count_c] == "1" or results[count_c] == "2" or results[count_c] == "3":
            #                     count_c += 1
            #                 elif (character == value) and (insert_count == word_array_value_count):
            #                     results.pop(count_c)
            #                     results.insert(count_c, "4")
            #                     count_c += 1
            #                 elif character == value:
            #                     results.pop(count_c)
            #                     results.insert(count_c, "2")
            #                     insert_count += 1
            #                     count_c += 1
            #                 elif character != value:
            #                     results.pop(count_c)
            #                     results.insert(count_c, "0")
            #                     count_c += 1
            #             count_b += 1
            
            # print(results)
            # RESULTS_DICT.update({answer: results})
            # print(RESULTS_DICT)
            # print(type(RESULTS_DICT))
            # print(len(RESULTS_DICT))

    # current_round = rounds_remaining
    # rounds_remaining = rounds(current_round)

    # if rounds_remaining <= 0:
    #     print("Your five chances have been used! Bad Luck!")
    #     print("The word was: " + WORD)
    #     play_again()
    # elif win is not True:
    #     ask_question(rounds_remaining, WORD)


def count_values(array, value):
    '''
    Returns a count of how many times the value occurs in the array
    '''
    count = 0
    for char in array:
        if char == value:
            count += 1

    return count
