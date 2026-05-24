import random

print("Enter your guessed number (1-100): ")
a= random.randint(1,100)

while True:
        guess = int(input())
        if guess == a:
            print("Congratulations! You guessed the number.")
            break
        elif guess < a:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")


