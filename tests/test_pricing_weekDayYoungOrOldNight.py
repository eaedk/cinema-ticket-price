from code.src.pricing import price


class TestSolution:
    """Test if the solution is correct"""

    def test_weekDayYoungOrOldNight(*args):
        """Test function"""

        assert price(dayOfWeek="tue", isOldOrYoung=True, isNight=True) == 13
