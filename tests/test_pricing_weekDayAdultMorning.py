from code.src.pricing import price


class TestSolution:
    """Test if the solution is correct"""

    def test_weekDayAdultMorning(*args):
        """Test function"""

        assert price(dayOfWeek="tue", isOldOrYoung=False, isNight=False) == 30
