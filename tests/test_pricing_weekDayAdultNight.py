from code.src.pricing import price


class TestSolution:
    """Test if the solution is correct"""

    def test_weekDayAdultNight(*args):
        """Test function"""

        assert price(dayOfWeek="tue", isOldOrYoung=False, isNight=True) == 20
