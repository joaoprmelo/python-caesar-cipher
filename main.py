alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(plain_text, shift_amount):
    cipher_password = ""       
    for letter in plain_text:
        position = alphabet.index(letter)         
        if direction == 'encode':
            new_position = position + shift_amount    
            cipher_password += alphabet[new_position]
        elif direction == 'decode':
            new_position = position - shift_amount
            cipher_password += alphabet[new_position]                        
    print(f'The encoded text is {cipher_password}')

from art import logo
print(logo)

should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    
    caesar(plain_text = text, shift_amount = shift)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n")
    if restart == 'no':
        should_end = True
        print('Goodbye')