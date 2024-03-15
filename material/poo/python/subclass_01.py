class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def eat(self):
        print("miam", self.name)


class Dog(Animal):
    # Pas besoin de redéfinir les méthodes qui ne changent pas
    pass


class Cat(Animal):
    def __init__(self, name, claw_length):
        super().__init__(name)
        self.claw_length = claw_length

    def say_miaou(self):
        print("miaou", self.name)


dog = Dog("Milou")
cat = Cat("miaouss", 10)

dog.eat()
cat.say_miaou()
print(cat.claw_length)
