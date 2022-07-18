from code.src.pricing import price

# pricing = _import_("src/pricing.py")
# price = pricing.price
# import code.src


class TestSolution:
    """Test if the solution is correct"""

    def test_weekendAdultNight(*args):
        """Test function"""

        assert price(dayOfWeek="fri", isOldOrYoung=False, isNight=True) == 15
        assert price(dayOfWeek="sat", isOldOrYoung=False, isNight=True) == 15
        assert price(dayOfWeek="sun", isOldOrYoung=False, isNight=True) == 15
