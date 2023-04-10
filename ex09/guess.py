import random

secret_number = random.randint(1, 99)
guess = None
guesses = 0

print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to find out the secret number.")
print("Type 'exit' to end the game.")
print("Good luck!")

while guess != secret_number:
    guess = input("What's your guess between 1 and 99?\n>> ")
    if guess == "exit":
        print("Goodbye!")
        break
    if not guess.isdigit() or int(guess) < 1 or int (guess) > 99:
        print("Thats not a number.")
        continue
    guesses += 1
    guess = int(guess)
    if guess > secret_number:
        print("Too high!")
    elif guess < secret_number:
        print("Too low!")
    else:
        if secret_number == 42:
            print("The answer to the ultimate question of life, the universe and everything is 42.")
        if guesses == 1:
            print("Congratulations! You got it on your first try!")
        else:
            print("Congratulations, you've got it!")
            print(f"You won in {guesses} attempts!")