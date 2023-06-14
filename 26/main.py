student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

import pandas

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}'
nato_dataFrame = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row.letter: row.code for (index, row) in nato_dataFrame.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

is_on = True

while is_on:
    user_input = input('What word do you want to translate? Type "Exit" to quit. ').split()

    if user_input[0].upper() == 'EXIT':
        is_on = False
        break

    if len(user_input) > 1:
        print('Only one word at a time.')
        break

    user_input_clean = [x.upper() for x in user_input[0]]

    code_word = [value for letter in user_input_clean for (key, value) in nato_dict.items() if key in letter]
    print(code_word)
