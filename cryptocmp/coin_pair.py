from warnings import warn

import cryptocmp.api.price.single
from cryptocmp.coin import Coin
import datetime


MINUTE = datetime.timedelta(minutes=1)
HOUR = datetime.timedelta(hours=1)
DAY = datetime.timedelta(days=1)

_time_units = {
    'minute': MINUTE,
    'hour': HOUR,
    'day': DAY,
}


def _price_history_getter(time_unit):
    getter = None
    if time_unit is DAY:
        import cryptocmp.api.historical.price.days
        getter = cryptocmp.api.historical.price.days.get
    elif time_unit is HOUR:
        import cryptocmp.api.historical.price.hours
        getter = cryptocmp.api.historical.price.hours.get
    elif time_unit is MINUTE:
        import cryptocmp.api.historical.price.minutes
        getter = cryptocmp.api.historical.price.minutes.get
    return getter


def _coin(coin_or_symbol):
    if isinstance(coin_or_symbol, str):
        coin = Coin(coin_or_symbol)
    elif isinstance(coin_or_symbol, Coin):
        coin = coin_or_symbol
    else:
        raise TypeError
    return coin


class CoinPair:
    """
    Provides access to CryptoCompare API in OOP style. Intended to be more
    user friendly and straightforward.
    """

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

    def price_history(self, time_from=None, time_to=None, time_unit=None,
                      limit=None, exchange=None, extra_params=None, sign=None):
        aggregate = None
        if time_unit is None:
            time_unit = DAY
        elif isinstance(time_unit, datetime.timedelta):
            if time_unit < MINUTE:
                warn('Time unit less than 1 minute is currently not supported.'
                     'Using the minimum time unit of 1 minute instead.')
                time_unit = MINUTE
            elif time_unit < HOUR:
                aggregate=time_unit.total_seconds() / 60
                time_unit = MINUTE
            elif time_unit < DAY:
                aggregate=time_unit.total_seconds() / 3600
                time_unit = HOUR
            else:
                aggregate=time_unit.days
                time_unit = DAY
        elif isinstance(time_unit, str):
            try:
                time_unit = _time_units[time_unit]
            except KeyError:
                raise ValueError('Unknown time_unit: %s' % time_unit)
        else:
            raise TypeError('Unsupported type of time_unit: %s' %
                            type(time_unit))

        if time_to is None:
            time_to = datetime.datetime.now()

        if time_from is not None:
            if limit is not None:
                raise RuntimeError('time_from and limit must not be specified'
                                   'together')
            time_period = time_to - time_from
            limit = time_period // time_unit

        price_history_getter = _price_history_getter(time_unit)

        return price_history_getter(
            coin=self.first.symbol,
            in_coin=self.second.symbol,
            to_timestamp=time_to.timestamp(),
            limit=limit,
            exchange=exchange,
            aggregate=aggregate,
            extra_params=extra_params,
            sign=sign,
        )

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
