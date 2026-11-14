from vanity_plates import is_valid

def test_is_valid():
    assert is_valid("AAAAAA") == True
    assert is_valid("AAAAA1") == True
    assert is_valid("aaaa2") == True
    assert is_valid("aaa3") == True
    assert is_valid("aa4") == True
    assert is_valid("aa50") == True
    assert is_valid("aa560") == True
    assert is_valid("aa5670") == True

    assert is_valid("a1a123") == False
    assert is_valid("112345") == False
    assert is_valid("12345a") == False