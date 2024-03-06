from player import Player
from match import Match
from tournament import Tournament
from faker import Faker
import random

fake = Faker()

# Fonction pour générer une date de naissance aléatoire
def random_birthdate():
    year = random.randint(1970, 2000)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return f"{day:02d}-{month:02d}-{year}"

# Fonction pour créer un joueur aléatoire
def random_player():
    first_name = fake.first_name()
    last_name = fake.last_name()
    birth = random_birthdate()
    return first_name, last_name, birth

# Création d'une instance de Tournoi
tournament = Tournament("Chess Tournament", "City", "01-01-2023", "11-02-2023")

# Création de 6 joueurs aléatoires
for _ in range(6):
    first_name, last_name, birth = random_player()
    random_player_instance = Player(first_name, last_name, birth)
    tournament.add_player(random_player_instance)
print(tournament.get_players())
