import random


class Character:
    """
    Class describes character
    """
    def __init__(self, name):

        self.name = name
        self._hp = 100
        self._damage = 20

    def is_dead(self):

        """
        Function to check if char is dead
        """

        if self._hp <= 0:
            return True

    def on_combat(self, enemy):

        """
        Function to describe fighting
        """

        self._hp -= enemy.attack()
        is_dead = self.is_dead()

        if is_dead:
            return is_dead

        print(f'Char hp: {self._hp}')
        enemy.take_damage(self._damage)

    def move(self):

        step = random.choice(['left', 'right', 'up', 'down'])
        return step

    def heal(self):

        self._hp += random.choice(range(5, 20))
        print('Current health:' + str(self._hp))

    def show_current_health(self):

        return self._hp

class Orc(Character):

    """
    Class to describe Orc race
    """

    def __init__(self, name):

        super().__init__(name)  # call to Character().__init__

        self._hp *= 1.5
        self._damage *= 1.2


class Elf(Character):

    """
    Class to describe Elf race
    """

    def __init__(self, name):

        super().__init__(name)  # call to Character().__init__

        self._hp *= 1.2
        self._damage *= 1.5


# races to be checked within a game loop
RACES = {'orc': Orc, 'elf': Elf}
