# Write your code here
import random

# SECRETS = ["python", "java", "kotlin", "javascript"]
# SECRET_WORD = SECRETS[random.randint(0, len(SECRETS)-1)]
# hint = SECRET_WORD[:3] + str(''.join(["-" for x in SECRET_WORD[3:]]))
#
# if input("Guess the word {}:".format(hint)) == SECRET_WORD:
#     print("You survived!")
# else:
#     print("You lost!")

print("H A N G M A N" + '\n')
attempts = 8
words_pool = ["python", "java", "kotlin", "javascript"]
chosen_word = words_pool[random.randint(0, len(words_pool)-1)]
game_word = str(''.join(["-" for x in chosen_word[::]]))

while game_word != chosen_word and attempts > 0:
    guested_letters = list()
    print(game_word)
    letter = input("Input a letter: ")
    if letter in chosen_word and letter not in guested_letters:
        guested_letters.append(letter)
        for x in range(len(chosen_word)):
            if chosen_word[x] == letter:
                game_word = list(game_word)
                game_word[x] = letter
                game_word = str(''.join(game_word))
    else:
        print("That letter doesn't appear in the word")
        attempts -= 1
else:
    print("Thanks for playing!");
    print("We'll see how well you did in the next stage")
