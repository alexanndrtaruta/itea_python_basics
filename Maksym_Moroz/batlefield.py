class Desk:
    def __init__(self):
        self.empty_place = '| |'
        self.white_checker = '|w|'
        self.black_checker = '|b|'
        self.desk = [[self.empty_place, self.black_checker, self.empty_place, self.black_checker, self.empty_place, self.black_checker, self.empty_place, self.black_checker],
                [self.black_checker, self.empty_place, self.black_checker, self.empty_place, self.black_checker, self.empty_place, self.black_checker, self.empty_place,],
                [self.empty_place, self.black_checker, self.empty_place, self.black_checker, self.empty_place, self.black_checker, self.empty_place, self.black_checker],
                [self.empty_place,  self.empty_place,  self.empty_place, self.empty_place,  self.empty_place,  self.empty_place, self.empty_place,  self.empty_place],
                [self.empty_place,  self.empty_place,  self.empty_place, self.empty_place,  self.empty_place,  self.empty_place, self.empty_place,  self.empty_place],
                [self.white_checker, self.empty_place, self.white_checker, self.empty_place, self.white_checker, self.empty_place, self.white_checker, self.empty_place],
                [self.empty_place, self.white_checker, self.empty_place, self.white_checker, self.empty_place, self.white_checker, self.empty_place, self.white_checker],
                [self.white_checker, self.empty_place, self.white_checker, self.empty_place, self.white_checker, self.empty_place, self.white_checker, self.empty_place]]

        self.position_dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}

    def desk_to_print(self, desk):
        self.show_desk = ''

        for i in range(8):
            self.show_desk += ''.join(map(str, self.desk[i])) + "\n"

        return print(self.show_desk)

    def move_checkers(self, desk):

        position_y = int(input('Choose checker number '))
        position_x = self.position_dict[input('Choose checker letter')]
        new_position_x = self.position_dict[input('Choose checker letter')]
        new_position_y = int(input('Choose checker number '))

        self.desk[position_y].pop(position_x)
        self.desk[position_y].insert(position_x, self.empty_place)

        self.desk[new_position_y].pop(new_position_x)
        self.desk[new_position_y].insert(new_position_x, self.white_checker)

        print(self.desk_to_print(desk))

    def attack(self):

        position_y = int(input('Choose checker number '))
        position_x = self.position_dict[input('Choose checker letter')]

        attack_checker_y = int(input('Choose number attacked checker '))
        attack_checker_x = self.position_dict[input('Choose letter attacked checker')]

        def delete_checker_and_attack_checker():
            self.desk[attack_checker_y][attack_checker_x].pop()
            self.desk[attack_checker_y].insert(attack_checker_x, self.empty_place)
            self.desk[position_y][position_x].pop()
            self.desk[position_y].insert(position_x, self.empty_place)

        def new_white_checker_position(y, x):
            self.desk[y][x].pop()
            self.desk[y].insert(x, self.white_checker)


        if (((attack_checker_x == position_x + 1 or attack_checker_x == position_x - 1) and attack_checker_y == position_y - 1)
            and self.desk[attack_checker_y][attack_checker_x] != self.white_checker and
            (self.desk[attack_checker_y - 1][attack_checker_x + 1] == self.empty_place
             or self.desk[attack_checker_y - 1][attack_checker_x - 1] == self.empty_place)
             and position_y == attack_checker_y + 1 and (position_x == attack_checker_x - 1 or position_x == attack_checker_x - 1)):

            if self.desk[position_x + 1] == self.desk[attack_checker_x] and self.desk[position_y - 1] == self.desk[attack_checker_y]:
                delete_checker_and_attack_checker()
                new_white_checker_position(attack_checker_y - 1, attack_checker_x + 1)

            elif self.desk[position_x - 1] == self.desk[attack_checker_x] and self.desk[position_y - 1] == self.desk[attack_checker_y]:
                delete_checker_and_attack_checker()
                new_white_checker_position(attack_checker_y - 1, attack_checker_x + 1)

            elif self.desk[position_x + 1] == self.desk[attack_checker_x] and self.desk[position_y + 1] == self.desk[attack_checker_y]:
                delete_checker_and_attack_checker()
                new_white_checker_position(attack_checker_y + 1, attack_checker_x + 1)

            elif self.desk[position_x - 1] == self.desk[attack_checker_x] and self.desk[position_y + 1] == self.desk[attack_checker_y]:
                delete_checker_and_attack_checker()
                new_white_checker_position(attack_checker_y + 1, attack_checker_x + 1)
            else:
                print('The move is impossible! Try a different one.')













