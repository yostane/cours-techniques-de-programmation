class Human:
    # x est une propriété ou variable statique
    x = 0

    def __init__(self, name) -> None:
        self.name = name

    def say_name(self):
        print("name", self.name)

    @staticmethod
    def say_hello():
        """Ceci est une méthode statique (il n'a pas de self)"""
        print("hello")


# Appel de la méthode statique et utilisation de la propriété statique
Human.say_hello()
print(Human.x)
Human.x = 200
print(Human.x)

h1 = Human("Garen")
h1.say_name()
