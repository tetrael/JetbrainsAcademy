class Board:
    acceptable_chars = ('X', 'O')
    symbols = list(['_', '_', '_', '_', '_', '_', '_', '_', '_'])
    symbol = 'X'

    def select_index(self, coordinates):
        index = 0
        if int(coordinates[1]) == 1:
            index = int(coordinates[0]) + 5
        elif int(coordinates[1]) == 2:
            index = int(coordinates[0]) + 2
        elif int(coordinates[1]) == 3:
            index = int(coordinates[0]) - 1
        return index

    def change_symbol(self):
        self.symbol = 'O' if self.symbol == 'X' else 'X'

    def check_who_wins(self, char):
        # Checking if there are characters in a horizontal line
        if self.symbols[0] == char and self.symbols[1] == char and self.symbols[2] == char:
            return True
        elif self.symbols[3] == char and self.symbols[4] == char and self.symbols[5] == char:
            return True
        elif self.symbols[6] == char and self.symbols[7] == char and self.symbols[8] == char:
            return True
        # Checking if there are characters in a vertical line
        elif self.symbols[0] == char and self.symbols[3] == char and self.symbols[6] == char:
            return True
        elif self.symbols[1] == char and self.symbols[4] == char and self.symbols[7] == char:
            return True
        elif self.symbols[2] == char and self.symbols[5] == char and self.symbols[8] == char:
            return True
        # Checking if there are characters in a diagonal line
        elif self.symbols[0] == char and self.symbols[4] == char and self.symbols[8] == char:
            return True
        elif self.symbols[2] == char and self.symbols[4] == char and self.symbols[6] == char:
            return True
        else:
            return False

    def take_coordinates(self):
        coordinates = str(input("Enter the coordinates: ")).split()
        if not coordinates[0].isnumeric() \
                or not coordinates[1].isnumeric():
            print("You should enter numbers!")
            self.take_coordinates()
        elif int(coordinates[0]) not in [1, 2, 3] \
                or int(coordinates[1]) not in [1, 2, 3]:
            print("Coordinates should be from 1 to 3!")
            self.take_coordinates()
        elif self.symbols[self.select_index(coordinates)] != '_':
            print("This cell is occupied! Choose another one!")
            self.take_coordinates()
        else:
            self.symbols[self.select_index(coordinates)] = self.symbol
            self.print_board(self.symbols)
            self.change_symbol()

    def game_finish(self):
        if abs(self.symbols.count('X') - self.symbols.count('O')) not in [0, 1] \
                or (self.check_who_wins('X') and self.check_who_wins('O')):
            print("Impossible")
            return True
        elif self.check_who_wins('X'):
            print("X wins")
            return True
        elif self.check_who_wins('O'):
            print("O wins")
            return True
        # elif self.symbols.count('_') > 0:
        #     print("Game not finished")
        #     return True
        elif self.symbols.count('X') > 4 and self.symbols.count('O') > 3 and \
                not self.check_who_wins('X') and not self.check_who_wins('O'):
            print("Draw")
            return True
        else:
            return False

    def print_board(self, chars):
        print("---------\r| {} {} {} |\r| {} {} {} |\r| {} {} {} |\r---------".format(*chars))


board = Board()
board.print_board(board.symbols)
while not board.game_finish():
    board.take_coordinates()
