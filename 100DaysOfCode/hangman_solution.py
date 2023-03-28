import random
from replit import clear
import hangman_art as art
import hangman_words as wrd

print(art.logo)

word_list = wrd.word_list

chosen_word = random.choice(word_list)

chosen_word_size = len(chosen_word)
chosen_word_hide = []

for _ in range(chosen_word_size):
    chosen_word_hide += "_"

# print("The word is:", chosen_word)

lives = 7
words_guess = set()
words_wrong = set()
end_of_game = False

while not end_of_game:
    print(f"Word to guess: {' '.join(chosen_word_hide)}")
    guess = input("Gues a letter: ").lower()
    clear() 

    for idx, letter in enumerate(chosen_word):
        if letter == guess:
            chosen_word_hide[idx] = guess
        elif letter != guess and not chosen_word.count(guess) > 0:
            words_wrong.add(guess)
        else:
            pass

    words_guess.add(guess)
    lives_used = len(words_wrong)
    rest_of_lives = lives - lives_used

    #print console
    if "_" not in chosen_word_hide:
        end_of_game = True
        print("You win!")
    elif not end_of_game and lives_used < lives:
        print(f"words guessed: {', '.join(words_guess)} ")
        print(f"words wrongs: {', '.join(words_wrong)} ")
        print(art.stages[rest_of_lives])
        print("You have:", rest_of_lives, "lives to use.")
    elif rest_of_lives == 0:
        print("You lose.")
        print("The correct word is: {}".format(chosen_word))
        end_of_game == True
    