"""Proportion tests."""
# flake8: noqa
import pytest

from voting.proportion import grofman


def test_proportion_method(proportion_method, votes, seats_list):
    assert proportion_method(votes, seats_list) > 0

def test_grofman_parties(votes, seats_list, parties):
    if parties not in ('votes', 'seats'):
        with pytest.raises(ValueError):
            grofman(votes, seats_list, parties)
    else:
        assert grofman(votes, seats_list, parties) > 0
