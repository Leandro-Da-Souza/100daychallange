from art import logo, vs
from game_data import data
import random

def get_vs(data: list):
    contenders = random.choices(data, k=2)
    return contenders

def compare(contenders: dict, guess: slice):
    user_choice = contenders[guess]
    # vs_choice = contenders[list({key:value for key, value in contenders.items() if key != guess})[0]]
    vs_choice = next(value for key, value in contenders.items() if key != guess)
    if user_choice['follower_count'] > vs_choice['follower_count']:
        return True
    else:
        return False

        
def game():
    print(logo)
    is_game_over = False
    user_score = 0

    while is_game_over == False:
        contenders = get_vs(data=data)
        contenders_dict = {
            'A': contenders[0],
            'B': contenders[1]
        }

        while (contenders_dict['A'] == contenders_dict['B']):
            contenders_dict['B'] = random.choice(data)

        print(f"Compare A: {contenders[0]['name']}, a {contenders[0]['description']} from {contenders[0]['country']}.")
        print(vs)
        print(f"Against B: {contenders[1]['name']}, a {contenders[1]['description']} from {contenders[1]['country']}.")
        
        user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()

        while True:
            if (user_guess == 'A' or user_guess == 'B'):
                break
            else:
                print("I'm sorry, i did not understand you")
                user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()

        if(compare(contenders=contenders_dict, guess=user_guess) == True):
            print("You Win!")
            user_score +=1
            rounds +=1
            print(f"Your score: {user_score}")
        else:
            print('You Lose.')
            print(f"Final user score: {user_score}")
            is_game_over = True


game()