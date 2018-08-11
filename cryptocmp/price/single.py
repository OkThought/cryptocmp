from typing import Sequence

from cryptocmp import decorators


@decorators.extract_data
@decorators.response_error_raise
@decorators.get('data/price')
def get(
        from_symbol,
        to_symbols,
        try_conversion=None,
        exchange=None,
        extra_params=None,
        sign=None,
):
    """Get the current price of any crypto-currency in any other currency.

    If the crypto does not trade directly into the toSymbol requested, BTC will
    be used for conversion.
    If the opposite pair trades CryptoCompare inverts it (eg.: BTC-XMR)

    :param try_conversion:
        If set to false, it will try to get only direct trading values
    :param from_symbol:
        REQUIRED The crypto-currency symbol of interest
        [Max character length: 10]
    :param to_symbols:
        List of crypto-currency symbols to convert into
    :param exchange:
        The exchange to obtain data from
        (CryptoCompare aggregated average - CCCAGG - by default)
        [Max character length: 30]
    :param extra_params:
        The name of your application
        (recommended to send it) [Max character length: 2000]
    :param sign:
        If set to true, the server will sign the requests
        (by default CryptoCompare doesn't sign them),
        this is useful for usage in smart contracts
    :return:
        Dictionary of prices with appropriate currency symbols as keys.

        Example:

        cryptocmp.price.single.get('BTC', ('USD','JPY','EUR'))

        {
            'USD': 6114.94,

            'JPY': 679420.45,

            'EUR': 5373.64,
        }

    """

    if isinstance(to_symbols, Sequence):
        to_symbols = ','.join(to_symbols)

    return {
        'tryConversion': try_conversion,
        'fsym': from_symbol,
        'tsyms': to_symbols,
        'e': exchange,
        'extraParams': extra_params,
        'sign': sign,
    }
