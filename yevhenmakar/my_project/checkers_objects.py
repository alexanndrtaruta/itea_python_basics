class Deck:

    def __init__(self):

        self.deck = [['x', ' ', 'x', ' ', 'x', ' ', 'x', ' '],
                     [' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x'],
                     ['x', ' ', 'x', ' ', 'x', ' ', 'x', ' '],
                     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                     [' ', 'o', ' ', 'o', ' ', 'o', ' ', 'o'],
                     ['o', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
                     [' ', 'o', ' ', 'o', ' ', 'o', ' ', 'o']]

    def print_deck(self):

        rows = ['1', '2', '3', '4', '5', '6', '7', '8']

        print('     A ', ' B ', ' C ', ' D ', ' E ', ' F ', ' G ', ' H ')

        for j, i in enumerate(self.deck):

            print(rows[j] + '  |', ' | '.join(i), '|  ' + rows[j])

        print('     A ', ' B ', ' C ', ' D ', ' E ', ' F ', ' G ', ' H ')

    def define_checkers(self, user_user):

        if user_user == 1:
            user_checkerboard = 'x'

        else:
            user_checkerboard = 'o'

        return user_checkerboard

    def convert_inputs_to_coords(self, user_input):

        syms = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
        coord = (int(user_input[1]) - 1, syms[user_input[0]])

        return coord

    def check_your_checkerboard(self, cell, user_checkerboard):

        coord = self.convert_inputs_to_coords(cell)

        if self.deck[coord[0]][coord[1]] == user_checkerboard:
            return True

    def check_move(self, user_input_1, user_input_2, user_checkerboard):

        coord_1 = self.convert_inputs_to_coords(user_input_1)

        coord_2 = self.convert_inputs_to_coords(user_input_2)

        dif_coord = ((coord_2[0] - coord_1[0]), (coord_2[1] - coord_1[1]))

        if user_checkerboard == 'x':

            if (dif_coord == (1, -1) or dif_coord == (1, 1)) and self.deck[coord_2[0]][coord_2[1]] == ' ':
                checker = True

            else:
                checker = False

            return checker

        if user_checkerboard == 'o':

            if (dif_coord == (-1, -1) or dif_coord == (-1, 1)) and self.deck[coord_2[0]][coord_2[1]] == ' ':
                checker = True

            else:
                checker = False

            return checker

    def check_beat(self, user_input_1, user_input_2, bot_checkerboard):

        coord_1 = self.convert_inputs_to_coords(user_input_1)

        coord_2 = self.convert_inputs_to_coords(user_input_2)

        dif_coord = (((coord_2[0] - coord_1[0]) / 2), ((coord_2[1] - coord_1[1]) / 2))

        possible_attack = self.deck[coord_1[0] + int(dif_coord[0])][coord_1[1] + int(dif_coord[0])]

        if self.deck[coord_2[0]][coord_2[1]] == ' ' and possible_attack == bot_checkerboard:
            checker = True

        else:
            checker = False

        return checker

    def move(self, coord_x, coord_y):

        x = self.convert_inputs_to_coords(coord_x)
        y = self.convert_inputs_to_coords(coord_y)

        self.deck[y[0]][y[1]], self.deck[x[0]][x[1]] = self.deck[x[0]][x[1]], ' '

        return self.deck

    def beat(self, coord_x, coord_y):

        x = self.convert_inputs_to_coords(coord_x)
        y = self.convert_inputs_to_coords(coord_y)

        dif_coord = (((y[0] - x[0]) / 2), ((y[1] - x[1]) / 2))
        print(dif_coord)

        self.deck[y[0]][y[1]], self.deck[x[0]][x[1]] = self.deck[x[0]][x[1]], ' '
        self.deck[x[0] + int(dif_coord[0])][x[1] + int(dif_coord[0])] = ' '


class Bot:

    def __init__(self):

        self.army = []

    def make_army(self, deck, bot_checkerboard):

        for x in range(len(deck)):
            for y in range(len(deck)):
                if deck[x][y] == bot_checkerboard:
                    self.army.append((x, y))

        return self.army

    def check_beat(self, deck, army, user_checkerboard):
        army_beat = []

        for i in army:
            possible_move_1 = (i[0] + 1, i[1] - 1)
            possible_move_2 = (i[0] + 1, i[1] + 1)
            possible_move_3 = (i[0] - 1, i[1] + 1)
            possible_move_4 = (i[0] - 1, i[1] - 1)
            try:
                if deck[possible_move_1[0]][possible_move_1[1]] == user_checkerboard \
                        or deck[possible_move_2[0]][possible_move_2[1]] == user_checkerboard \
                        or deck[possible_move_3[0]][possible_move_3[1]] == user_checkerboard \
                        or deck[possible_move_4[0]][possible_move_4[1]] == user_checkerboard:
                    army_beat.append(i)
            except IndexError:
                print('out of the range')

    def check_move(self, deck, army, bot_checkerboard):
        army_move = []
        if bot_checkerboard == 'x':
            for i in army:
                possible_move_1 = (i[0] + 1, i[1] - 1)
                possible_move_2 = (i[0] + 1, i[1] + 1)
                if deck[possible_move_1[0]][possible_move_1[1]] == ' ' \
                        or deck[possible_move_2[0]][possible_move_2[1]] == ' ':
                    army_move.append(i)

        if bot_checkerboard == 'o':
            for i in army:
                possible_move_1 = (i[0] - 1, i[1] - 1)
                possible_move_2 = (i[0] - 1, i[1] + 1)
                if deck[possible_move_1[0]][possible_move_1[1]] == ' ' \
                        or deck[possible_move_2[0]][possible_move_2[1]] == ' ':
                    army_move.append(i)
        print(army_move)
