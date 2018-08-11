from cryptocmp import decorators


@decorators.extract_data
@decorators.response_error_raise
@decorators.get('data/histominute')
def get(
        from_symbol,
        to_symbol,
        try_conversion=None,
        exchange=None,
        aggregate=None,
        limit=None,
        to_timestamp=None,
        extra_params=None,
        sign=None,
):
    """
    Get open, high, low, close, volumefrom and volumeto from the each minute
    historical data.

    This data is only stored for 7 days, if you need more, use the hourly or
    daily path.

    It uses BTC conversion if data is not available because the coin is not
    trading in the specified currency.

    :param try_conversion:
        If set to false, it will try to get only direct trading values
    :param from_symbol:
        REQUIRED The cryptocurrency symbol of interest
        [Max character length: 10]
    :param to_symbol:
        REQUIRED The currency symbol to convert into
        [Max character length: 10]
    :param exchange:
        The exchange to obtain data from
        (CryptoCompare aggregated average - CCCAGG - by default)
        [Max character length: 30]
    :param aggregate:
        Time period to aggregate the data over (in minutes)
    :param limit:
        The number of data points to return. It is more than 1
    :param to_timestamp:
        Last unix timestamp to return data for.
    :param extra_params:
        The name of your application
        (recommended to send it) [Max character length: 2000]
    :param sign:
        If set to true, the server will sign the requests
        (by default CryptoCompare doesn't sign them),
        this is useful for usage in smart contracts
    :return:
        OHLCV price data from each minute of the CryptoCompare historical data
    """

    # use limit-1 because it seems api interprets it as the last index
    # even though they described it as "The number of data points to return"
    return {
        'tryConversion': try_conversion,
        'fsym': from_symbol,
        'tsym': to_symbol,
        'e': exchange,
        'aggregate': aggregate,
        'limit': limit-1,
        'toTs': to_timestamp,
        'extraParams': extra_params,
        'sign': sign,
    }
