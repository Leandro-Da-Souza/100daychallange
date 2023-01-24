print('Welcome to the rollercoaster!')
height = int(input("What is your height in cm?\n"))
age = int(input('What is your age in years?\n'))

if height >= 120:
    print('You may ride the rollercoaster!')
    if age <= 12:
        print('That will be $5 thank you!')
    elif age <= 18:
        print('That will be $7 thank you!')
    else:
        print('That will be $12 thank you!')
else:
    print('Sorry, come back in a year!')

# number = int(input('Which number do you want to check?\n'))

# if number % 2 == 0:0
#     print('This is an even number.')
# else:
#     print('This is an odd number.')

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = round(weight / (height ** 2))
statement = f"Your BMI is {bmi}, "

if bmi > 35:
    print(statement + 'you are clinically obese.')
elif bmi > 30:
    print(statement + 'you are obese.')
elif bmi > 25:
    print(statement + 'you are slightly overweight.')
elif bmi > 18.5:
    print(statement + 'you have a normal weight.')
else:
    print(statement + 'you are underweight.')


# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year % 4 == 0 and year % 100 != 0:
    print('Leap year.')
else:
    if year % 400 == 0:
        print('Leap year.')
    else:
        print('Not leap year.')

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0

if size == 'L':
    bill = 25
elif size == 'M':
    bill = 20
elif size == 'S':
    bill = 15

if add_pepperoni == 'Y':
    if size == 'L' or size == 'M':
        bill += 3
    else:
        bill += 2

if extra_cheese == 'Y':
    bill += 1

print(f"Your final bill is: ${bill}.")


# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

def love_calculator(iterable):
    true_count = 0
    love_count = 0
    score = '';

    for x in iterable:
        x.lower()
        
        true_count += sum(map(x.count, ['t', 'r', 'u', 'e']))
        love_count += sum(map(x.count, ['l', 'o', 'v', 'e']))

        score = f"{true_count}{love_count}"
    
    score = int(score)

    if score < 10 or score > 90:
        print(f"Your score is {score}, you go together like coke and mentos.")
    elif score >= 40 and score <= 50:
        print(f"Your score is {score}, you are alright together.")
    else:
        print(f"Your score is {score}.")

love_calculator((name1, name2))


