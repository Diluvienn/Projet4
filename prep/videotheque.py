vhf = []
dvd = []
films = [
    ("Blade Runner (1982)", "vhf"),
    ("Alien : Le 8ème Passager (1979)", "vhf"),
    ("2001 : L'Odyssée de l'espace (1968)", "VhF"),
    ("Matrix (1999)", "DVD"),
    ("Interstellar (2014)", "dvD"),
    ("L'Empire contre-attaque (1980)", "vhf"),
    ("Retour vers le futur (1985)", "vhf"),
    ("La Guerre des Étoiles (1977)", "vhf"),
    ("L'Armée des 12 singes (1995)", "dVd"),
    ("Terminator 2 : Le Jugement dernier (1991)", "DVD"),
]


class Film:
    def __init__(self, name, date, place, type):
        self.name = name
        self.date = date
        self.place = place
        self.type = type


class VHF(Film):
    def __init__(self, name, date, place, type=vhf):
        super().__init__(name, date, place, type)

    def add_vhf(self):
        vhf.append(self.name)
    print("je suis un VHF")


class DVD(Film):
    def __init__(self, name, date, place, type=dvd):
        super().__init__(name, date, place, type)
    def add_dvd(self):
        dvd.append(self.name)
    print("je suis un DVD")

def tri_alpha():
    print(film.sort())
