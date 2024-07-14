class Tictactoe:
    def __init__(self):
        self.board = [" " for _ in range(9)]

    def print_board(self):
        row_1 = '|'.join(self.board[0:3])
        row_2 = '|'.join(self.board[3:6])
        row_3 = '|'.join(self.board[6:9])
        print(row_1)
        # _ = ['-' for i in range(5)]
        print("-----")
        print(row_2)
        print("-----")

        print(row_3)

    # print("-----")

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == ' ']

    def winner(self, symbol):
        win_condition = [(0, 1, 2), (0, 4, 8), (0, 3, 6), (2, 4, 6), (2, 5, 8), (1, 4, 7), (3, 4, 5), (6, 7, 8)]
        for i in win_condition:
            if all([self.board[j] == symbol for j in i]):
                return True
        return False

    def minimax(self, opponent):
        if self.winner('O'):
            return 1
        if self.winner('X'):
            return -1
        if ' ' not in self.board:
            return 0

        if opponent:
            val = 100000
            for i in self.available_moves():
                self.board[i] = 'X'
                evaluation = self.minimax(False)
                self.board[i] = ' '
                val = min(val, evaluation)
            return val
        else:
            val = -100000
            for i in self.available_moves():
                self.board[i] = 'O'
                evaluation = self.minimax(True)
                self.board[i] = ' '
                val = max(val, evaluation)
            return val

    def find_best_route(self):
        val = -100000
        index = 0
        for i in self.available_moves():
            self.board[i] = 'O'
            evaluation = self.minimax(True)
            # index = i
            if evaluation > val:
                val = evaluation
                index = i
            self.board[i] = ' '
        return index


if __name__ == "__main__":
    game = Tictactoe()
    game.print_board()
    while " " in game.board:
        user = int(input("Hay nhap so thu tu o ban muon di (0-8):"))
        game.board[user] = 'X'
        game.print_board()
        print()
        game.board[game.find_best_route()] = 'O'
        game.print_board()
        print()
        if game.winner('O'):
            print("AI thang!!")
            break
        if game.winner('X'):
            print("Ban thang")
            break
        if " " not in game.board:
            print("Hoa!!!")
