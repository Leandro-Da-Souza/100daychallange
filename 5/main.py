# fruits = ['Apples', 'Mangos', 'Lemons']

# for x in fruits:
#     print(x)
#     print(x + ' hella good!')

# # 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆


# #Write your code below this row 👇
# total_height = 0
# for x in student_heights:
#     total_height += x

# average_height = round(total_height / len(student_heights))

# print(average_height)

# # 🚨 Don't change the code below 👇
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇
# highest_score = 0
# for x in student_scores:
#     if x > highest_score:
#         highest_score = x

# print(f"The highest score in the class is: {highest_score}")

total = 0
for x in range(1, 101):
    total += x

print(total)

#Write your code below this row 👇

for x in range(1,101):
    if(x % 15 == 0):
        print('FizzBuzz')
    elif(x % 5 == 0):
        print('Buzz')
    elif(x % 3 == 0):
        print('Fizz')
    else:
        print(x)

#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

if (nr_symbols > nr_letters or nr_numbers > nr_letters
        or (nr_symbols + nr_numbers) > nr_letters):
    print('Error, initiating self destruct sequence, 3...2...1')
    quit()

selected_letters = random.sample(letters,
                                 nr_letters - (nr_symbols + nr_numbers))

selected_symbols = random.sample(symbols, nr_symbols)

selected_numbers = random.sample(numbers, nr_numbers)

password = selected_letters + selected_symbols + selected_numbers

password = "".join(random.sample(password, len(password)))

print(f"Your new password is !!! {password} !!! keep it safe...")
