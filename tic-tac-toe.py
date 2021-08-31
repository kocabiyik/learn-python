from itertools import cycle


class TicTacToe:
    """TicTacToe game representation"""

    def __init__(self):
        self.board = [[" "] * 3 for i in range(3)]
        self.player = cycle(["x", "o"])

    def mark(self, position):
        square = self.board[position[0]][position[1]]
        if square != ' ':
            raise ValueError("The square is occupied")
        else:
            self.board[position[0]][position[1]] = next(self.player)

    def is_win(self):
        pass

    def __str__(self):
        row = [" | ".join(self.board[r]) for r in range(3)]
        return "\n---------\n".join(row)


game = TicTacToe()
game.mark((1, 1))
game.mark((1, 0))
game.mark((0, 2))
game.mark((2, 2))
print(game)
