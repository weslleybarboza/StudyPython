# loop start

# random in list, show option A var a_option.

from random import choice
from game_data import data

list_used = []
def newOption ():
    '''
    Return a new option without repeat itens usaged.
    '''
    list_option = []
    for i in data:
        list_option.append(i['name'])

    list_available = [item for item in list_option if item not in list_used]
    
    new_option = choice(list_available)
    list_used.append(new_option)
    
    return new_option

newOption()

print(list_used)

# random in list, show B option var b_option. Can't be A.

# show option to user choose. Save it in var user_option.

# compare the options, show who won. funcao winner().

# if user_option won, the var a_option receive winner(), the var b_option receive another random. The score gets 1 point. The game continue.
# if user_option lose, the game ended, the final score is showed.
