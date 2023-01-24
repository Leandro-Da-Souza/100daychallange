import operator
from art import logo

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

is_running = True

# def encrypt(plain_text: str, shift_amount: int):
#     encoded_text = ""
#     for i in plain_text:
#         index = (alphabet.index(i) + shift_amount) % len(alphabet)
#         encoded_text += alphabet[index]
    
#     return encoded_text

# def decrypt(cipher_text: str, shift_amount: int):
#     decoded_text = ""
#     for i in cipher_text:
#         index = (alphabet.index(i) - shift_amount + len(alphabet)) % len(alphabet)
#         decoded_text += alphabet[index]

#     return decoded_text

def caesar(text: str, shift: int, direction: str):
    new_text = ""
    ops = {
        'decode': operator.sub,
        'encode': operator.add
    }
    if direction.lower() == 'decode':
        shift = shift + len(alphabet)

    for char in text:
        if char in alphabet:
            index = (ops[direction.lower()](alphabet.index(char), shift)) % len(alphabet)
            new_text += alphabet[index]
        else:
            new_text += char
    return new_text

while is_running == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    print(f"Here's your {direction}d result: {caesar(text=text, shift=shift, direction=direction)}")

    end_program = input("Type 'yes' if you want to go again. Otherwise type 'no'. ")
    
    if not (end_program.lower() == 'yes'):
        print('Good bye.')
        is_running = False