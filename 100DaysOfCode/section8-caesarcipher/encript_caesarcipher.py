import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

restart = True

def caesar(direction, text, shift):
    new_text = ""
    if direction == 'decode':
        shift *= -1
    for l in text:       
        if l in alphabet:
            new_index = alphabet.index(l) + shift
            word = alphabet[new_index]
        else:
            word = l
        new_text += word
    print(f'The {direction}d text is "{new_text}".')    

while restart:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(direction, text, shift)

    chose = input("\nDo you want to restart the cipher program? Y or N. ").lower()

    if chose == 'n':
        restart = False
        print("Goodbye")
