"""Diversity tests."""
from voting.diversity import general
from voting.diversity import renyi


def test_diversity_method(diversity_method, votes):
    assert isinstance(diversity_method(votes), float)


def test_general_q(votes, q):
    assert isinstance(general(votes, q), float)


def test_renyi_q(votes, q):
    assert isinstance(renyi(votes, q), float)
