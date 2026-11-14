import random
while True:
    try:
        n = -1
        while n < 1:
            n = int(input("input the top number: "))
        x = random.randint(1, n)
        user_guess = -1
        while user_guess != x:
            user_guess = int(input(f"guess the number between 1 and {n}: "))
            if user_guess < x:
                print("Too small!")
            elif user_guess > x:
                print("Too large!")
            elif user_guess == x:
                print("Just right!")
        break
    except ValueError:
        print("must be a positive number")