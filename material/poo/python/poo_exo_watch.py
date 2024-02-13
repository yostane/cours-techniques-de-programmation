class Watch:
    def __init__(self, hour, minute, is_mechanical) -> None:
        self.hour = hour
        self.minute = minute
        self.is_mechanical = is_mechanical
        self.is_worn = False


class Person:
    def __init__(self, name) -> None:
        self.name = name
        self.worn_watch = None

    def wear_watch(self, watch):
        if self.worn_watch != None and not watch.is_worn:
            self.worn_watch = watch

    def remove_watch(self):
        if self.worn_watch != None:
            self.worn_watch.is_worn = None
            self.worn_watch = None
