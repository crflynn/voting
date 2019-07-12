"""Apportionment method tests."""


def test_apportionment_sum(apportionment_method, votes, seats):
    assert sum(apportionment_method(votes, seats)) == seats


def test_apportionment_values(apportionment_method, votes, seats_val):
    assert sum(apportionment_method(votes, seats_val)) == seats_val
