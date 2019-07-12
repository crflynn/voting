voting
======

|travis| |rtd| |codecov| |pypi| |pyversions|


.. |travis| image:: https://img.shields.io/travis/crflynn/voting.svg
    :target: https://travis-ci.org/crflynn/voting

.. |rtd| image:: https://img.shields.io/readthedocs/voting.svg
    :target: http://voting.readthedocs.io/en/latest/

.. |codecov| image:: https://codecov.io/gh/crflynn/voting/branch/master/graphs/badge.svg
    :target: https://codecov.io/gh/crflynn/voting

.. |pypi| image:: https://img.shields.io/pypi/v/voting.svg
    :target: https://pypi.python.org/pypi/voting

.. |pyversions| image:: https://img.shields.io/pypi/pyversions/voting.svg
    :target: https://pypi.python.org/pypi/voting


A pure Python module for election quotas, voting measures, and apportionment
methods.

Installation
------------

The ``voting`` package works in Python 2.7, 3.4, 3.5, 3.6. It is available on
pypi and can be installed using pip.

.. code-block:: shell

    pip install voting

Package structure
-----------------

* voting

  * apportionment

    * adams
    * dhondt
    * hagenbach_bischoff
    * hamilton
    * huntington_hill
    * jefferson
    * sainte_lague
    * vinton
    * webster

  * diversity

    * berger_parker
    * general
    * gini_simpson
    * golosov
    * inverse_simpson
    * laakso_taagepera
    * renyi
    * shannon
    * simpson

  * proportion

    * adjusted_loosemore_hanby
    * dhondt
    * gallagher
    * grofman
    * least_square
    * lijphart
    * loosemore_hanby
    * rae
    * regression
    * rose
    * sainte_lague

  * quota

    * droop
    * hagenbach_bischoff
    * hare
    * imperiali

Examples
--------

Apportioning seats using the Huntington-Hill method.

.. code-block:: python

    from voting import apportionment


    votes = [2560, 3315, 995, 5012]
    seats = 20
    assignments = apportionment.huntington_hill(votes, seats)


Calculating the effective number of parties using Golosov's measure.

.. code-block:: python

    from voting import diversity


    parties = [750, 150, 50, 50]
    effective_parties = diversity.golosov(parties)


Measuring the disproportionality of democratic representation using the
Sainte-Lague measure.

.. code-block:: python

    from voting import proportion


    votes = [750, 150, 50, 50]
    seats = [80, 16, 2, 2]
    disproportionality = proportion.sainte_lague(votes, seats)

Determining the Droop quota

.. code-block:: python

    from voting import quota


    votes = 1000
    seats = 20
    election_quota = quota.droop(votes, seats)
