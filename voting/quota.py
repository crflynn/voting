"""Quota calculations."""


def droop(votes, seats):
    r"""Calculate the Droop quota.

    :math:`\frac{votes}{seats + 1} + 1`

    :param int votes: the number of votes
    :param int seats: the number of seats
    """
    return int(1.0 * votes / (seats + 1) + 1)


def hagenbach_bischoff(votes, seats):
    r"""Calculate the Hagenbach-Bischoff quota.

    :math:`\frac{votes}{seats + 1}`

    :param int votes: the number of votes
    :param int seats: the number of seats
    """
    return 1.0 * votes / (seats + 1)


def hare(votes, seats):
    r"""Calculate the Hare quota.

    :math:`\frac{votes}{seats}`

    :param int votes: the number of votes
    :param int seats: the number of seats
    """
    return 1.0 * votes / seats


def imperiali(votes, seats):
    r"""Calculate the Imperiali quota.

    :math:`\frac{votes}{seats + 2}`

    :param int votes: the number of votes
    :param int seats: the number of seats
    """
    return 1.0 * votes / (seats + 2)
