import datetime
from testbook import testbook
import pytest


# @testbook("nb.ipynb", execute=True)
# def test_print(tb, capsys):
#     say_hello = tb.ref("say_hello")
#     say_hello()
#     captured = capsys.readouterr()
#     assert captured.out == "Hello!"


@testbook("nb.ipynb", execute=True)
def test_value(tb):
    # with pytest.deprecated_call():
    value = tb.ref("value")
    assert value() == 0
