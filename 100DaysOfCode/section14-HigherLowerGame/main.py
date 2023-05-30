from random import choice as random_choice
from game_data import data
import art
import os

list_used = []
def newOption ():
    '''
    Return a random new option without repeat itens usaged.
    '''
    list_option = []
    for i in data:
        list_option.append(i)

    list_available = [item for item in list_option if item not in list_used]
    
    new_option = random_choice(list_available)
    list_used.append(new_option)
    
    return new_option

def result(a_option, b_option):
    '''
    Return granter option.
    '''
    if a_option['follower_count'] >= b_option['follower_count']:
        return 'a'
    else:
        return 'b'

clear = lambda: os.system('clear')

# random in list, show option A var a_option.
a_option = newOption()

# random in list, show B option var b_option. Can't be A.
b_option = newOption()

# loop start
score = 0
playing = True
while playing:
    clear()
    print(art.logo)

    print(f"Compare A: {a_option['name']}, a {a_option['description']}, from {a_option['country']}.")
    print(art.vs)
    print(f"Against B: {b_option['name']}, a {b_option['description']}, from {b_option['country']}.")

    # show option to user choose. Save it in var user_option.
    choice = input("Who has more follower? Type 'A' or 'B': ").lower()
    # print(f'You choose: {choice}')

    # compare the options, show who won. funcao winner().
    outcome = result(a_option, b_option)

    # def check_result(choice, result):
    if choice == outcome:
        score += 1
        if outcome == 'a':
            b_option = newOption()
        else:
            a_option = b_option
            b_option = newOption()
    else:
        clear()
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        playing = False


# print(list_used)

# if user_option won, the var a_option receive winner(), the var b_option receive another random. The score gets 1 point. The game continue.

# if user_option lose, the game ended, the final score is showed.
