# Old way of iterating through a list to create a new one with a for loop
import random

numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

print(numbers)
print(new_list)

# with list comprehension (new_list = [new_item for item in list]), works with any python sequence (range, list,
# dict, string)
new_list2 = [n + 2 for n in numbers]
print(new_list2)

name = 'Leandro'
new_list3 = [letter for letter in name]
print(new_list3)

new_list4 = [n * 2 for n in range(1, 5)]
print(new_list4)

# conditional list comprehension
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

short_names = [name for name in names if len(name) < 5]
print(short_names)

all_caps = [name.upper() for name in names if len(name) > 5]
print(all_caps)

numbers4 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

# Write your 1 line code 👇 below:
squared_numbers = [n * n for n in numbers4]

# Write your code 👆 above:

print(squared_numbers)

numbers6 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above

# Write your 1 line code 👇 below:
result = [n for n in numbers6 if n % 2 == 0]

# Write your code 👆 above:

print(result)

file1 = [l.strip() for l in open('file1.txt', 'r').readlines()]
file2 = [l.strip() for l in open('file2.txt', 'r').readlines()]
result = [int(n) for n in file1 if n in file2]
# Write your code above 👆

print(result)

# Dictionary Comprehension === new_dict = {new_key: new_value for item in list}
# Dictionary Comprehension === new_dict = {new_key: new_value for (key,value) in dict.items()}
# Conditional Comprehension === new_dict = {new_key: new_value for (key,value) in dict.items() if test}

students_score = {name: random.randint(1, 100) for name in names}
print(students_score)

passed_students = {name: score for (name, score) in students_score.items() if score >= 60}
print(passed_students)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆
result = {word: len(word) for word in sentence.split()}
# Write your code below:
print(result)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆

# Write your code 👇 below:
weather_f = {key: ((value * 9 / 5) + 32) for (key, value) in weather_c.items()}

print(weather_f)

# Looping through dictionaries
# for (key, value) in students_score.items():
#     print(key, value)

import pandas

students2 = {
    "students": names,
    "score": [value for (key, value) in students_score.items()]
}
students_score_pandas = pandas.DataFrame(students2)

# for (key, value) in students_score_pandas.items():
#     print(value)

for (index, row) in students_score_pandas.iterrows():
    print(row.students)
    print(row.score)
