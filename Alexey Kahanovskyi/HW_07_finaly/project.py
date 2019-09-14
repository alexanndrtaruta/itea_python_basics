import Deck
from time import sleep

d = Deck.Main()

d.print_list()

while d.count_check():

    while True:

        choice = input('moove or fight ? (press m or f): ')

        if choice.lower() == 'm':

            d.new_index()
            d.cord()
            d.checker_moove()
            break

        elif choice.lower() == 'f':

            d.new_index()
            d.cord()
            d.fight_vs_bot()
            break

        else:

            continue

    d.print_list()

    cho = input(' Next tern ? (press Enter) ')

    if cho == '':

        if d.bot_fight_checker() == True:

            d.bot_fight()

        else:

            d.bot_moove()

    d.print_list()

sleep(2)
