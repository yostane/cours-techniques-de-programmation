class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, p, width, height) -> None:
        self.p = p
        self.width = width
        self.height = height


class Character:
    def __init__(self, name, hp, mp, position, hitbox) -> None:
        self.name = name
        self.hp = hp
        self.mp = mp
        self.position = position
        self.hitbox = hitbox


class Hero(Character):
    def __init__(self, name, hp, mp, position, hitbox) -> None:
        super().__init__(name, hp, mp, position, hitbox)
        self.level = 1

    def attack(monster):
        monster.hp -= 2

    def performSkill(character):
        pass


class Monster(Character):
    def __init__(self, name, hp, mp, position, hitbox) -> None:
        super().__init__(name, hp, mp, position, hitbox)

    def attack(hero):
        hero.hp -= 1


class Warrior(Character):
    def __init__(self, name, hp, position, hitbox) -> None:
        super().__init__(name, hp, 0, position, hitbox)
