"""
Required unit tests using pytest
"""
import pytest
from game_logic import determine_results


@pytest.mark.parametrize("word,answer,expected", [
    ('hello', 'hello', {'hello': ['3', '3', '3', '3', '3']}),
    ('ready', 'early', {'early': ['2', '2', '2', '1', '3']}),
])
def test_result_current_results(word, answer, expected):
    """
    Tests the results returned from a round based on a given answer against a
    set word.
    """
    returned_result = determine_results(word, answer)
    assert returned_result.current_results == expected
