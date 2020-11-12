# Write your code here
import random

SECRETS = ["python", "java", "kotlin", "javascript"]
SECRET_WORD = SECRETS[random.randint(0, len(SECRETS)-1)]

if input("Guess the word:") == SECRET_WORD:
    print("You survived!")
else:
    print("You lost!")