cryptocmp
=========

.. image:: https://img.shields.io/pypi/v/cryptocmp.svg
        :target: https://pypi.python.org/pypi/cryptocmp

.. image:: https://img.shields.io/travis/OkThought/cryptocmp.svg
        :target: https://travis-ci.org/OkThought/cryptocmp

.. image:: https://readthedocs.org/projects/cryptocmp/badge/?version=latest
        :target: https://cryptocmp.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/OkThought/cryptocmp/shield.svg
     :target: https://pyup.io/repos/github/OkThought/cryptocmp/
     :alt: Updates


Python wrapper for `CryptoCompare API`_

Description
-----------

``cryptocmp`` provides to the `CryptoCompare API`_ in two ways:

-  Straight wrappers of the API calls in ``cryptocmp.api`` package.
-  A more user friendly mapping to these wrappers in object-oriented
   style via the following classes:

   -  ``cryptocmp.coin.Coin`` represents a crypto coin.

Installation
------------

::

   pip3 install cryptocmp

or this can also work if you have only python3 installed (the symlink
``pip`` pointing to ``pip3`` is created)

::

   pip install cryptocmp

Usage
-----

Examples
~~~~~~~~

In object-oriented style:

-  Get a set of all available crypto coins:

   >>> from cryptocmp.coin import Coin
   >>> Coin.all()
   {'EOSDAC', 'GAP', 'ARN', 'SERA', 'ICASH', 'STAR*', 'AC3', ...}


-  Get a current price of BTC in USD:

   >>> from cryptocmp.coin import Coin
   >>> bitcoin = Coin('BTC')
   >>> bitcoin.price('USD')
   6318.35``

-  Get a current price of BTC in USD, EUR and GBP at the same time
   (produces single API call under the hood):

   >>> from cryptocmp.coin import Coin
   >>> bitcoin = Coin('BTC')
   >>> bitcoin.price(('USD', 'EUR', 'GBP'))
   {'USD': 6316.17, 'EUR': 5540.34, 'GBP': 4977.23}``

-  Get last 2 candles of BTC/USD daily historical data::

    >>> CoinPair('BTC', 'USD').price_history(points_num=2)
    [
        {
            'time': 1534291200,
            'close': 6274.22,
            'high': 6620.07,
            'low': 6193.63,
            'open': 6199.63,
            'volumefrom': 132926.33,
            'volumeto': 852103141.83
        },
        {
            'time': 1534377600,
            'close': 6439.39,
            'high': 6439.39,
            'low': 6217.33,
            'open': 6274.22,
            'volumefrom': 24013.18,
            'volumeto': 152446768.26
        }
    ]

Credit
------

Thanks to `CryptoCompare`_ for providing this service and building a
nice community around everything crypto related.

Project was partially patched with files generated by `Cookiecutter`_
using `cookiecutter-pypackage`_ project template. Thanks to `Audrey Roy
Greenfeld`_ and contributors who made python package creation so easy.

.. _CryptoCompare API: https://min-api.cryptocompare.com/
.. _CryptoCompare: https://www.cryptocompare.com/
.. _Cookiecutter: https://github.com/audreyr/cookiecutter-pypackage
.. _cookiecutter-pypackage: https://github.com/audreyr/cookiecutter-pypackage
.. _Audrey Roy Greenfeld: https://github.com/audreyr
