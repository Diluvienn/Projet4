"""This module contains the definition of the Match class, which represents a match
in a chess tournament. It provides methods to initialize a match with players and scores,
simulate playing the match, and obtain a string representation of the match.

Classes:
    Match: A class representing a match in a chess tournament.

Usage:
    # Create a Match instance
    # Play the match
    # Get the string representation of the match
"""

import datetime
import random

possible_score = [(0, 1), (0.5, 0.5), (1, 0)]


class Match:
    """A class representing a match in a chess tournament."""

    def __init__(self, players):

        self.players = players
        self.result = None

    def __str__(self):
        player1_name = f"{list(self.players.keys())[0].firstname} {list(self.players.keys())[0].lastname}"
        player2_name = f"{list(self.players.keys())[1].firstname} {list(self.players.keys())[1].lastname}"
        return (f"Match: {player1_name} vs {player2_name}, Scores: {self.players[list(self.players.keys())[0]]}-"
                f"{self.players[list(self.players.keys())[1]]}")

    def play_match(self):
        # Génération aléatoire du résultat du match
        result = random.choice(["win", "loss", "draw"])
        # Assign the match result to the instance variable self.result
        self.result = result
        for player, score in self.players.items():

        # Mise à jour des scores des joueurs en fonction du résultat
            if result == "win":
                winning_player = max(self.players, key=self.players.get)  # Trouver le joueur avec le score le plus élevé
                self.players[winning_player] += 1  # Incrémenter le score du joueur gagnant
            elif result == "loss":
                losing_player = min(self.players, key=self.players.get)  # Trouver le joueur avec le score le plus bas
                self.players[losing_player] += 1  # Incrémenter le score du joueur perdant
            elif result == "draw":
                for player in self.players:
                    self.players[player] += 0.5  # Ajouter 0.5 aux scores de tous les joueurs

            # # Enregistrement du résultat du match dans la variable match.result
            # for player, score in self.players.items():
            #     print(f"Joueur : {player.firstname} {player.lastname}, Score : {score}")

            return result

    def has_player(self, player):
        """Check if the given player is participating in this match."""
        return player in self.players

if __name__ == "__main__":
    pass
