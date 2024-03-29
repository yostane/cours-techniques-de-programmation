class Fruit:
    def __init__(self) -> None:
        self.weight = 10

    def __str__(self) -> str:
        return f"Fruit: weight -> {self.weight}"


class Human:
    def __init__(self) -> None:
        self.hp = 10

    def eat(self, apple):
        print(f"miam la pomme {apple}")
        apple.weight = 1
        self.hp += 10

    def heal(self, human):
        print(f"Soin appliqué à {human}")
        human.hp += 3

    def __str__(self) -> str:
        return f"Human: hp -> {self.hp}"


a1 = Fruit()
a2 = Fruit()

h1 = Human()
h2 = Human()

h1.eat(a1)
h1.eat(a2)

h1.heal(h2)

print(h1, h2)
