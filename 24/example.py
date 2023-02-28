# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# with open('my_file.txt') as file:
#     contents = file.read()
#     print(contents)

# This will overwrite anything you have in your file
# with open('my_file.txt', mode="w") as file:
#     file.write('New New New')

# this will append to anything you already have written
# with open('my_file.txt', mode="a") as file:
#     file.write('\nNew Text, appended on the old text')

# IF you're trying to open a file that does not exist, Python will create it for you. will only work in W mode.
# with open('my_new_file.txt', mode="w") as file:
#     file.write('A WHOLE NEW FILE')
