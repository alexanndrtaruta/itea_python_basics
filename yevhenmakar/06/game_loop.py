import characters
import enemies
import random
from time import sleep

char_race = input('Your race: ')
char_name = input('Your name: ')

# Check if char_race exists
if char_race in characters.RACES:
    # Create main_char instance
    main_char = characters.RACES[char_race](char_name)

print('Let\'s the game begin')
while True:

    step = input('Where do you want to move? ("left", "right", "up", "down")\n')
    if step == main_char.move():
        heal_or_battle = random.randint(0, 1)
        if heal_or_battle == 0:
            # Randomly picked enemy
            current_enemy = random.choice(enemies.ENEMIES_TYPES)()

            is_dead = main_char.on_combat(current_enemy)

            if is_dead:
                print('Game over')
                break

            sleep(2)
        elif heal_or_battle == 1:
            print('You found health')
            char_heal = main_char.heal()
    else:
        print('No enemies, go farther!')
