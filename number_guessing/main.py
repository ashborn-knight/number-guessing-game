import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7  # You can change this number for more or fewer chances

    print("Welcome to the Number Guessing Game!")
    print("I have picked a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it correctly.\n")

    while attempts < max_attempts:
        # Ask the user for a guess
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.\n")
        elif guess > secret_number:
            print("Too high! Try again.\n")
        else:
            print(f"🎉 Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break
    else:
        # Runs only if the user didn't guess correctly
        print(f"😢 Sorry, you've used all {max_attempts} attempts.")
        print(f"The correct number was {secret_number}.")

# Run the game
number_guessing_game()
