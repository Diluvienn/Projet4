from player import Player
from match import Match


# Créer des instances de joueurs avec des données valides
try:
    player1 = Player("Durand", "Jean", "01-01-2000")
    print("Player 1 created successfully.")
except ValueError as e:
    print(f"Error creating player 1: {e}")

# Créer des instances de joueurs avec des données invalides
try:
    player2 = Player("tom", "John", "01-01-2000")
    print("Player 2 created successfully.")
except ValueError as e:
    print(f"Error creating player 2: {e}")


# Créer un match
match1 = Match(["Player1", "Player2"], [1, 2])

# Afficher les informations sur le match
print(match1)
