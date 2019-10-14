"""Apportionment method tests."""
<<<<<<< HEAD
=======
from voting.apportionment import adams
>>>>>>> master
from voting.apportionment import webster


def test_apportionment_sum(apportionment_method, votes, seats):
    assert sum(apportionment_method(votes, seats)) == seats


def test_apportionment_values(apportionment_method, votes, seats_val):
    assert sum(apportionment_method(votes, seats_val)) == seats_val


def test_webster():
    assert all([a >= 0 for a in webster([2057, 2496, 2059, 181], 15)])


def test_adams():
    assert adams([10, 1], 2) == [1, 1]

    votes = [
        1918578,
        1348072,
        1023503,
        937901,
        639747,
        625263,
        621832,
        610408,
        455025,
        429811,
        405843,
        399454,
        343031,
        319922,
        297665,
        280657,
        269326,
        262508,
        171904,
        157147,
        130419,
        110358,
        97194,
        75432,
    ]
    seats = 240
    result = [37, 26, 20, 18, 13, 12, 12, 12, 9, 9, 8, 8, 7, 7, 6, 6, 6, 6, 4, 4, 3, 3, 2, 2]
    assert adams(votes, seats) == result

