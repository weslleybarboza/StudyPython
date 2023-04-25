alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
len(alphabet)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# text = 'hfxf'

# def encrypt(text, shift):
#     new_text = ""
#     for l in text:
#         new_index = alphabet.index(l) + shift
#         new_text += alphabet[new_index]
#     print(f'The encoded text is {new_text}.')

# def decrypt(text, shift):
#     new_text = ""
#     for l in text:
#         new_index = alphabet.index(l) - shift
#         new_text += alphabet[new_index]
#     print(f'The decode text is {new_text}.')

def caesar(direction, text, shift):
    new_text = ""
    if direction == 'decode':
        shift *= -1
    for l in text:
        new_index = alphabet.index(l) + shift
        new_text += alphabet[new_index]
    print(f'The {direction}d text is {new_text}.')    

caesar(direction, text, shift)

# if direction == 'encode':
#     encrypt(text,shift)
# else:
#     decrypt(text, shift)