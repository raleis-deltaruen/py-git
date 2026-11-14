import random
   

def main():
    n = -1
    while True:
        try:
            while 1 > n or n > 3:
                n = int(input("Level: "))
            generate_integer(n)
        except ValueError:
            print("must be a number")

def generate_integer(level):            
    level_min = 0
    level_max = 9
    if level == 2:
        level_min = 10
        level_max = 99
    elif level == 3:
        level_min = 100
        level_max = 999


    count = 0
    score = 10

    while count != score:
        number_1 = random.randint(level_min, level_max)
        number_2 = random.randint(level_min, level_max)
        answer = number_1 + number_2
        user_answer = "10000"
        count_wrong = 0
        while not user_answer.isdigit() or int(user_answer) != answer:
            count_wrong += 1
            if count_wrong > 1:
                print("EEE")
                if count_wrong == 4:
                    score -= 1
                    print(f"{number_1} + {number_2} = {answer}" )
                    break
            user_answer = input(f"what's {number_1} + {number_2}? ")

        if int(user_answer) == answer:
            count += 1
    print(score)        
    exit()     

if __name__ == "__main__":
    main()