from code.src.pricing import price


class TestSolution:
    """Test if the solution is correct"""

    def test_weekendAdultNight(*args):
        """Test function"""

        assert price(dayOfWeek="fri", isOldOrYoung=False, isNight=True) == 15
        assert price(dayOfWeek="sat", isOldOrYoung=False, isNight=True) == 15
        assert price(dayOfWeek="sun", isOldOrYoung=False, isNight=True) == 15
