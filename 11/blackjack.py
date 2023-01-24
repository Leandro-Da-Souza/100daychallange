import random
import sys
sys.path.append('..')

from art import logo
from clear import clear

def deal_card():
    """Return random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card

def calculate_score(cards: list):
    """Take a list and return the score calculated from the cards"""
    if (sum(cards) == 21 and len(cards) == 2):
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

def compare(user_score: int, dealer_score: int):
    if user_score == dealer_score:
        return "Draw."
    elif dealer_score == 0:
        return 'Lose, dealer has Blackjack.'
    elif user_score == 0:
        return 'Win with a Blackjack.'
    elif user_score > 21:
        return 'You went over. You lose.'
    elif dealer_score > 21:
        return 'Dealer went over. You Win.'
    elif user_score > dealer_score:
         return "You win."
    else:
        return "You lose."

def play_game():
    clear.clear()
    print(logo)

    user_cards = []
    dealer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())

    while not is_game_over: 
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Dealer's first card: {dealer_cards[0]}")

        if(user_score == 0 or dealer_score == 0 or user_score > 21):
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal.lower() == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)

    print(f"    Your cards: {user_cards}, your final score: {user_score}")
    print(f"    Dealer's cards: {dealer_cards}, dealer's final score: {dealer_score}")
    print(compare(user_score=user_score, dealer_score=dealer_score))

    if input("Do you want to play a new game of Blackjack? type 'y' or 'n'. ").lower() == 'y':
        play_game()

play_game()



