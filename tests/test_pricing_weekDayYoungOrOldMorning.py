from code.src.pricing import price

# pricing = _import_("src/pricing.py")
# price = pricing.price
# import code.src


class TestSolution:
    """Test if the solution is correct"""

    def test_weekDayYoungOrOldMorning(*args):
        """Test function"""

        assert price(dayOfWeek="tue", isOldOrYoung=True, isNight=False) == 23
