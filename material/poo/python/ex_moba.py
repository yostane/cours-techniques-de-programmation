import random


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

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__} (name={self.name}, hp={self.hp}, mp={self.mp})"
        )

    def __repr__(self):
        """print d'une liste appelle cette méthode au lieu de __str__"""
        return self.__str__()


class Hero(Character):
    def __init__(self, name, position, hitbox) -> None:
        hp = random.randint(100, 200)
        mp = random.randint(50, 100)
        super().__init__(name, hp, mp, position, hitbox)
        self.level = 1

    def attack(self, monster):
        monster.hp -= 2
        print(self, "inflige deux de dégâts. Nouvel état du monstre", monster)

    def performSkill(self, character):
        print(
            self,
            "a appliqué une compétence a un personnage dont le nouvel état est:",
            character,
        )


class Warrior(Hero):
    def __init__(self, name, position, hitbox) -> None:
        super().__init__(name, position, hitbox)
        self.mp = 0

    def performSkill(self, character):
        character.hp = max(character.hp - 10, 0)
        super().performSkill(self, character)


class Mage(Hero):
    def performSkill(self, character):
        if self.mp < 5:
            return
        character.hp = max(character.hp - 20, 0)
        self.mp -= 5
        super().performSkill(character)


class Tank(Hero):
    def performSkill(self, character):
        if self.hp < 2:
            return
        character.hp += 2
        self.hp -= 2
        super().performSkill(character)


class Healer(Hero):
    def performSkill(self, character):
        if self.mp < 8:
            return
        character.hp += 30
        self.mp -= 8
        super().performSkill(character)


class Monster(Character):
    def __init__(self, name, position, hitbox) -> None:
        hp = random.randint(30, 70)
        super().__init__(name, hp, 0, position, hitbox)

    def attack(self, hero):
        print(self, "inflige deux de dégâts. Nouvel état du héro", hero)
        hero.hp -= 1


class Minion(Monster):
    pass


class Buldozer(Monster):
    pass


mage = Mage(
    "Ryze",
    Point(10, 10),
    Rectangle(Point(0, 0), 100, 100),
)

warrior = Warrior(
    "Gerran",
    Point(50, 100),
    Rectangle(Point(0, 0), 100, 100),
)

healer = Healer(
    "Sorakan",
    Point(50, 50),
    Rectangle(Point(0, 0), 100, 100),
)

tanky = Tank(
    "tanky",
    Point(70, 50),
    Rectangle(Point(0, 0), 100, 100),
)

minion1 = Minion(
    "m1",
    Point(200, 500),
    Rectangle(Point(0, 0), 100, 100),
)

minion2 = Minion(
    "m2",
    Point(200, 500),
    Rectangle(Point(0, 0), 100, 100),
)

b1 = Buldozer(
    "b1",
    Point(200, 500),
    Rectangle(Point(0, 0), 100, 100),
)

heroes = [mage, healer, warrior, tanky]
monsters = [minion1, minion2, b1]

print("héros", heroes)
print("monstres", monsters)

warrior.attack(b1)
mage.performSkill(minion1)
