rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

RPS = {0: ['Rock', rock], 1: ['Paper', paper], 2: ['Scissors', scissors]}

print('WELCOME! to rock, paper or scissors...')
print(
    'You will be competing with advance AI to the death, choose carefully...')

human_choice = int(
    input('What do you choose? 0 for rock, 1 for paper, 2 for scissors... '))

if (human_choice < 0 or human_choice > 2):
    print("Choose between 0 and 2 fool...")
else:
    ai_choice = random.randint(0, 2)
  
    print(f"You chose {RPS[human_choice][0]}:")
    print(RPS[human_choice][1])

    print(f"AI chose {RPS[ai_choice][0]}:")
    print(RPS[ai_choice][1])

    if human_choice == ai_choice:
        print('draw...self destruct initiated...%&@#!')
        quit()

    if human_choice == 0:
        if ai_choice == 1:
            print('You lose and also die.')
        elif ai_choice == 2:
            print('You beat AI and also get to live.')
    elif human_choice == 1:
        if ai_choice == 2:
            print('You lose and also die.')
        elif ai_choice == 0:
            print('You beat AI and also get to live.')
    elif human_choice == 2:
        if ai_choice == 0:
            print('You lose and also die.')
        elif ai_choice == 1:
            print('You beat AI and also get to live.')