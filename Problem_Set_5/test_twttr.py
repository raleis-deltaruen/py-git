from twttr import vowel_removal

def test_vowel_removal():
    assert "hll" == vowel_removal("hello") 
    assert vowel_removal("1") == "1"
    assert vowel_removal("qwrtypsdfghjklzxcvbnm") == "qwrtypsdfghjklzxcvbnm"
    