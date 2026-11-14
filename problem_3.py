def vowel_removal(x: str) -> str:
    result = x
    vowels = ["a", "u", "o", "i", "e"]
    for vowel in vowels:
        result = result.replace(vowel, "").replace(vowel.upper(), "")
    return result
assert "ppl" == vowel_removal("apple")
assert "PPL" == vowel_removal("APPLE")
assert "gmtry" == vowel_removal("geometry")
print("success")