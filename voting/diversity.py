"""Measures of diversity."""
from math import exp
from math import log

from voting.util import normalize


def berger_parker(groups):
    r"""Calculate the Berger-Parker index.

    .. math::

        max(p_i)

    :param list group: a list of integers representing populations of groups
    """
    groups = normalize(groups)
    return max(groups)


def general(groups, q=1):
    r"""Calculate the general diversity index.

    .. math::

        \left( \sum_{i=1}^n p_i^q \right) ^ {1/(1-q)}

    :param list groups: a list of integers representing populations of groups
    :param float q: weight value
    """
    if q == 1:
        return exp(shannon(groups))
    groups = normalize(groups)
    return sum([g ** q for g in groups]) ** (1.0 / (1 - q))


def gini_simpson(groups):
    r"""Calculate the Gini-Simpson index.

    .. math::

        1 - \sum_{i=1}^n p_i^2

    :param list group: a list of integers representing populations of groups
    """
    return 1 - simpson(groups)


def golosov(groups):
    r"""Calculate the effective number of parties using Golosov.

    .. math::

        \sum_{i=1}^n \frac{p_i}{p_i + p_1^2 - p_i^2}

    where :math:`p_1` is the largest proportion.

    :param list group: a list of integers representing populations of a group
    """
    groups = normalize(groups)
    p1 = max(groups)
    return sum([g / (g + p1 ** 2 - g ** 2) for g in groups])


def inverse_simpson(groups):
    r"""Calculate the Inverse-Simpson index.

    .. math::

        \frac{1}{\sum_{i=1}^n p_i^2}

    :param list group: a list of integers representing populations of groups
    """
    return 1.0 / simpson(groups)


def laakso_taagepera(groups):
    r"""Calculate the effective number of parties using Laakso-Taagepera.

    .. math::

        \frac{1}{\sum_{i=1}^n p_i^2}

    :param list group: a list of integers representing populations of groups
    """
    groups = normalize(groups)
    return 1.0 / sum([g ** 2 for g in groups])


def renyi(groups, q=0):
    r"""Calculate the Renyi entropy.

    .. math::

        \frac{1}{1-q} \ln \left( \sum_{i=1}^n p_i ^ q \right)

    :param list groups: a list of integers representing populations of groups
    :param float q: weight value

    """
    if q == 1:
        return shannon(groups)
    groups = normalize(groups)
    return 1.0 / (1 - q) * log(sum([g ** q for g in groups]))


def shannon(groups):
    r"""Calculate the Shannon index.

    .. math::

        \sum_{i=1}^n p_i \ln (p_i)

    :param list groups: a list of integers representing populations of groups
    """
    groups = normalize(groups)
    return sum([g * log(g) for g in groups])


def simpson(groups):
    r"""Calculate the Simpson index.

    .. math::

        \sum_{i=1}^n p_i^2

    :param list groups: a list of integers representing populations of groups
    """
    groups = normalize(groups)
    return sum([g ** 2 for g in groups])
