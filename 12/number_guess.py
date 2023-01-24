import random
from art import logo

difficulty = {
    "easy": 8,
    "hard": 5
}

game_over = False
random_number = random.randrange(1, 10)
print('Welcome to the Number Guessing Game!')
print("I'm thinking of a number between 1 and 100.")
user_difficulty = difficulty[input("Choose difficulty: 'hard' or 'easy'. ").lower()]

while game_over == False:
    print(logo)
    user_guess = int(input('Guess the number... '))

    print(f"You guessed {user_guess}.")
    if user_guess == random_number:
        print('Congrats, you guessed it!')
        print(f"Your guess: {user_guess}, AI guess: {random_number}")
        game_over = True
    elif user_difficulty == 0:
        print("You've run out of guesses, you die...")
        game_over = True
    elif random_number > user_guess:
        print('Too low...')
        user_difficulty -= 1
        print(f"You have {user_difficulty} left...")
    else:
        print('Too high...')
        user_difficulty -= 1
        print(f"You have {user_difficulty} left...")
