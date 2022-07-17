def price(dayOfWeek, isOldOrYoung=False, isNight=False):
    """Price the ticket according to the parameters.

    Parameters
    ----------
    dayOfWeek : str
        3 letters that encode the Day of the week.
    isOldOrYoung : boolean
        Description of parameter `x`.
    isNight : type
        Description of parameter `x`.

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
