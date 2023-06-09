from random import choice as random_choice
from game_data import data
import art
from replit import clear

list_used = []


def new_random_element():
    """
    Return a random new option without repeat item usage.
    """
    list_option = []
    for i in data:
        list_option.append(i)

    list_available = [item for item in list_option if item not in list_used]

    new_option = random_choice(list_available)
    list_used.append(new_option)

    return new_option


def result(a_position, b_position):
    """
    Return granter option.
    """
    if a_position['follower_count'] >= b_position['follower_count']:
        return 'a'
    else:
        return 'b'


# random in list, show option A var a_option.
a_option = new_random_element()

# random in list, show B option var b_option. Can't be A.
b_option = new_random_element()

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
            b_option = new_random_element()
        else:
            a_option = b_option
            b_option = new_random_element()
    else:
        clear()
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        playing = False
