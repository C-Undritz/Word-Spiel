'''
Works out the current round results.
'''
import os
from game.tools import validate_word
from game.classes import Round
if os.path.exists("env.py"):
    import env


rapidapi_key = os.environ.get("RAPIDAPI_KEY")


def determine_win(word, answer):
    '''
    Checks the user entered answer to determine whether user entered answer is
    correct.
    '''
    if answer == word:
        return True
    return False


def determine_results(word, answer):
    '''
    Checks the user entered answer to determine how many letters are correct.
    Instantiates an instance of the Round class and determines the values for
    each attribute of the class
    '''
    current_round = Round(False, False, {}, [])

    if not validate_word(answer):
        return current_round

    results = []
    current_round.answer_valid = True
    if determine_win(word, answer):
        current_round.win = True

    # Determines characters both in the answer and word in the same
    # position and updates the results with a '3' for each occurance.
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

    # Determines characters in the answer that are not in the word by
    # checking against the word_array and updating results with a '1'
    # for each occurance.
    for count, character in enumerate(answer_array):
        if character == 0 or character in word_array:
            continue
        results = array_update(results, count, "1")
        answer_array = array_update(answer_array, count, "0")

    # Determines characters both in the answer and word but not in the
    # same position. Updates the results with a '2' for each occurance.
    for count, character in enumerate(answer_array):
        if character == '0':
            continue
        word_char_count = count_values(word_array, character)
        if word_char_count > 0:
            results = array_update(results, count, "2")
            answer_array = array_update(answer_array, count, "0")
            # Updates word_array value with '0' so not included in
            # word_char_count on the next for loop.
            for i, value in enumerate(word_array):
                if value != character:
                    continue
                word_array = array_update(word_array, i, "0")
                break
        else:
            results = array_update(results, count, "1")
            answer_array = array_update(answer_array, count, "0")

    current_round.add_round_results(answer, results)
    current_round.add_round_hints(hints(answer, results))
    return current_round


def hints(answer, results):
    '''
    Creates a dictionary of each letter used in the guess along with the
    returned results value.  This will be used to update the hints list in the
    game class instance.
    '''
    hints_dict = {}

    # Checks and appends any letters that are a '3' (green) in the results.  
    # Prevents the incorrect logging of green letter as a '1' where the first 
    # instance if the letter in the results is in the wrong position.
    for count, character in enumerate(answer):
        if results[count] == '3':
            entry = []
            entry.append(int(results[count]))
            hints_dict.update({character: entry})

    # Checks and appends any letters that are a '1' (grey) or '2' (orange) in
    # the results.
    for count, character in enumerate(answer):
        if character in hints_dict:
            value = hints_dict[character]
            if value[0] == 1 or results[count] == '1' or results[count] == '3':
                # Ensures values of 1 or 3 will only appear once or not at all.
                continue
            value.append(int(results[count]))
            hints_dict.update({character: value})
        else:
            entry = []
            entry.append(int(results[count]))
            hints_dict.update({character: entry})

    print(f'Hints dict following the recording of remaining values {hints_dict}')

    return hints_dict


def count_values(data, value):
    '''
    Returns a count of how many times the value occurs in the data
    '''
    count = 0
    for char in data:
        if char == value:
            count += 1

    return count


def array_update(array, index, value):
    '''
    Performs required array updates during analysis of the answer
    against the word.
    '''
    array.pop(index)
    array.insert(index, value)
    return array
