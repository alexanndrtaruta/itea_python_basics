import RPG_characters
import RPG_enemies
import random
from time import sleep

char_race = input('Your race: ')
char_name = input('Your name: ')

if char_race in RPG_characters.RACES:

    main_char = RPG_characters.RACES[char_race](char_name)

while True:

    moove = input(' Enter your moove ( w - forward,  d - right, s - back, a - left ) : ')

    option = random.choice(['enemy', 'nothing', 'enemy', 'heal' , 'enemy'])

    if option == 'enemy':

        current_enemy = random.choice(RPG_enemies.ENEMIES_TYPES)()

        while not current_enemy.is_dead():

            is_dead = main_char.on_combat(current_enemy)
            sleep(1.5)

            if is_dead:
                print(' game over ')
                break


    elif option == 'heal':

        main_char.heal()
        continue
