"""
Module for managing player information and storage.

This module defines a Player class representing individual chess players and a PlayerRepository class
for managing player data storage and retrieval.

Classes:
    - Player: Represents a chess player with attributes including first name, last name, date of birth,
      and national chess ID.
    - PlayerRepository: Manages the storage and retrieval of player information.
"""


class Player:
    """Player"""

    def __init__(self, firstname: str, lastname: str, birth: str, national_chess_id: str):
        self.firstname = firstname.title()
        self.lastname = lastname.title()
        self.birth = birth
        self.national_chess_id = national_chess_id
        self.score = 0

    def __str__(self):
        return (f"Prénom : {self.firstname} "
                f"nom : {self.lastname} "
                f"(Date de naissance: {self.birth}, "                
                f"Identifiant national: {self.national_chess_id})")

    def fullname(self):
        """Retourne le nom complet du joueur."""
        return f"{self.firstname} {self.lastname}"

    def calculate_total_score(self, rounds, previous_scores=None):
        total_score = self.score

        for round in rounds:
            for match in round.matches:
                if self in match.players:
                    total_score += match.players[self]
        return total_score

    def to_json(self):
        """Converts player data to a JSON-compatible dictionary.

        Returns:
            dict: A dictionary containing player information in a JSON-compatible format.
                  Keys include 'firstname', 'lastname', 'birth', and 'national chess ID'.
        """
        return {
            'firstname': self.firstname,
            'lastname': self.lastname,
            'birth': self.birth,
            'national chess ID': self.national_chess_id
        }

    @classmethod
    def from_json(cls, json_data):
        """Crée un objet Player à partir des données JSON.

        Args:
            json_data (dict): Les données JSON représentant le joueur.

        Returns:
            Player: L'objet Player créé à partir des données JSON.
        """
        # Extraire les données du JSON
        firstname = json_data['firstname']
        lastname = json_data['lastname']
        birth = json_data['birth']
        national_chess_id = json_data['national chess ID']

        player = cls(firstname, lastname, birth, national_chess_id)

        return player
