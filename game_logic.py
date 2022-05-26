import requests
import os
if os.path.exists("env.py"):
    import env


rapidapi_key = os.environ.get("RAPIDAPI_KEY")
WORD = None
CREATE_RESULTS_DICT = False
RESULTS_DICT = {}


def generate_word():
    '''
    Generates a random word for the player to guess
    '''
    global WORD
    global CREATE_RESULTS_DICT
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
    WORD = response.text[2:-2]
    CREATE_RESULTS_DICT = True
    print("line 29 ", WORD)


def determine_win(answer):
    '''
    Checks the user entered answer to determine whether user entered answer is
    correct.
    '''
    if answer == WORD:
        print("You Win!")
        return True
    else:
        return False


def determine_results(answer):
    '''
    Checks the user entered answer to determine how many letters are correct
    '''
    global CREATE_RESULTS_DICT
    global RESULTS_DICT

    print("line 36 ", WORD)
    results = []

    # if answer == WORD:
    #     win = True
    #     print("You Win!")
    #     # play_again()
    # else:
    if validate_word(answer):
        count_a = 0
        word_array = []
        answer_array = []
        # First check loops through the player answer and determines any
        # characters that are present in the word and are in the correct
        # position.  For each or these a '3' is entered into the results
        # array.  For any that are not then a '0' is entered into the
        # results array.  Two new arrays are populated: word_array and
        # answer_array, which are needed for the next checks.  These are
        # populated with the characters from the word and answer, but
        # where there is a correct answer at this stage a '0' is added,
        # as this value has already been assessed and should not be
        # included in the next stage of checks.
        for letter in answer:
            if letter in WORD[count_a]:
                results.insert(count_a, "3")
                word_array.append("0")
                answer_array.append("0")
            else:
                results.insert(count_a, "0")
                word_array.append(WORD[count_a])
                answer_array.append(answer[count_a])
            count_a += 1

        # Second check loops through the results array and populates the
        # values based on checks of the remaining values within the
        # word_array and answer array adding values 1, 2, or 4 as hints.
        count_b = 0
        for number in results:
            if number == "1" or number == "2" or number == "3" or number == "4":
                count_b += 1
            else:
                value = answer_array[count_b]
                word_array_value_count = count_values(word_array, value)
                answer_array_value_count = count_values(answer_array, value)
                if value not in word_array:
                    results.pop(count_b)
                    results.insert(count_b, "1")
                    count_b += 1
                elif word_array_value_count >= answer_array_value_count:
                    # if there is more or the same of the character value
                    # in the word when compared to that value in the
                    # answer then all instances of the character can be
                    # marked as occuring in the word but not in the
                    # correct position.
                    for character in answer_array:
                        if character == value:
                            results.pop(count_b)
                            results.insert(count_b, "2")
                    count_b += 1
                elif word_array_value_count < answer_array_value_count:
                    # if there is less of the character value in the word
                    # when compared to that value in the answer then a
                    # more complex check is required as not all instances
                    # of the character can be marked as occuring in the
                    # word.
                    insert_count = 0
                    count_c = 0
                    for character in answer_array:
                        if results[count_c] == "1" or results[count_c] == "2" or results[count_c] == "3" or results[count_c] == "4":
                            count_c += 1
                        elif (character == value) and (insert_count == word_array_value_count):
                            results.pop(count_c)
                            results.insert(count_c, "4")
                            count_c += 1
                        elif character == value:
                            results.pop(count_c)
                            results.insert(count_c, "2")
                            insert_count += 1
                            count_c += 1
                        elif character != value:
                            results.pop(count_c)
                            results.insert(count_c, "0")
                            count_c += 1
                    count_b += 1

        print(results)
        RESULTS_DICT.update({answer: results})
        print(RESULTS_DICT)
        print(type(RESULTS_DICT))
        print(len(RESULTS_DICT))
        
    return RESULTS_DICT
    # current_round = rounds_remaining
    # rounds_remaining = rounds(current_round)

    # if rounds_remaining <= 0:
    #     print("Your five chances have been used! Bad Luck!")
    #     print("The word was: " + WORD)
    #     play_again()
    # elif win is not True:
    #     ask_question(rounds_remaining, WORD)


def validate_word(value):
    '''
    Takes the word generated or entered by user to check that it is a valid
    word using wordsapi.
    '''
    url = "https://wordsapiv1.p.rapidapi.com/words/" + value + "/typeOf"

    headers = {
        "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com",
        "X-RapidAPI-Key": rapidapi_key
    }

    response = requests.request("GET", url, headers=headers)
    data = response.text
    result = ""

    x = 2
    while x < 9:
        result += data[x]
        x += 1

    if result == 'success':
        return False
    else:
        return True


def count_values(array, value):
    '''
    Returns a count of how many times the value occurs in the array
    '''
    count = 0
    for char in array:
        if char == value:
            count += 1

    return count