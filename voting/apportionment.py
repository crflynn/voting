"""Apportionment methods."""
from math import ceil
from math import floor
from math import modf
from math import sqrt
from operator import itemgetter


def adams(votes, seats):
    """Apportion seats using the Adams method.

    :param list votes: a list of vote counts
    :param int seats: the number of seats to apportion
    """
    divisor = 1.0 * sum(votes) / seats
    decs, lower = zip(*[modf(1.0 * v / divisor) for v in votes])
    upper = [ceil(1.0 * v / divisor) for v in votes]
    surplus = int(sum(upper) - seats)
    while surplus > 0:
        # divisors that would remove another seat to each group
        divisors = [1.0 * vote / max(floor(allocated + dec), 1) for allocated, dec, vote in zip(lower, decs, votes)]
        # argsort low to high
        divs = [i[0] for i in sorted(enumerate(divisors), key=itemgetter(1))]
        for k in divs:
            if divisors[k] > divisor:
                idx = k
                break
        # if they're all zero, subtract from the largest group
        else:
            largest = [i[0] for i in sorted(enumerate(votes), key=itemgetter(1))]
            idx = largest[-1]
        divisor = divisors[idx]
        decs, lower = zip(*[modf(1.0 * v / divisor) for v in votes])
        upper = [ceil(1.0 * v / divisor) for v in votes]
        surplus = int(sum(upper) - seats)
    return upper


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
    decs, lower = zip(*[modf(1.0 * v / divisor) for v in votes])
    lower = [int(l) for l in lower]
    unallocated = int(seats - sum(lower))
    if unallocated > 0:
        # argsort high to low
        leftovers = [i[0] for i in sorted(enumerate(decs), key=itemgetter(1))][::-1]
        for k in range(unallocated):
            lower[leftovers[k]] += 1
    return lower


def huntington_hill(votes, seats):
    """Apportion seats using the Huntington-Hill method.

    :param list votes: a list of vote counts
    :param int seats: the number of seats to apportion
    """
    if seats < len(votes):
        raise ValueError("Must be at least one seat per group.")
    elif seats == len(votes):
        return [1] * len(votes)
    divisor = 1.0 * sum(votes) / seats
    decs, lower = zip(*[modf(1.0 * v / divisor) for v in votes])
    quotients = [d + l for d, l in zip(decs, lower)]
    geo_means = [sqrt(ceil(q) * floor(q)) for q in quotients]
    assigned = [ceil(q) if q >= g else floor(q) for q, g in zip(quotients, geo_means)]
    unallocated = int(seats - sum(assigned))
    if unallocated > 0:
        # divisors that would add another seat to each group
        geo_means_next = [sqrt(ceil(q + 1) * floor(q + 1)) for q in quotients]
        diffs = [
            1.0 * vote / max(gn, 1) if q >= g else 1.0 * vote / max(g, 1)
            for vote, q, g, gn in zip(votes, quotients, geo_means, geo_means_next)
        ]
        # argsort
        divs = [i[0] for i in sorted(enumerate(diffs), key=itemgetter(1))][::-1]
        for k in range(unallocated):
            assigned[divs[k]] += 1
    elif unallocated < 0:
        unallocated = abs(unallocated)
        # divisors that would subtract a seat from each group
        geo_means_next = [sqrt(ceil(q - 1) * floor(q - 1)) for q in quotients]
        diffs = [
            1.0 * vote / max(gn, 1) if q < g else 1.0 * vote / max(g, 1)
            for vote, q, g, gn in zip(votes, quotients, geo_means, geo_means_next)
        ]
        # sort fix to prevent allocations to be zero to any one group
        diffs = [float("inf") if d < divisor else d for d in diffs]
        # argsort
        divs = [i[0] for i in sorted(enumerate(diffs), key=itemgetter(1))]
        for k in range(unallocated):
            assigned[divs[k]] -= 1
    return assigned


def jefferson(votes, seats):
    """Apportion seats using the Jefferson method.

    Known also as the D'Hondt method or Hagenbach-Bischoff method.

    :param list votes: a list of vote counts
    :param int seats: the number of seats to apportion
    """
    allocated = [0] * len(votes)
    while sum(allocated) < seats:
        quotients = [1.0 * vote / (allocated[idx] + 1) for idx, vote in enumerate(votes)]
        idx_max = quotients.index(max(quotients))
        allocated[idx_max] += 1
    return allocated


def sainte_lague(votes, seats):
    """Apportion seats using the Sainte-Lague method.

    Identical to the Webster method.

    :param list votes: a list of vote counts
    :param int seats: the number of seats to apportion
    """
    return webster(votes, seats)


def vinton(votes, seats):
    """Apportion seats using the Vinton method.

    Identical to the Hamilton method.

    :param list votes: a list of vote counts
    :param int seats: the number of seats to apportion
    """
    return hamilton(votes, seats)


def webster(votes, seats):
    """Apportion seats using the Webster method.

    Known also as the Sainte-Lague method.

    :param list votes: a list of vote counts
    :param int seats: the number of seats to apportion
    """
    divisor = 1.0 * sum(votes) / seats
    decs, lower = zip(*[modf(1.0 * v / divisor) for v in votes])
    lower = [int(l) for l in lower]
    assigned = [round(l + d) for l, d in zip(lower, decs)]
    unallocated = int(seats - sum(assigned))
    if unallocated > 0:
        # divisors that would add another seat to each group
        diffs = [
            1.0 * vote / (i + 1.5) if dec >= 0.5 else 1.0 * vote / (i + 0.5) for i, dec, vote in zip(lower, decs, votes)
        ]
        # argsort
        divs = [i[0] for i in sorted(enumerate(diffs), key=itemgetter(1))][::-1]
        for k in range(unallocated):
            assigned[divs[k]] += 1
    elif unallocated < 0:
        overallocated = abs(unallocated)
        # divisors that would subtract a seat from each group
        diffs = [
            1.0 * vote / (i + 0.5) if dec >= 0.5 else 1.0 * vote / (i - 0.5) for i, dec, vote in zip(lower, decs, votes)
        ]
        # argsort
        divs = [i[0] for i in sorted(enumerate(diffs), key=itemgetter(1))]
        # deallocate seats without bringing seat allocation below zero
        div_idx = 0
        while overallocated > 0:
            if assigned[divs[div_idx]] > 0:
                assigned[divs[div_idx]] -= 1
                overallocated -= 1
            else:
                div_idx += 1
    return assigned
