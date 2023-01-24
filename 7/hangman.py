import random

random_words = [
    # 'Leprosy',
    # 'Frankenstein',
    # 'Dracula',
    # 'Beelzebub',
    # 'Cocoon',
    # 'Butterfly',
    # 'Dragonfly',
    # 'Stingbeetle',
    # 'Rhinocerous',
    # 'Sunshine',
    # 'Waterfall',
    'Swans'
]

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


number_of_guesses = 0
game_over = False
user_guesses = []

selected_word = "".join(random.sample(random_words, 1))
selected_output = ""

for n in selected_word:
    selected_output += '_'

selected_output = "".join(selected_output)
print('Welcome to Hangman, where you might hang a man.')
# print(selected_output)

while not game_over:
    print(f"Number of guesses: {number_of_guesses}")
    print(HANGMANPICS[number_of_guesses])
    print("".join(selected_output))

    guess = str(input('Which letter do you choose? '))
    user_guesses.append(guess)
    selected_word = list(selected_word)
    selected_output = list(selected_output)
    correct_guess = False

    if(number_of_guesses == 6):
        print('You are finished...')
        game_over = True
        break

    print(f"You've guessed {''.join(user_guesses)}")

    for y in selected_word:
        if y.lower() == guess.lower():
            selected_output[selected_word.index(y)] = y
            correct_guess = True
            
    if not correct_guess: number_of_guesses += 1

    check = all(word in selected_output for word in selected_word)

    if check is True:
        print('You win!')
        print(f"You've guessed {''.join(user_guesses)}")
        game_over = True
        break
    
 