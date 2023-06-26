class Position:
    HIGH = 'high'
    LOW = 'low'


class Warrior:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.block = None
        self.deceased = False
        self.zombie = False

    def attack(self, defender, position):
        if defender.deceased:
            defender.zombie = True
        else:
            if defender.block == position:
                pass
            elif position == Position.HIGH:
                defender.health -= 10
            elif position == Position.LOW:
                defender.health -= 5 if defender.block else defender.health -= 10
            if defender.health <= 0:
                defender.health = 0
                defender.deceased = True


ninja = Warrior('Ninja')
samurai = Warrior('Samurai')

ninja.block = Position.HIGH
samurai.attack(ninja, Position.LOW)
print(ninja.health)  # It should print 95
