import random

print("H A N G M A N")
attempts = 8
words_pool = ["python", "java", "kotlin", "javascript"]
chosen_word = random.choice(words_pool)
guessed_letters = set()

while attempts > 0:
    game_word = ''.join(letter if letter in guessed_letters else "-" for letter in chosen_word)
    print('\n' + game_word)
    letter = input("Input a letter: ")

    if letter not in chosen_word or letter in game_word:
        print("No improvements" if letter in game_word else "That letter doesn't appear in the word")
        attempts -= 1
    else:
        guessed_letters.add(letter)

    if attempts == 0:
        print("You lost!")
        break

else:
    print("You survived!")
