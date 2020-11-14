# Write your code here
import random

print("H A N G M A N")
attempts = 8
words_pool = ["python", "java", "kotlin", "javascript"]
chosen_word = random.choice(words_pool)
game_word = str(''.join(["-" for x in chosen_word[::]]))

while attempts > 0:
    print('\n' + game_word)
    letter = input("Input a letter: ")
    if letter in chosen_word:
        for x in range(len(chosen_word)):
            if chosen_word[x] == letter:
                game_word = list(game_word)
                game_word[x] = letter
                game_word = str(''.join(game_word))
    else:
        print("That letter doesn't appear in the word")

    attempts -= 1
else:
    print("\nThanks for playing!");
    print("We'll see how well you did in the next stage")
