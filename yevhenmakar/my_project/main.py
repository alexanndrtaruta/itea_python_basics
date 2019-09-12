import random
from checkers_objects import Deck, Bot


def check_valid_checkerboard(cell):
    while True:
        if Deck.check_your_checkerboard(my_deck, cell, user_checkerboard):
            break
        else:
            print('It\'s not your checkerboard')
            cell = input('Where do you want to move from?\n')
    return True


my_deck = Deck()
bot = Bot()

color = random.randint(0, 1)

user_checkerboard = Deck.define_checkers(my_deck, color)

print('Your checkers is', user_checkerboard)

if user_checkerboard == 'x':

    bot_checkerboard = 'o'
else:

    bot_checkerboard = 'x'

print('Bot\'s checkerboard is', bot_checkerboard)

while True:

    my_deck.print_deck()

    decision = input('Do you want move or beat? \n')
    user_input_1 = input('Where do you want to move from?\n')
    a = check_valid_checkerboard(user_input_1)
    user_input_2 = input('Where do you want to move to?\n')
    if decision == 'move':
        if Deck.check_move(my_deck, user_input_1, user_input_2, user_checkerboard):
            move = Deck.move(my_deck, user_input_1, user_input_2)
        else:
            print('You can\'t move there!')

    elif decision == 'beat':
        if Deck.check_beat(my_deck, user_input_1, user_input_2, bot_checkerboard):
            beat = Deck.beat(my_deck, user_input_1, user_input_2)
        else:
            print('You can\'t beat like this!')

    bot_army = bot.make_army(my_deck.deck, bot_checkerboard)
    print(bot_army)
    pos = bot.check_beat(my_deck.deck, bot_army, user_checkerboard)
    print(pos)


