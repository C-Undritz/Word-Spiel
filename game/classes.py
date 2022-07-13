"""
Classes required for the game
"""
import os
import requests
from game.validations import validate_word
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
        self.current_results.update({answer: results})

    def __str__(self):
        return f"Valid answer: {self.answer_valid}. Win: {self.win}. Results: {self.current_results}"


class Game:
    """
    Game class to manage the variables and states of each full game played.
    """
    def __init__(self, round_count, game_results, win):
        self.word = self.generate_word()
        self.round_count = round_count
        self.game_results = game_results
        self.win = win

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

    def determine_win(self, value):
        """
        (*possibly not needed) Sets the win status to True is the round win is
        true
        """
        if value:
            self.win = True

    def reset(self):
        """
        Resets the instantiated Game class.
        """
        self.__init__(0, [], False)

    def __str__(self):
        return f"Word: {self.word}. Round count: {self.round_count}. Game results: {self.game_results}"
