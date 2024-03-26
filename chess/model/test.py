from model.match import Match
from model.player import Player

# test_match.py

from match import Match  # Assurez-vous que le nom du fichier et la classe correspondent

# Créez une instance de Match avec des données de test
players = {
    Player("John", "Doe", "01-01-2020", "AB12345"): 3.5,
    Player("Jane", "Smith", "22-01-2021", "ZP12345"): 2.0
}
test_match = Match(players)

# Appelez la méthode __str__() sur l'instance de Match et imprimez le résultat
print(str(test_match))
