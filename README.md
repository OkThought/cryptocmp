# cryptocmp
Python wrapper for [CryptoCompare API](https://min-api.cryptocompare.com/)

## Description
`cryptocmp` provides to the
[CryptoCompare API](https://min-api.cryptocompare.com/)
in two ways:

- Straight wrappers of the API calls in `cryptocmp.api` package.
- A more user friendly mapping to these wrappers in object-oriented
  style via the following classes:

  - `cryptocmp.coin.Coin` represents a crypto coin.

## Installation

```
pip3 install cryptocmp
```
or this can also work if you have only python3 installed
(the symlink `pip` pointing to `pip3` is created)
```
pip install cryptocmp
```

## Usage

### Examples

In object-oriented style:

- Get a set of all available crypto coins:
    ```
    >>> from cryptocmp.coin import Coin
    >>> Coin.all()
    {'EOSDAC', 'GAP', 'ARN', 'SERA', 'ICASH', 'STAR*', 'AC3', ...}
    ```
- Get a current price of BTC in USD:
    ```
    >>> from cryptocmp.coin import Coin
    >>> bitcoin = Coin('BTC')
    >>> bitcoin.price('USD')
    6318.35
    ```


## Credit

Thanks to [CryptoCompare](https://www.cryptocompare.com/)
for providing this service and building a nice community around
everything crypto related.
