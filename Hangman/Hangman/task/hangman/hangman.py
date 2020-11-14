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
    game_word = ''.join(letter if letter in game_word else "-" for letter in chosen_word)
    if letter not in chosen_word:
        print("That letter doesn't appear in the word")
    attempts -= 1
else:
    print("""
    Thanks for playing!
    We'll see how well you did in the next stage""")
