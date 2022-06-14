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
            return current_round
        else:
            # Determines characters both in the word and answer in the same
            # position.
            word_array = []
            answer_array = []
            for count, letter in enumerate(answer):
                if letter == word[count]:
                    results.insert(count, "3")
                    word_array.append("0")
                    answer_array.append("0")
                else:
                    results.insert(count, "0")
                    word_array.append(word[count])
                    answer_array.append(answer[count])

            # Determines characters in the answer that are in the word by
            # checking against the word_array.
            for count, letter in enumerate(answer_array):
                if letter == 0 or letter in word_array:
                    continue
                results.pop(count)
                results.insert(count, "1")
                answer_array.pop(count)
                answer_array.insert(count, "0")

            print("2----------------")
            print("Results array: ", str(results))
            print("Word array:    ", str(word_array))
            print("Answer array:  ", str(answer_array))
            print("-----------------")

            # for count, number in enumerate(results):
            #     if number not in ('1', '2', '3'):
            #         value = answer_array[count]
            #         print("value is: ", str(value))
            #         # word_value_count = count_values(word_array, value)
            #         # answer_value_count = count_values(answer_array, value)
            #         if value not in word_array:
            #             results.pop(count)
            #             results.insert(count, "1")
            #             print("added 1st '1'")

            #         else:
            #             # while word_value_count >= answer_value_count:
            #             word_value_count = count_values(word_array, value)
            #             print("word value count is: ", str(word_value_count))
            #             # for i in range(len(answer_array)):
            #             for count, value in enumerate(answer_array):
            #                 print("-----------------")
            #                 print("character is: ", str(answer_array[count]))
            #                 if results[count] in ('1', '2', '3'):
            #                     continue
            #                 elif answer_array[count] == value and word_value_count > 0:
            #                     results.pop(count)
            #                     results.insert(count, "2")
            #                     word_value_count -= 1
            #                     print("added a '2'")
            #                 else:
            #                     results.pop(count)
            #                     results.insert(count, "1")
            #                     print("added a final '1'")
            #                 count += 1
            #     else:
            #         print("skipped")


            # current_round.add_round_results({answer: results})
            # print("2----------------")
            # print(results)
            # print(word_array)
            # print(answer_array)

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


def count_values(data, value):
    '''
    Returns a count of how many times the value occurs in the data
    '''
    count = 0
    for char in data:
        if char == value:
            count += 1

    return count
