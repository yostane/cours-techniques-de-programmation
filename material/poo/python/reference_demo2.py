items = [1, 2, 3, 4]


class SportRoom:
    def __init__(self, capacity, sport_name) -> None:
        self.capacity = capacity
        self.sport_name = sport_name

    def __str__(self) -> str:
        return f"Room for sport {self.sport_name}, with capacity {self.capacity}"


sp = SportRoom(10, "Climbing")


def show_items(to_show_items):
    to_show_items[2] = "Yo"
    print(to_show_items)


def show_sport_room(sport_room):
    sport_room.capacity = 3
    print(sport_room)


show_items(items)
show_sport_room(sp)

print(items)
print(sp)
