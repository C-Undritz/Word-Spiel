"""
Required unit tests using pytest for game_logic.py
"""
import pytest
from game import game_logic


@pytest.mark.parametrize("word,answer,expected", [
    ('hello', 'hello', {'hello': ['3', '3', '3', '3', '3']}),
    ('ready', 'early', {'early': ['2', '2', '2', '1', '3']}),
    ('teeth', 'reach', {'reach': ['1', '3', '1', '1', '3']}),
    ('teeth', 'teach', {'teach': ['3', '3', '1', '1', '3']}),
    ('abbde', 'bbaec', {'bbaec': ['2', '3', '2', '2', '1']})
])
def test_result_current_results(word, answer, expected):
    """
    Tests the results returned from a round based on a given answer against a
    set word.
    """
    returned_result = game_logic.determine_results(word, answer)
    assert returned_result.current_results == expected
