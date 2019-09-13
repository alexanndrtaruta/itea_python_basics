import random


class Player:

    def __init__(self, color, deck):

        self.color = color
        self.checkers_army = []
        self.player_step = ()                   # ??? For what it?
        self.deck = deck

    def player_army(self):
        """
        Method generates army of player checkers
        :return: list
        """
        for x in range(len(self.deck)):
            for y in range(len(self.deck[x])):
                if self.deck[x][y] == self.color:
                    self.checkers_army.append((x, y))

        return self.checkers_army


class User(Player):

    def convert_to_coordinate(self, user_coordinate):
        """
        Method converts user input to coordinates
        :param user_coordinate: string
        :return: tuple
        """
        dict_letters = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
        dict_number = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7}

        y = dict_letters[user_coordinate[0]]
        x = dict_number[user_coordinate[1]]
        converted_coordinates = (x, y)

        return converted_coordinates

    def step_validation(self, checker_coords):              # user step validation

        condition_1 = (checker_coords[0] - 1, checker_coords[1] + 1)
        condition_2 = (checker_coords[0] - 1, checker_coords[1] - 1)

        return condition_1, condition_2


class Bot(Player):

    def step_validation(self, checker_coords):              # bot step validation

        condition_1 = (checker_coords[0] + 1, checker_coords[1] + 1)
        condition_2 = (checker_coords[0] + 1, checker_coords[1] - 1)

        return condition_1, condition_2

    def bot_step(self):
        """
        Method describes bot logic
        :return: touples of bot checker and its move coordinates
        """
        empty_fields = []
        bot_checkers_to_go = []
        bot_possible_steps = []

        for x in range(len(self.deck)):
            for y in range(len(self.deck[x])):
                if self.deck[x][y] == ' ':
                    empty_fields.append((x, y))

        for i in self.checkers_army:
            for ef in empty_fields:
                if ef == self.step_validation(i)[0] or ef == self.step_validation(i)[1]:        # step validation
                    bot_checkers_to_go.append(i)
                    bot_possible_steps.append(ef)

        unique_bot_checkers = list(set(bot_checkers_to_go))
        unique_bot_steps = list(set(bot_possible_steps))
        print('Unique list of steps', unique_bot_steps)
        bot_checker_choice = random.choice(unique_bot_checkers)
        print('Bot checker choice', bot_checker_choice)

        while True:

            bot_step_choice = random.choice(unique_bot_steps)
            print('Bot choice step 1', bot_step_choice)
            if bot_step_choice in self.step_validation(bot_checker_choice):
                break

        print('Bot choice step confirmation', bot_step_choice)

        return bot_checker_choice, bot_step_choice
