import random


class Deck:
    """
    Class describes desk
    """
    def __init__(self):

        self.deck = [["", "A", "B", "C", "D", "E", "F", "G", "H", "",],
                    ["", "o", " ", "o", " ", "o", " ", "o", " ", "",],
                    ["", " ", "o", " ", "o", " ", "o", " ", "o", "",],
                    ["", "o", " ", "o", " ", "o", " ", "o", " ", "",],
                    ["", " ", " ", " ", " ", " ", " ", " ", " ", "",],
                    ["", " ", " ", " ", " ", " ", " ", " ", " ", "",],
                    ["", " ", "x", " ", "x", " ", "x", " ", "x", "",],
                    ["", "x", " ", "x", " ", "x", " ", "x", " ", "",],
                    ["", " ", "x", " ", "x", " ", "x", " ", "x", "",],
                    ["", "A", "B", "C", "D", "E", "F", "G", "H", "",]]

    def revers(self):
        self.deck.reverse()
        return self.deck





    def print_deck(self):

        for i, j in enumerate(self.deck):
            print(f"{i} {'|'.join(j)} {i}")


    def convert_input_to_coord(self, input_turn):


        syms_1 = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, }
        syms_2 = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, }

        a = input_turn

        x = syms_1[a[1]]
        y = syms_2[a[0]]

        return x, y

    def move_bot(self, bot_chacker):
        indexes = []
        for i, j in enumerate(self.deck):
            if bot_chacker in j:
                for k, l in enumerate(j):

                    if l == bot_chacker and (self.deck[i - 1][k - 1] == " " or self.deck[i - 1][k + 1] == " "):
                        a = [i, k]
                        indexes.append(a)

        indexes_choice = random.choice(indexes)

        step_rigth_or_left_choice = [0, 1]
        step_rigth_or_left = random.choice(step_rigth_or_left_choice)
        print(step_rigth_or_left)
        print(self.deck[indexes_choice[0]][indexes_choice[1]])

        if step_rigth_or_left == 1:

            self.deck[indexes_choice[0] - 1][indexes_choice[1] - 1] = self.deck[indexes_choice[0]][indexes_choice[1]]
        else:
            self.deck[indexes_choice[0] - 1][indexes_choice[1] + 1 ] = self.deck[indexes_choice[0]][indexes_choice[1]]

        self.deck[indexes_choice[0]][indexes_choice[1]] = " "





    def attack_bot(self, bot_chacker, player_chacker):
        indexes = []
        for i, j in enumerate(self.deck):
            if bot_chacker in j:
                for k, l in enumerate(j):
                    if l == bot_chacker and (self.deck[i - 1][k - 1] == player_chacker and self.deck[i - 2][k - 2] == "") or (self.deck[i + 1][k + 1] == player_chacker and self.deck[i + 2][k + 2] == "") or (self.deck[i - 1][k + 1] == player_chacker and self.deck[i - 2][k + 2] == "") or (self.deck[i + 1][k - 1] == player_chacker and self.deck[i + 2][k - 2] == ""):

                        a = [i, k]
                        indexes.append(a)

        indexes_choice = random.choice(indexes)
        return self.deck






