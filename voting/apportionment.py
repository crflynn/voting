"""Apportionment methods."""
from math import ceil
from math import modf
from operator import itemgetter


def adams(votes, seats):
    """Apportion seats using the Adams method.

    :param list votes: a list of vote counts
    :param int seats: the number of seats to apportion
    """
    pass


def dhondt(votes, seats):
    """Apportion seats using the D'Hondt method.

    Identical to the Jefferson method.

    :param list votes: a list of vote counts
    :param int seats: the number of seats to apportion
    """
    return jefferson(votes, seats)


def hagenbach_bischoff(votes, seats):
    """Apportion seats using the Hagenbach-Bischoff method.

    Identical to the Jefferson method.

    :param list votes: a list of vote counts
    :param int seats: the number of seats to apportion
    """
    return jefferson(votes, seats)


def hamilton(votes, seats):
    """Apportion seats using the Hamilton method.

    Known also as the Vinton method.

    :param list votes: a list of vote counts
    :param int seats: the number of seats to apportion
    """
    divisor = 1.0 * sum(votes) / seats
    decs, ints = zip(*[modf(1.0 * v / divisor) for v in votes])
    ints = list(ints)
    unallocated = int(seats - sum(ints))
    leftovers = \
        [i[0] for i in sorted(enumerate(decs), key=itemgetter(1))][::-1]
    for k in range(unallocated):
        ints[leftovers[k]] += 1
    return ints


def huntington_hill(votes, seats):
    """Apportion seats using the Huntington-Hill method.

    :param list votes: a list of vote counts
    :param int seats: the number of seats to apportion
    """
    pass


def jefferson(votes, seats):
    """Apportion seats using the Jefferson method.

    Known also as the D'Hondt method or Hagenbach-Bischoff method.

    :param list votes: a list of vote counts
    :param int seats: the number of seats to apportion
    """
    divisor = 1.0 * sum(votes) / seats
    decs, ints = zip(*[modf(1.0 * v / divisor) for v in votes])
    ints = list(ints)
    unallocated = int(seats - sum(ints))
    diffs = [1.0 * vote / ceil(i + dec)
             for i, dec, vote in zip(ints, decs, votes)]
    divs = [i[0] for i in sorted(enumerate(diffs), key=itemgetter(1))][::-1]
    for k in range(unallocated):
        ints[divs[k]] += 1
    return ints


def vinton(votes, seats):
    """Apportion seats using the Vinton method.

    Identical to the Hamilton method.

    :param list votes: a list of vote counts
    :param int seats: the number of seats to apportion
    """
    return hamilton(votes, seats)


def webster(votes, seats):
    """Apportion seats using the Webster method.

    :param list votes: a list of vote counts
    :param int seats: the number of seats to apportion
    """
    pass
