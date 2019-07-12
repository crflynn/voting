"""Measures of disproportionality."""
from math import sqrt

from voting.util import normalize


def adjusted_loosemore_hanby(votes, seats, parties="votes"):
    r"""Calculate the adjusted Loosemore-Hanby index of disproportionality.

    .. math::

        N \sum_{i=1}^n |v_i - s_i|

    where N is :math:`\sum_{i=1}^n v_i` if ``parties == 'votes'`` or
    :math:`\sum_{i=1}^n s_i` if ``parties == 'seats'``.

    :param list votes: a list of vote counts
    :param list seats: a list of seat counts
    :param str parties: ``votes`` or ``seats`` to use to calculate the
        effective number of parties
    """
    votes = normalize(votes)
    seats = normalize(seats)
    return grofman(votes, seats, parties)


def dhondt(votes, seats):
    r"""Calculate the D'Hondt index of disproportionality.

    .. math::

        \max \frac{s_i}{v_i}

    :param list votes: a list of vote counts
    :param list seats: a list of seat counts
    """
    votes = normalize(votes)
    seats = normalize(seats)
    return max([1.0 * s / v for v, s in zip(votes, seats)])


def gallagher(votes, seats):
    r"""Calculate the Gallagher index of disproportionality.

    .. math::

        \sqrt{\frac{1}{2} \sum_{i=1}^n (v_i - s_i)^2}

    :param list votes: a list of vote counts
    :param list seats: a list of seat counts
    """
    votes = normalize(votes)
    seats = normalize(seats)
    return sqrt(1.0 / 2) * least_square(votes, seats)


def grofman(votes, seats, parties="votes"):
    r"""Calculate the Grofman index of disproportionality.

    .. math::

        N \sum_{i=1}^n |v_i - s_i|

    where N is :math:`\sum_{i=1}^n v_i^2` if ``parties == 'votes'`` or
    :math:`\sum_{i=1}^n s_i^2` if ``parties == 'seats'``.

    :param list votes: a list of vote counts
    :param list seats: a list of seat counts
    :param str parties: ``votes`` or ``seats`` to use to calculate the
        effective number of parties
    """
    votes = normalize(votes)
    seats = normalize(seats)
    if parties == "votes":
        n = sum([v ** 2 for v in votes])
    elif parties == "seats":
        n = sum([s ** 2 for s in seats])
    else:
        raise ValueError("Parties argument must be either votes or seats.")

    return n * sum([abs(v - s) for v, s in zip(votes, seats)])


def least_square(votes, seats):
    r"""Calculate the least squares index of disproportionality.

    .. math::

        \sqrt{\sum_{i=1}^n (v_i - s_i)^2}

    :param list votes: a list of vote counts
    :param list seats: a list of seat counts
    """
    votes = normalize(votes)
    seats = normalize(seats)
    return sqrt(sum([(v - s) ** 2 for v, s in zip(votes, seats)]))


def lijphart(votes, seats):
    r"""Calculate the Lijphart index of disproportionality.

    .. math::

        \max | v_i - s_i |

    :param list votes: a list of vote counts
    :param list seats: a list of seat counts
    """
    votes = normalize(votes)
    seats = normalize(seats)
    return max([abs(v - s) for v, s in zip(votes, seats)])


def loosemore_hanby(votes, seats):
    r"""Calculate Loosemore-Hanby index of disproportionality.

    .. math::

        \frac{1}{2} \sum_{i=1}^n |v_i - s_i|

    :param list votes: a list of vote counts
    :param list seats: a list of seat counts
    """
    votes = normalize(votes)
    seats = normalize(seats)
    return 1.0 / 2 * sum([abs(v - s) for v, s in zip(votes, seats)])


def rae(votes, seats):
    r"""Calculate Rae's index of disproportionality.

    .. math::

        \frac{1}{n} \sum_{i=1}^n |v_i - s_i|

    :param list votes: a list of vote counts
    :param list seats: a list of seat counts
    """
    votes = normalize(votes)
    seats = normalize(seats)
    return 1.0 / len(votes) * sum([abs(v - s) for v, s in zip(votes, seats)])


def regression(votes, seats):
    r"""Calculate the regression index of disproportionality.

    .. math::

        \frac{\sum_{i=1}^n v_i s_i}{\sum_{i=1}^n v_i^2}

    :param list votes: a list of vote counts
    :param list seats: a list of seat counts
    """
    votes = normalize(votes)
    seats = normalize(seats)
    num = sum([v * s for v, s in zip(votes, seats)])
    denom = sum([v ** 2 for v in votes])
    return 1.0 * num / denom


def rose(votes, seats):
    r"""Calculate the Rose index of proportionality.

    .. math::

        100 - \frac{1}{2} \sum_{i=1}^n |v_i - s_i|

    :param list votes: a list of vote counts
    :param list seats: a list of seat counts
    """
    votes = normalize(votes)
    seats = normalize(seats)
    return 100 - loosemore_hanby(votes, seats)


def sainte_lague(votes, seats):
    r"""Calculate the Sainte-Lague index of disproportionality.

    .. math::

        \sum_{i=1}^n \frac{(v_i - s_i)^2}{v_i}

    :param list votes: a list of vote counts
    :param list seats: a list of seat counts
    """
    votes = normalize(votes)
    seats = normalize(seats)
    return sum(1.0 / v * (v - s) ** 2 for v, s in zip(votes, seats))
