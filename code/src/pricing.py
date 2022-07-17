def price(dayOfWeek, isOldOrYoung=False, isNight=False):
    """Price the ticket according to the parameters.

    Parameters
    ----------
    dayOfWeek : str
        3 letters that encode the Day of the week.
    isOldOrYoung : boolean
        Age segmentation parameter, True if the client is young or old, False otherwise. Default: False.
    isNight : boolean
        Time segmentation parameter, True for a night session, False otherwise. Default: False.

    Returns
    -------
    price : int
        price of the ticket calculated.

    """

    weekendDays = [
        "fri",
        "sat",
        "sun",
    ]
    normal_price = 30
    weekendDiscount = -5
    oldYoungDiscount = -7
    morningDiscount = -10

    price = normal_price

    # week day
    if dayOfWeek.lower() in weekendDays:
        price += weekendDiscount
    if isNight:
        price += morningDiscount
    if isOldOrYoung:
        price += oldYoungDiscount

    return price
