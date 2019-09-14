class Checker:

    def __init__(self, coordinates, color, deck):

        self.coords = coordinates
        self.color = color
        self.deck = deck

    def step(self, move_dest, valid_condition1, valid_condition2):
        """
        Method describes posibility of piece to move
        :param move_dest: tuple of coordination
        :param valid_condition1: tuple with allowed coordination for moving
        :param valid_condition2: tuple with allowed coordination for moving
        :return: bool True/False
        """
        correct_destination = (move_dest == valid_condition1 or move_dest == valid_condition2)

        if self.deck[self.coords[0]][self.coords[1]] == self.color:

            if correct_destination and self.is_empty(move_dest):
                result = True

            else:
                result = False
            return result

        else:
            print('This is empty field')
            result = False
            return result

    def empty_field_list(self):
        """
        Method calculates empty fields on the deck
        :return: list of coordinates
        :rtype: list
        """
        empty_field = []

        for x in range(len(self.deck)):
            for y in range(len(self.deck[x])):
                if self.deck[x][y] == ' ':
                    empty_field.append((x, y))

        return empty_field

    def is_empty(self, move_dest):
        """
        Method checks of is field is empty
        :param move_dest: coords of square to move
        :return: bool True/False
        """
        if move_dest in self.empty_field_list():
            is_empty = True
        else:
            print('Field is not empty')
            is_empty = False

        return is_empty

    def attack_needed(self, checkers_army):
        """
        Method checks of attack opportunity
        :param checkers_army: list of tuples
        :return: bool True/False
        """
        enemy_army = []

        for x in range(len(self.deck)):
            for y in range(len(self.deck[x])):
                if self.deck[x][y] != ' ' and self.deck[x][y] != self.color:
                    enemy_army.append((x, y))
        print('Enemy army', enemy_army)
        first_check = []
        second_check = []

        for i in checkers_army:

            for j in enemy_army:

                if j == (i[0] + 1, i[1] + 1) or j == (i[0] - 1, i[1] - 1) or j == (i[0] + 1, i[1] - 1) or j == (
                        i[0] - 1, i[1] + 1):
                    first_check.append(j)

        for j in first_check:
            for ef in self.empty_field_list():

                if ef == (j[0] + 1, j[1] + 1) or ef == (j[0] - 1, j[1] - 1) or ef == (j[0] + 1, j[1] - 1) or ef == (
                        j[0] - 1, j[1] + 1):
                    second_check.append(ef)

        if not second_check:
            result = False

        elif second_check:
            print('You need to attack!!!')
            result = True

        else:
            result = False

        return result

    def attack_targets(self):
        """
        Method configurates dictionary with targets and fields for jumping
        :return: dict
        """
        targ_1 = self.coords[0] - 1, self.coords[1] - 1
        targ_2 = self.coords[0] - 1, self.coords[1] + 1
        targ_3 = self.coords[0] + 1, self.coords[1] - 1
        targ_4 = self.coords[0] + 1, self.coords[1] + 1

        step_attack_1 = self.coords[0] - 2, self.coords[1] - 2
        step_attack_2 = self.coords[0] - 2, self.coords[1] + 2
        step_attack_3 = self.coords[0] + 2, self.coords[1] - 2
        step_attack_4 = self.coords[0] + 2, self.coords[1] + 2

        dict_attack = {step_attack_1: targ_1, step_attack_2: targ_2, step_attack_3: targ_3, step_attack_4: targ_4}

        return dict_attack

    def attack(self, move_dest):
        """
        Method describes and rewrites deck after attack
        :param move_dest: tuple(x, y) - coordination to go
        :return: rewritten deck
        """
        dict_attack = self.attack_targets()

        if move_dest in dict_attack and self.is_empty(move_dest):
            target = dict_attack[move_dest]

            if self.deck[target[0]][target[1]] != self.color and self.deck[target[0]][target[1]] != ' ':
                self.deck[move_dest[0]][move_dest[1]] = self.deck[self.coords[0]][self.coords[1]]
                self.deck[self.coords[0]][self.coords[1]] = ' '
                self.deck[target[0]][target[1]] = ' '
                return self.deck

            else:
                print('This step is not correct. Do another one')
