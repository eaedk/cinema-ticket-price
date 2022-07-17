from code.src.pricing import price

# pricing = _import_("src/pricing.py")
# price = pricing.price
# import code.src


class TestSolution:
    """Test if the solution is correct"""

    def test_weekDayAdultMorning(*args):
        """Test function"""

        assert price(dayOfWeek="tue", isOldOrYoung=False, isNight=False) == 30

    def test_weekDayYoungOrOldNight(*args):
        """Test function"""

        assert price(dayOfWeek="tue", isOldOrYoung=True, isNight=True) == 13

    def test_weekDayYoungOrOldMorning(*args):
        """Test function"""

        assert price(dayOfWeek="tue", isOldOrYoung=True, isNight=False) == 23

    def test_weekDayAdultNight(*args):
        """Test function"""

        assert price(dayOfWeek="tue", isOldOrYoung=False, isNight=True) == 20

    def test_weekendAdultMorning(*args):
        """Test function"""

        assert price(dayOfWeek="fri", isOldOrYoung=False, isNight=False) == 25
        assert price(dayOfWeek="sat", isOldOrYoung=False, isNight=False) == 25
        assert price(dayOfWeek="sun", isOldOrYoung=False, isNight=False) == 25

    def test_weekendAdultNight(*args):
        """Test function"""

        assert price(dayOfWeek="fri", isOldOrYoung=False, isNight=True) == 15
        assert price(dayOfWeek="sat", isOldOrYoung=False, isNight=True) == 15
        assert price(dayOfWeek="sun", isOldOrYoung=False, isNight=True) == 15
