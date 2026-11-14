from jar import Jar
import pytest

def test_init():
    ...

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

    assert jar.capacity == 12
    assert jar.size == 12

def test_capacity():
    jar = Jar(7)
    assert jar.capacity == 7
def test_deposit():
    jar = Jar()
    assert jar.deposit(11) == 11
    with pytest.raises(ValueError):
        jar.deposit(13)
    with pytest.raises(ValueError):
        jar.deposit(5)

def test_withdraw():
    jar = Jar()
    jar.deposit(11)
    assert jar.withdraw(2) == 9

