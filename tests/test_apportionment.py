"""Apportionment method tests."""
from voting.apportionment import webster


def test_apportionment_sum(apportionment_method, votes, seats):
    assert sum(apportionment_method(votes, seats)) == seats


def test_apportionment_values(apportionment_method, votes, seats_val):
    assert sum(apportionment_method(votes, seats_val)) == seats_val


def test_webster():
    assert all([a >= 0 for a in webster([2057, 2496, 2059, 181], 15)])
