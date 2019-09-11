class Character:
    """
    Class describes character
    """
    
    def __init__(self, name):

        self.name = name
        self._hp = 100
        self._damage = 5

    
    def heal(self):
        
        self._hp += 10
        print(f'Char hp + heal: {self._hp}')
    
    
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
        

class Orc(Character):

    """
    Class to describe Orc race
    """


    def __init__(self, name):

        super().__init__(name)  

        self._hp *= 1.5
        self._damage *= 1.2


class Elf(Character):
    """
    Class to describe Elf race
    """


    def __init__(self, name):
        super().__init__(name)  

        self._hp *= 1.9
        self._damage *= 0.75


RACES = {'orc': Orc, 'elf': Elf }
