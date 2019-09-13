import random
import deck as d
import player
import checker

color = random.choice(['black', 'white'])

if color == 'black':
    user_color = 'x'
    bot_color = 'o'

else:
    user_color = 'o'
    bot_color = 'x'

print('\nYou will play for', color + '!\n')


deck = d.Deck(user_color)

while True:

    deck.deck_output()

# user logic
    while True:
        user = player.User(user_color, deck.deck)
        user.player_army()

        try:
            user_coords_from = user.convert_to_coordinate(input('Enter your checker coordinates: '))
            user_coords_to = user.convert_to_coordinate(input('Enter your move destination coordinates: '))
        except KeyError or IndexError:
            continue

        user_step_validation_1 = user.step_validation(user_coords_from)[0]
        user_step_validation_2 = user.step_validation(user_coords_from)[1]

        user_checker = checker.Checker(user_coords_from, user_color, deck.deck)

        if user_checker.attack_needed(user.player_army()):

            user_coords_from = user.convert_to_coordinate(input('Enter your checker for attack: '))
            user_coords_to = user.convert_to_coordinate(input('Enter your move destination coordinates: '))
            user_checker.attack(user_coords_to)
            break

        user_step = user_checker.step(user_coords_to, user_step_validation_1, user_step_validation_2)

        if user_step:
            deck.deck_update(user_coords_from, user_coords_to)
            break
        else:
            print('User input - incorrect!')

        # Bot logic
    bot = player.Bot(bot_color, deck.deck)
    bot.player_army()

    bot_step = list(bot.bot_step())

    bot_checker_choice = bot_step[0]

    bot_movement = bot_step[1]

    bot_checker = checker.Checker(bot_color, bot_checker_choice, deck.deck)

    deck.deck_update(bot_checker_choice, bot_movement)
