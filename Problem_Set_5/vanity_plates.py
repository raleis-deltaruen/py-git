def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s: str):
    if len(s) > 6 or len(s) < 2:
        return False
    if s[0].isdigit() or s[1].isdigit():
        return False
    if s.isalpha():
        return True
    
    for i in range(2,len(s)):
        if s[i].isdigit():
            return s[i:].isdigit() and s[i:].isalnum() and int(s[i]) != 0

if __name__ == "__main__":
    main()