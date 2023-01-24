# import random
# import my_module

# random_int = random.randint(1,5)

# print(random_int)
# print(my_module.pi)

# random_float = random.random()
# print(random_float)

# random_number = round((random_int * random_float), 2)
# print(random_number)

# #Remember to use the random module
# #Hint: Remember to import the random module here at the top of the file. 🎲
	 
# #Write the rest of your code below this line 👇
# import random

# rand = random.randint(0, 1)

# if rand == 1:
#     print('Heads')
# else:
#     print('Tails')

# us_states = ['Wyoming', 'Alaska', 'Washington', 'Seattle', 'Delaware']

# for x in us_states:
#     print(x)

# print(us_states[0])
# print(us_states[-1])

# Import the random module here

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random

lucky_person = random.randint(0, len(names) - 1)

print(f"{names[lucky_person]} is going to buy the meal today!")

# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
def placeTreasure(x):
    coordinates = list(x.split('? ')[0])
    
    map[int(coordinates[1]) - 1][int(coordinates[0]) - 1] = 'X'

placeTreasure(position)
#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

