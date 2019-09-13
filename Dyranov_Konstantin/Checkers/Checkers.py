class Color(object):
    EMPTY = 0  # If the color of the checkers is our color, you cannot beat
    Black = 1
    White = 2


class Empty(object):
    color = Color.EMPTY

    def get_moves(self, board, x, y):
        raise Exception("Error !")

    def __repr__(self):  # in the final form will be through the STR method
        return " "


class Objekt(object):
    IMG = None  # Save the image of the checkers

    def __init__(self, color):
        self.color = color

    def __repr__(self):
        return self.IMG[0 if self.color == Color.White else 1]


class Chekckers(Objekt):
    IMG = ["?", "?"]

    def get_moves(self, board, x, y):  # checkers move list of possible moves
        moves = []
        if self.color == Color.Black and y < 7 and board.get_color(x, y+1) == Color.EMPTY:  # the move of the black checker with a check to see if the checker is on the end of the board
            moves.append([x, y+1])
        return moves

class Empty_checkers(Objekt):
    IMG = [" ", " "]

    def get_moves(self, boaed, x, y):
        moves = []
        return moves


class Board(object):
    def __init__(self):
        self.board = [[Empty()] * 8 for y in range(8)]  # Create a board
        self.board[0][0] = Chekckers(Color.Black)  # Checkers position on the field
        self.board[0][2] = Chekckers(Color.Black)
        self.board[0][4] = Chekckers(Color.Black)
        self.board[0][6] = Chekckers(Color.Black)
        self.board[1][1] = Chekckers(Color.Black)
        self.board[1][3] = Chekckers(Color.Black)
        self.board[1][5] = Chekckers(Color.Black)
        self.board[1][7] = Chekckers(Color.Black)
        self.board[2][0] = Chekckers(Color.Black)
        self.board[2][2] = Chekckers(Color.Black)
        self.board[2][4] = Chekckers(Color.Black)
        self.board[2][6] = Chekckers(Color.Black)

        self.board[5][1] = Chekckers(Color.White)
        self.board[5][3] = Chekckers(Color.White)
        self.board[5][5] = Chekckers(Color.White)
        self.board[5][7] = Chekckers(Color.White)
        self.board[6][0] = Chekckers(Color.White)
        self.board[6][2] = Chekckers(Color.White)
        self.board[6][4] = Chekckers(Color.White)
        self.board[6][6] = Chekckers(Color.White)
        self.board[7][1] = Chekckers(Color.White)
        self.board[7][3] = Chekckers(Color.White)
        self.board[7][5] = Chekckers(Color.White)
        self.board[7][7] = Chekckers(Color.White)

        self.board[3][1] = Empty_checkers(Color.EMPTY)
        self.board[3][3] = Empty_checkers(Color.EMPTY)
        self.board[3][5] = Empty_checkers(Color.EMPTY)
        self.board[3][7] = Empty_checkers(Color.EMPTY)
        self.board[4][0] = Empty_checkers(Color.EMPTY)
        self.board[4][2] = Empty_checkers(Color.EMPTY)
        self.board[4][4] = Empty_checkers(Color.EMPTY)
        self.board[4][6] = Empty_checkers(Color.EMPTY)

        '''
        for row in self.board:
            for elem in row:
                print(elem, end=' ')
            print()
        '''
    def get_color(self, board, x, y):
        return self.board[y][x].get_color

    def get_moves(self, board, x, y):
        return self.board[y][x].get_moves(self, x, y)

    def move(self, xy_from, xy_to):
        self.board[xy_to[1]][xy_to[0]] = self.board[xy_from[1]][xy_from[0]]
        self.board[xy_from[1]][xy_from[0]] = Empty()

    def __repr__(self):
        colors = [0, 46]
        res = ""  # first chess line
        i = 0
        for y in range(8):
            for x in range(8):
                res += set_color(colors[i]) + str(self.board[y][x]) + "  "
                i = 1 - i
            i = 1 - i
            res += set_color(0) + "\n"
        return res

#print(Board())

def set_color(color):
    return "\033[%sm" % color

b = Board()
print(b)
#m = (b.get_moves[2, 1])
#print(m)
#m = b.get_moves(2, 1)
#b.move([2, 1]), m[0])
#print(b)
