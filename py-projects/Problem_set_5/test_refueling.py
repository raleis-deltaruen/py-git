from refueling import convert, gauge
import pytest

def test_convert():
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("cat/4")
    with pytest.raises(ValueError):
        convert("3/dog")
    with pytest.raises(TypeError):
        convert("4/3")
    with pytest.raises(ZeroDivisionError):
        convert("3/0")
    assert convert("3/4") == 0.75

def test_gauge():
    assert gauge(0.99) == "F"
    assert gauge(1) == "F"
    assert gauge(0.01) == "E"
    assert gauge(0.00) == "E"
    assert gauge(0.50) == "50%"
    assert gauge(0.75) == "75%"
    assert gauge(0.25) == "25%"
