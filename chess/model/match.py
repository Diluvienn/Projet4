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
    def from_json(cls, match_data, tournament):
        # Récupérer les données des joueurs depuis le JSON
        players_data = match_data["players"]

        # Créer un dictionnaire pour stocker les objets Player et leurs scores
        players = {}

        # Convertir les noms des joueurs en objets Player
        for player_name, score in players_data.items():
            player_firstname, player_lastname = player_name.split()
            player = find_player(tournament, player_firstname, player_lastname)
            if player:
                players[player] = score
            else:
                print(f"Joueur introuvable dans la liste des joueurs du tournoi : {player_name}")

        # Créer l'objet Match avec les joueurs (objets Player) et leurs scores
        match = cls(players)
        return match

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

        # Inverser aléatoirement l'ordre des joueurs
        players_list = list(self.players.keys())
        random.shuffle(players_list)
        player1, player2 = players_list

        # Mise à jour des scores des joueurs en fonction du résultat
        if result == "win":
            winning_player = player1 if random.random() < 0.5 else player2
            self.players[winning_player] += 1
        elif result == "loss":
            losing_player = player1 if random.random() < 0.5 else player2
            self.players[losing_player] += 1
        elif result == "draw":
            for player in self.players:
                self.players[player] += 0.5

        return result
        # for _, _ in self.players.items():
        #
        #     # Mise à jour des scores des joueurs en fonction du résultat
        #     if result == "win":
        #         winning_player = max(self.players,
        #                              key=self.players.get)  # Trouver le joueur avec le score le plus élevé
        #         self.players[winning_player] += 1  # Incrémenter le score du joueur gagnant
        #     elif result == "loss":
        #         losing_player = min(self.players, key=self.players.get)  # Trouver le joueur avec le score le plus bas
        #         self.players[losing_player] += 1  # Incrémenter le score du joueur perdant
        #     elif result == "draw":
        #         for player in self.players:
        #             self.players[player] += 0.5  # Ajouter 0.5 aux scores de tous les joueurs
        #     return result


def find_player(tournament, player_firstname, player_lastname):
    for p in tournament.players_list:
        if p.firstname == player_firstname and p.lastname == player_lastname:
            return p
    return None



if __name__ == "__main__":
    pass