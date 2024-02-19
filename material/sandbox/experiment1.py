class Dog:
    """
    is_full: est rassasié
    breed: race
    """
    def __init__(self, breed):
        self.is_full = False
        self.breed = breed

class Cat:
    def say_miaou(self):
        print("miaou")

class Human:
    def __init__(self, name, dogs, cats):
        self.name = name
        self.dogs = dogs
        self.cats = cats

    def feed(self):
        """Nourrir"""
        for cat in self.cats:
            cat.say_miaou()
        for dog in self.dogs:
            if not dog.is_full:
                dog.is_full = True
            else:
                print(f"A déjà mangé : {dog.breed}")

d1 = Dog("Berget Allemand")
d2 = Dog("Caniche")
c1 = Cat()
d2.is_full = True

h = Human("dupont", [d1, d2, Dog("Husky")], [c1, Cat()])
h.feed()
h.feed()
