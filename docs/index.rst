clashroyale.py
==============

Installation
------------

**Python 3.8 or higher is required.**

To install the stable version, do the following:

.. code-block:: sh

    # Unix / macOS
    python3 -m pip install "clashroyale.py"

    # Windows
    py -m pip install "clashroyale.py"

To install the development version, do the following:

.. code-block:: sh

    $ git clone https://github.com/Ombucha/clashroyale.py

Make sure you have the latest version of Python installed, or if you prefer, a Python version of 3.8 or greater.

If you have any other issues feel free to search for duplicates and then create a new issue on GitHub with as much detail as possible. Include the output in your terminal, your OS details and Python version.


Client
------

.. autoclass:: clashroyale.Client
    :members:


Models
------

.. autoclass:: clashroyale.ClashRoyaleObject
    :members:

.. autoclass:: clashroyale.ClanLog
    :members:

.. autoclass:: clashroyale.ClanMemberList
    :members:

.. autoclass:: clashroyale.ClanList
    :members:

.. autoclass:: clashroyale.BattleLog
    :members:

.. autoclass:: clashroyale.TournamentList
    :members:

.. autoclass:: clashroyale.ChallengeList
    :members:


Exceptions
----------

.. autoclass:: clashroyale.ClashRoyaleException
    :members:

.. autoclass:: clashroyale.ForbiddenError
    :members:

.. autoclass:: clashroyale.MaintenanceError
    :members:

.. autoclass:: clashroyale.RateLimitError
    :members:

.. autoclass:: clashroyale.UncallableError
    :members:

.. autoclass:: clashroyale.UnknownError
    :members:
