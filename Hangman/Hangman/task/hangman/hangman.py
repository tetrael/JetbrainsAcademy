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
    if len(letter) != 1:
        print("You should input a single letter")
        continue
    if not letter.islower() or not letter.isalpha():
        print("Please enter a lowercase English letter")
        continue

    if letter not in chosen_word and letter not in guessed_letters:
        print("That letter doesn't appear in the word")
        guessed_letters.add(letter)
        attempts -= 1
    elif letter not in guessed_letters:
        guessed_letters.add(letter)
    else:
        print("You've already guessed this letter")

    if attempts == 0:
        print("You lost!")
        break

else:
    print("You guessed the word {}!".format(game_word))
    print("You survived!")
