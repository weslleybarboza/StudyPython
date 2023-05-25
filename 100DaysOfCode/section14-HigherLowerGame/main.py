# loop start


from random import choice
from game_data import data

list_used = []
def newOption ():
    '''
    Return a random new option without repeat itens usaged.
    '''
    list_option = []
    for i in data:
        list_option.append(i)

    list_available = [item for item in list_option if item not in list_used]
    
    new_option = choice(list_available)
    list_used.append(new_option)
    
    return new_option

def result(a_option, b_option, choice):
    '''
    Check if choice is correct. Return 1 for True and 0 False.
    '''
    if a_option['follower_count'] >= b_option['follower_count'] and choice == 'a':
        return 1
    else:
        return 0

# random in list, show option A var a_option.
a_option = newOption()

# random in list, show B option var b_option. Can't be A.
b_option = newOption()

print(f"Compare A: {a_option['name']}, a {a_option['description']}, from {a_option['country']}.")
print(f"Against B: {b_option['name']}, a {b_option['description']}, from {b_option['country']}.")

# show option to user choose. Save it in var user_option.
choice = input("Who has more follower? Type 'A' or 'B': ").lower()

# compare the options, show who won. funcao winner().
result(a_option, b_option, choice)








print(list_used)



# if user_option won, the var a_option receive winner(), the var b_option receive another random. The score gets 1 point. The game continue.
# if user_option lose, the game ended, the final score is showed.
