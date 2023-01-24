# def greet():
#     print('Hello')
#     print('How are you?')
#     print('Bye!')

# greet('Sunny')

# def greet_two(name: str):
#     print(f'Hello {name}!')
#     print('How are you?')
#     print('Bye!')

# greet_two('Sunny')

# def greet_with(name: str, location: str):
#     print(f'Hello {name}!')
#     print(f'What is it like in {location}?')

# greet_with('Sunny', 'Stockholm')

#Write your code below this line 👇
# import math

# def paint_calc(height, width, cover):
#     res = math.ceil((height * width) / cover)
#     print(f"You'll need {res} cans of paint.")

# #Write your code above this line 👆
# # Define a function called paint_calc() so that the code below works.   

# # 🚨 Don't change the code below 👇
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

# def greet_with_two(name: str, location: str):
#     print(f"Hello {name}, what is it like in {location}?")

# greet_with_two(location='Nowhere', name='Jack Bauer')

#Write your code below this line 👇
def prime_checker(number):
    is_prime = True
    
    for n in range(2, number):
        if(number % n == 0):
            is_prime = False
    
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)