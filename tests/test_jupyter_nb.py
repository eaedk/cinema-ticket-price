# import datetime
# from testbook import testbook
# import pytest
import ipynb.fs.full.nb  as notebook

def test_func_value():
    assert notebook.value() == 10

def test_class_Number() :
    assert isinstance(notebook.Number(10), int)

def test_pandas() :
    # x = pd.DataFrame({"i": [0, 1, 2]})
    print(notebook.Number(10).df)
    assert 1 == 1