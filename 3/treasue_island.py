print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
first_step = input('You arrived at the island. Where do you want to go, left or right? ')

if (first_step.lower() == 'right'):
    print('You stumbled upon a goblin, the goblin slays you.')
    print('You died. Game Over.')

second_step = input('You go left and come to a ashen lake, a boat is on its way but will arrive in some time. Do you swim accross or wait for the boat? Swim or wait. ')

if (second_step.lower() == 'swim'):
    print('You start swimming, after coming halfway across the lake a giant sea serpent swallows you whole.')
    print('You Died. Game Over.')

third_step = input('You wait for the boat. After 10 minutes it arrives, you get accros and encounter three doors on the side of a volcano. Red, blue and yellow. A little witch appears and tells you: "2 of three gives doom to thee, 1 will give you all and then its done.". Which door do you go through? Red, Blue, or Yellow? ')

if (third_step.lower() == 'yellow'):
    print('You Won!\nCongratulations!\nGame Over.')
else:
    print('You failed and the world is doomed. Try again?')