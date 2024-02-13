class Watch:
    def __init__(self, hour, minute, is_mechanical) -> None:
        self.hour = hour
        self.minute = minute
        self.is_mechanical = is_mechanical
        self.is_worn = False

    def __str__(self) -> str:
        return f"Current time {self.hour}:{self.minute}"

    def add(self, minute):
        self.minute += minute
        while self.minute >= 60:
            self.minute -= 60
            self.hour += 1
            if self.hour >= 24:
                self.hour = 0


class Person:
    def __init__(self, name) -> None:
        self.name = name
        self.worn_watch = None

    def wear_watch(self, watch):
        if self.worn_watch == None and not watch.is_worn:
            self.worn_watch = watch
            watch.is_worn = True

    def remove_watch(self):
        if self.worn_watch != None:
            self.worn_watch.is_worn = False
            self.worn_watch = None


antoine = Person("Antoine")
cyril = Person("Cyril")

watch1 = Watch(12, 12, True)
antoine.wear_watch(watch1)

watch2 = Watch(11, 10, True)
cyril.wear_watch(watch1)
print("Montre portée par Cyrtil ?", cyril.worn_watch)

cyril.wear_watch(watch2)
print("Montre portée par Cyrtil ?", cyril.worn_watch)


watch1.add(50)
print("after add 50", watch1)

watch1.add(2000)
print("after add 2000", watch1)
