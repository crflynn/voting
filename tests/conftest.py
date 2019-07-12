"""Fixtures."""
import pytest

from voting.apportionment import adams
from voting.apportionment import dhondt
from voting.apportionment import hagenbach_bischoff
from voting.apportionment import hamilton
from voting.apportionment import huntington_hill
from voting.apportionment import jefferson
from voting.apportionment import sainte_lague
from voting.apportionment import vinton
from voting.apportionment import webster
from voting.diversity import berger_parker
from voting.diversity import general
from voting.diversity import gini_simpson
from voting.diversity import golosov
from voting.diversity import inverse_simpson
from voting.diversity import laakso_taagepera
from voting.diversity import renyi
from voting.diversity import shannon
from voting.diversity import simpson
from voting.proportion import adjusted_loosemore_hanby
from voting.proportion import dhondt as dh  # dupe of apportionment
from voting.proportion import gallagher
from voting.proportion import grofman
from voting.proportion import least_square
from voting.proportion import lijphart
from voting.proportion import loosemore_hanby
from voting.proportion import rae
from voting.proportion import regression
from voting.proportion import rose
from voting.proportion import sainte_lague as sl  # dupe of apportionment
from voting.quota import droop
from voting.quota import hagenbach_bischoff as hb  # dupe of apportionment
from voting.quota import hare
from voting.quota import imperiali


@pytest.fixture(params=[[2560, 3315, 995, 5012]])
def votes(request):
    return request.param


@pytest.fixture(params=[20])
def seats(request):
    return request.param


@pytest.fixture(params=list(range(4, 50)))
def seats_val(request):
    return request.param


@pytest.fixture(params=[[5, 6, 7, 8]])
def seats_list(request):
    return request.param


@pytest.fixture(
    params=[adams, dhondt, hagenbach_bischoff, hamilton, huntington_hill, jefferson, sainte_lague, vinton, webster]
)
def apportionment_method(request):
    return request.param


@pytest.fixture(params=[droop, hb, hare, imperiali])
def quota_method(request):
    return request.param


@pytest.fixture(params=[droop, hb, hare, imperiali])
def quota_method(request):
    return request.param


@pytest.fixture(
    params=[
        adjusted_loosemore_hanby,
        dh,
        gallagher,
        grofman,
        least_square,
        lijphart,
        loosemore_hanby,
        rae,
        regression,
        rose,
        sl,
    ]
)
def proportion_method(request):
    return request.param


@pytest.fixture(params=["seats", "votes", "something_else"])
def parties(request):
    return request.param


@pytest.fixture(
    params=[berger_parker, general, gini_simpson, golosov, inverse_simpson, laakso_taagepera, renyi, shannon, simpson]
)
def diversity_method(request):
    return request.param


@pytest.fixture(params=[0, 0.5, 1, 2])
def q(request):
    return request.param
