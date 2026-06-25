import random

def guess_number():
    number = random.randint(1, 10)
    attempt = 0
    max_attempt = 3
    
    print("Enter a number between 1 to 10 (or type quit to exit)\n")
    while True:
        user_input = input("Enter a number between 1 to 10:").strip().lower()
        if user_input == "quit":
            print("Thanks for playing..")
            break
        if not user_input.isdigit():
            print("Please enter a valid number")
            break
        guess = int(user_input)
        attempt += 1
        if attempt < max_attempt:
            print(f"Attempt {attempt}")
            if guess < number:
                print("Too low")
            elif guess > number:
                print("Too high")
            else:
                print(f"You guessed correct {number}")
                break
        else:
            print(f"Attempt exceeded..")
            break




guess_number()