def main():
    x = input("Input: ")
    print(vowel_removal(x))

def vowel_removal(x: str) -> str:  
    vowels = ["a", "u", "o", "i", "e"]
    for vowel in vowels:
        x = x.replace(vowel, "").replace(vowel.upper(), "")
    return x

if __name__ == "__main__":
    main()