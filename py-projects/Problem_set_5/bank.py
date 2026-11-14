def main():
    a = input("Greet Kerman: ")
    print(value(a))
def value(greeting):
    result = greeting
    if "hello" == result.lower():
        return "$0"
    elif "h" == result[0].lower():
        return "$20"
    else: return "$100"

if __name__ == "__main__":
    main()