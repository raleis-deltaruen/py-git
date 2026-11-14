from bank import value
def test_value():
    assert "$0" == value("Hello")
    assert "$0" == value("hello")
    assert "$20" == value("Hey")
    assert "$20" == value("hey")
    assert "$20" == value("Hi")
    assert "$20" == value("hi")
    assert "$100" == value("greetings")