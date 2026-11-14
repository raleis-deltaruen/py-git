from seasons_of_love import Date

def test_str():
    date = Date()
    assert date.get("2000-10-10") == "thirteen million, seven hundred eight thousand, eight hundred eighty"
    assert date.get("2000-12-10") == "thirteen million, six hundred twenty thousand, nine hundred sixty"