# Write your code here
import random

SECRETS = ["python", "java", "kotlin", "javascript"]
SECRET_WORD = SECRETS[random.randint(0, len(SECRETS)-1)]
hint = SECRET_WORD[:3] + str(''.join(["-" for x in SECRET_WORD[3:]]))

if input("Guess the word {}:".format(hint)) == SECRET_WORD:
    print("You survived!")
else:
    print("You lost!")


