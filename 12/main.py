# enemies = "Dracula"

# def increase_enemies():
#     enemies = "Frankenstein"
#     print(f"enemies in local scope: {enemies}")
    
# increase_enemies()
# print(f"enemies in global scope: {enemies}")

## there is no block scope in PY, so variables delcared in if, while etc is available to the outside, but not in functions, functions counts as separate local scopes. if you want to modify global variable in local scope, add line global before the variable. try to avoid since error prone. 

enemies = "Dracula"

def increase_enemies():
    global enemies
    enemies = "Frankenstein"
    print(f"enemies in local scope: {enemies}")
    
increase_enemies()
print(f"enemies in global scope: {enemies}")