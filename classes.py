"""
Classes required for the game
"""
import os
import requests
from validations import validate_word
if os.path.exists("env.py"):
    import env

rapidapi_key = os.environ.get("RAPIDAPI_KEY")


class Round:
    """
    Round class to manage the variables and states of each round played.
    """
    def __init__(self, answer_valid, win, current_results):
        self.answer_valid = answer_valid
        self.win = win
        self.current_results = current_results

    def add_round_results(self, answer, results):
        """
        Adds the current answer and results list
        """
        self.current_results.append({answer: results})

    def show(self, line):
        """
        Prints the instatiated class current state
        """
        print('Line from which show called: ', line)
        print('Valid answer: ', self.answer_valid)
        print('Results: ', self.current_results)
        print('Win? ', self.win)

    def __str__(self):
        return f"Valid answer: {self.answer_valid}. Win: {self.win}. Results: {self.current_results}"


class Game:
    """
    Game class to manage the variables and states of each full game played.
    """
    def __init__(self, round_count, game_results):
        self.word = self.generate_word()
        self.round_count = round_count
        self.game_results = game_results

    def generate_word(self):
        """
        Generates a random word for the player to guess.
        """
        # url = "https://random-words5.p.rapidapi.com/getMultipleRandom"
        # querystring = {
        #     "count": "1",
        #     "wordLength": "5"
        # }
        # headers = {
        #     "X-RapidAPI-Host": "random-words5.p.rapidapi.com",
        #     "X-RapidAPI-Key": rapidapi_key
        # }

        # response = requests.request("GET", url, headers=headers, params=querystring)
        # word = response.text[2:-2]
        word = "abcda"
        if validate_word(word):
            return word
        else:
            self.generate_word()

    # def add_results(self, answer, results):
    #     """
    #     Adds the results dictionary with each round guess and results
    #     against each letter in the player guess
    #     """
    #     self.game_results.append({answer: results})

    def add_results(self, value):
        """
        Adds the results dictionary with each round guess and results
        against each letter in the player guess
        """
        self.game_results.append(value)

    def increment_count(self, value):
        """
        Increments the round counter by value parameter
        """
        self.round_count += value

    def show(self, line):
        """
        Prints the instatiated class current state
        """
        print('Line from which show called: ', line)
        print('Word: ', self.word)
        print('Round count: ', self.round_count)
        print('Game results: ', self.game_results)

    def __str__(self):
        return f"Word: {self.word}. Round count: {self.round_count}. Game results: {self.game_results}"