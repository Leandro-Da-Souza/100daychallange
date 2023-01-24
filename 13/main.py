############DEBUGGING#####################

# Describe Problem
# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()
"""Range second step is exclusive, so if you want 20, you would have to put 21"""

# Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])
"""indexes are 0 based, so should be 0,5 not 1,6"""

# # Play Computer
# year = int(input("What's your year of birth? "))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994:
#   print("You are a Gen Z.")
"""1994 value not caught by if, edit elif to include 1994"""

# # Fix the Errors
# age = int(input("How old are you?"))
# if age > 18:
#     print("You can drive at age {age}.")
# """cast age to int, indent line in if"""

#Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)
"""word_per_page was first a comparisson, edit to make assignment"""

# #Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])