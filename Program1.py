import random

n = random.randint(1,99)

guess = int(input("Enter an number between 1 and 99:"))
print(n)
while (n!=guess):
    if guess < n:
        print("Your guess is too low")
        guess = int(input("Enter an number between 1 and 99:"))
    elif guess > n:
        print("Your guess is too high")
        guess = int(input("Enter an number between 1 and 99:"))
    else:
        print("You guessed it!")
        break
