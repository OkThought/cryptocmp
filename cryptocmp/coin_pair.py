import cryptocmp.api.price.single
from cryptocmp.coin import Coin


def _coin(coin_or_symbol):
    if isinstance(coin_or_symbol, str):
        coin = Coin(coin_or_symbol)
    elif isinstance(coin_or_symbol, Coin):
        coin = coin_or_symbol
    else:
        raise TypeError
    return coin


class CoinPair:
    def __init__(self, first, second):
        self.first = _coin(first)
        self.second = _coin(second)

    def price(self, try_conversion=None, exchange=None, extra_params=None,
              sign=None):
        """Get the current price of the first currency in the second currency.

        :param try_conversion:
            If set to false, it will try to get only direct trading values.

        :param exchange:
            The exchange to obtain data from
            (CryptoCompare aggregated average - CCCAGG - by default).
            [Max character length: 30]

        :param extra_params:
            The name of your application.
            (recommended to send it) [Max character length: 2000]

        :param sign:
            If set to true, the server will sign the requests
            (by default CryptoCompare doesn't sign them),
            this is useful for usage in smart contracts.

        :return: Current price for this pair.
        """

        price_dict = cryptocmp.api.price.single.get(
            self.first.symbol,
            self.second.symbol,
            try_conversion=try_conversion,
            exchange=exchange,
            extra_params=extra_params,
            sign=sign,
        )
        return price_dict[self.first.symbol]

    def __str__(self):
        return '%s/%s' % (self.first, self.second)

    def __getitem__(self, item):
        if isinstance(item, int):
            if item == 0:
                return self.first
            elif item == 1:
                return self.second
            else:
                raise IndexError
        raise TypeError

    def __reversed__(self):
        return CoinPair(self.second, self.first)
