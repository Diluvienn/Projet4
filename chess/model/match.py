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

import random

from model.player import Player

possible_score = [(0, 1), (0.5, 0.5), (1, 0)]


class Match:
    """A class representing a match in a chess tournament."""

    def __init__(self, players):

        self.players = players
        self.result = None

    def to_json(self):
        # Convertir les clés en chaînes de caractères pour les noms des joueurs
        players_json = {f"{player.firstname} {player.lastname}": score for player, score in self.players.items()}

        # Créer un dictionnaire contenant les données du match
        match_json = {
            "players": players_json
        }

        return match_json

    @classmethod
    def from_json(cls, match_data):
        # Récupérer les données des joueurs depuis le JSON
        players_data = match_data["players"]

        # Créer un dictionnaire pour stocker les joueurs et leurs scores
        players = {}

        # Parcourir les données des joueurs
        for player_name, score in players_data.items():
            # Ajouter le joueur et son score au dictionnaire
            players[player_name] = score

        # Créer l'objet Match avec les joueurs et leurs scores
        match = cls(players)

        return match

    # @classmethod
    # def from_json(cls, match_data):
    #     # Récupérer les données du match depuis le JSON
    #     players_json = match_data["players"]
    #
    #     # Convertir les noms des joueurs en objets Player et récupérer les scores
    #     players = {}
    #     for player_name, score in players_json.items():
    #         player_firstname, player_lastname = player_name.split()
    #         player_data = players_json[player_name]
    #         birth = player_data["birth"]
    #         national_chess_id = player_data["national_chess_id"]
    #         player = Player(player_firstname, player_lastname, birth, national_chess_id)
    #         players[player] = score
    #
    #     # Récupérer le résultat du match
    #     result = match_data["result"]
    #
    #     # Créer une instance de Match avec les données récupérées
    #     match_instance = cls(players, result)
    #     return match_instance

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
        for _, _ in self.players.items():

            # Mise à jour des scores des joueurs en fonction du résultat
            if result == "win":
                winning_player = max(self.players,
                                     key=self.players.get)  # Trouver le joueur avec le score le plus élevé
                self.players[winning_player] += 1  # Incrémenter le score du joueur gagnant
            elif result == "loss":
                losing_player = min(self.players, key=self.players.get)  # Trouver le joueur avec le score le plus bas
                self.players[losing_player] += 1  # Incrémenter le score du joueur perdant
            elif result == "draw":
                for player in self.players:
                    self.players[player] += 0.5  # Ajouter 0.5 aux scores de tous les joueurs

            return result


if __name__ == "__main__":
    pass
