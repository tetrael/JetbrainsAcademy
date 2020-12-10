class TicTacToe:
    players = ('X', 'O')
    board = list(" " * 9)
    symbol = 'X'

    @staticmethod
    def select_index(coordinates):
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

    @staticmethod
    def who_wins(board, player):
        win_state = [
            # Checking if there are characters in a horizontal line
            [board[0], board[1], board[2]],
            [board[3], board[4], board[5]],
            [board[6], board[7], board[8]],
            # Checking if there are characters in a vertical line
            [board[0], board[3], board[6]],
            [board[1], board[4], board[7]],
            [board[2], board[5], board[8]],
            # Checking if there are characters in a diagonal line
            [board[0], board[4], board[8]],
            [board[2], board[4], board[6]],
        ]
        return [player, player, player] in win_state

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
        elif self.board[self.select_index(coordinates)] != ' ':
            print("This cell is occupied! Choose another one!")
            self.take_coordinates()
        else:
            self.board[self.select_index(coordinates)] = self.symbol
            self.print_board(self.board)
            self.change_symbol()

    def game_finish(self):
        if abs(self.board.count('X') - self.board.count('O')) not in [0, 1] \
                or (self.who_wins(self.board, self.players[0])
                    and self.who_wins(self.board, self.players[1])):
            print("Impossible")
            return True
        elif self.who_wins(self.board, self.players[0]):
            print("X wins")
            return True
        elif self.who_wins(self.board, self.players[1]):
            print("O wins")
            return True
        elif self.board.count('X') > 4 and self.board.count('O') > 3 \
                and not self.who_wins(self.board, self.players[0]) \
                and not self.who_wins(self.board, self.players[1]):
            print("Draw")
            return True
        else:
            return False

    @staticmethod
    def print_board(chars):
        print("---------\r| {} {} {} |\r| {} {} {} |\r| {} {} {} |\r---------".format(*chars))


game = TicTacToe()
game.print_board(game.board)
while not game.game_finish():
    game.take_coordinates()
