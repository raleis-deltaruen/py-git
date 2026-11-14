# check if contains - ! etc

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
        
main()
#assert is_valid("CS50")
#assert not is_valid("CS050")
#assert not is_valid("A")
#assert not is_valid("AAAAAAA")
#assert is_valid("AA!BC5")
#assert is_valid("AA BC5")
#print("success")