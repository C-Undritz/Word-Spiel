"""
Required unit tests using pytest for classes.py
"""
from classes import Game, Round


def test_new_round():
    """
    GIVEN a new round
    WHEN an the first answer is submitted
    THEN check that 'answer_valid', 'win' and 'current_results' are initiated correctly
    """
    new_round = Round(False, False, {})
    assert new_round.answer_valid is False
    assert new_round.win is False
    assert new_round.current_results == {}


def test_new_game():
    """
    GIVEN a new game
    WHEN a game is started
    THEN check that 'round_count', 'game_results' and 'win' are initiated correctly
    """
    new_game = Game(0, [], False)
    assert new_game.round_count == 0
    assert new_game.game_results == []
    assert new_game.win is False
