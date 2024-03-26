class Roue:
    pass


class Moteur:
    pass


class Voiture:
    def __init__(self, roues, moteur) -> None:
        if len(roues) < 3 or len(roues) > 5:
            raise Exception("Pass assez de roues")
        self.roues = roues
        self.moteur = moteur


class Suv(Voiture):
    pass


class Berline(Voiture):
    pass


class Personne:
    pass


class Mécanicien(Personne):
    pass


class Commercial(Personne):
    pass


class GarageAutomobile:
    def __init__(self, voitures, personnes) -> None:
        if len(personnes) == 0:
            raise Exception("Il faut au moins une personne")
        self.personnes = personnes
        self.voitures = voitures


personnes = [Mécanicien(), Commercial(), Mécanicien()]
roues1 = [Roue()] * 5
roues2 = [Roue()] * 3
moteur = Moteur()
voitures = [Berline(roues1, Moteur()), Suv(roues2, moteur)]

Berline([Roue()])

garage = GarageAutomobile(voitures, personnes)
GarageAutomobile([], [])
