class User:
    """CamelCase pour les noms de classes"""

    def __init__(self):
        """initialiseur ou constructeur.
        Son usage: Permet d'initialiser les propriétés"""
        self.first_name = "Naruto"
        self.last_name = "Uzumaki"
        self.birth_year = 1800

    def __str__(self) -> str:
        """Représentation textuelle. Utilisée surtout pour l'affichage dans les print"""
        return self.first_name + " " + self.last_name + " " + str(self.birth_year)

    def launch_attack(self):
        print(self.first_name, "launches an attack")


u1 = User()
u2 = User()
u3 = User()

print(u1, u1.first_name, u1.last_name)

u2.birth_year += 20
u2.first_name = "Boruto"
print(u2, u2.first_name, u2.birth_year)

u2.launch_attack()
