# typage dyamique: le type d'une variable ou argument peut changer
x = 10
x = "Hello"
print(x)

# snake case: say_hello
# camel case: sayHello


def say_hello(message: str) -> int:
    """le type des arguments est optionnel"""
    print("hello", message)
    return 10


say_hello("world")

u1 = {"first_name": "Naruto", "last_name": "Uzumaki", "birth_year": 1800}
print(u1, u1["birth_year"], u1["first_name"])
# Concéténation
u1["first_name"] = "Bor" + "uto"
# Addition ou incrémentation
u1["birth_year"] += 20
print(u1)
u2 = {"first_name": "Sasuke", "last_name": "Uchiha", "birth_year": 1800}
u2["birth_yar"] = 100
print(u2)
