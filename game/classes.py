"""
Classes required for the game
"""
import os
import requests
from game.tools import validate_word, alpha_dict
if os.path.exists("env.py"):
    import env

rapidapi_key = os.environ.get("RAPIDAPI_KEY")


class Round:
    """
    Round class to manage the variables and states of each round played.
    """
    def __init__(self, answer_valid, win, current_results, current_hints):
        self.answer_valid = answer_valid
        self.win = win
        self.current_results = current_results
        self.current_hints = current_hints

    def add_round_results(self, answer, results):
        """
        Adds the current answer and results list
        """
        self.current_results.update({answer: results})

    def add_round_hints(self, hints):
        """
        Adds the current hints dictionary
        """
        self.current_hints.append(hints)

    def __str__(self):
        return f"Valid answer: {self.answer_valid}. Win: {self.win}. Results: {self.current_results}. Hints: {self.current_hints}"


class Game:
    """
    Game class to manage the variables and states of each full game played.
    """
    def __init__(self, round_count, game_results, game_hints_dict, game_hints_list, win):
        self.word = self.generate_word()
        self.round_count = round_count
        self.game_results = game_results
        self.game_hints_dict = game_hints_dict
        self.game_hints_list = game_hints_list
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
        word = "hello"
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

    def update_hints(self, item):
        """
        Updates the ongoing hints dictionary against each letter in all
        guesses within a game and assigns a value that will dicate how
        the keyboard button is displayed.
        """
        dict_item = item[0]
        for key, value in dict_item.items():
            if len(value) == 1:
                if value[0] == 1:
                    self.game_hints_dict.update({key: 'grey'})
                elif value[0] == 2:
                    self.game_hints_dict.update({key: 'orange'})
                elif value[0] == 3:
                    self.game_hints_dict.update({key: 'green'})
            else:
                if sum(value) in (5, 7, 8):
                    self.game_hints_dict.update({key: 'mixed'})
                elif sum(value) == 4:
                    self.game_hints_dict.update({key: 'orange'})
                else:
                    self.game_hints_dict.update({key: 'green'})

            self.hints_list(self.game_hints_dict)

    def hints_list(self, hints):
        """
        Takes the updated game_hints_dict and separates it into three
        dictionaries based on a QWERTY keyboard.  Three dictionaries are
        then placed in a list.
        """
        self.game_hints_list.clear()

        row_one_keys = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
        row_two_keys = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
        row_three_keys = ['z', 'x', 'c', 'v', 'b', 'n', 'm']

        row_one = {x: hints[x] for x in hints if x in row_one_keys}
        row_two = {x: hints[x] for x in hints if x in row_two_keys}
        row_three = {x: hints[x] for x in hints if x in row_three_keys}

        self.game_hints_list.append(row_one)
        self.game_hints_list.append(row_two)
        self.game_hints_list.append(row_three)

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
        self.__init__(1, [], alpha_dict(), [], False)

    def __str__(self):
        return f"Word: {self.word}. Round count: {self.round_count}. Win: {self.win}. Game results: {self.game_results}. Game hints list: {self.game_hints_list}"
