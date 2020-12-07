acceptable_chars = ('X', 'O', '_')
symbols = list()


def check_who_wins(char):
    # Checking if there are characters in a horizontal line
    if symbols[0] == char and symbols[1] == char and symbols[2] == char:
        return True
    elif symbols[3] == char and symbols[4] == char and symbols[5] == char:
        return True
    elif symbols[6] == char and symbols[7] == char and symbols[8] == char:
        return True
    # Checking if there are characters in a vertical line
    elif symbols[0] == char and symbols[3] == char and symbols[6] == char:
        return True
    elif symbols[1] == char and symbols[4] == char and symbols[7] == char:
        return True
    elif symbols[2] == char and symbols[5] == char and symbols[8] == char:
        return True
    # Checking if there are characters in a diagonal line
    elif symbols[0] == char and symbols[4] == char and symbols[8] == char:
        return True
    elif symbols[2] == char and symbols[4] == char and symbols[6] == char:
        return True
    else:
        return False


for x in str(input("Enter cells: ")):
    symbols.append(x if x in acceptable_chars else '')

print("""---------
| {} {} {} |
| {} {} {} |
| {} {} {} |
---------""".format(*symbols))

if abs(symbols.count('X') - symbols.count('O')) not in [0, 1] \
        or (check_who_wins('X') and check_who_wins('O')):
    print("Impossible")
elif check_who_wins('X'):
    print("X wins")
elif check_who_wins('O'):
    print("O wins")
elif symbols.count('_') > 0:
    print("Game not finished")
elif not check_who_wins('X') and not check_who_wins('O'):
    print("Draw")
