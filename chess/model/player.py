"""
Module for managing player information and storage.

This module defines a Player class representing individual chess players and a PlayerRepository class
for managing player data storage and retrieval.

Classes:
    - Player: Represents a chess player with attributes including first name, last name, date of birth,
      and national chess ID.
    - PlayerRepository: Manages the storage and retrieval of player information.
"""

from utils.formatvalidator import validate_date_format, validate_national_chess_id_format


class Player:
    """Player"""

    def __init__(self, firstname: str, lastname: str, birth: str, national_chess_id: str):
        if not firstname.isalpha():
            raise ValueError("Firstname must contain only letters without accent or hypen..")
        if not lastname.isalpha():
            raise ValueError("Lastname must contain only letters without accent or hypen.")
        if not validate_date_format(birth):
            raise ValueError("Invalid date format. Please use 'dd-mm-yyyy' format.")
        if not validate_national_chess_id_format(national_chess_id):
            raise ValueError("Invalid national chess ID format. Please use 'AB12345' format.")
        self.firstname = firstname.capitalize()
        self.lastname = lastname.capitalize()
        self.birth = birth
        self.national_chess_id = national_chess_id
        self.score = 0

    def full_name(self):
        """Retourne le nom complet du joueur."""
        return f"{self.firstname} {self.lastname}"

    def calculate_total_score(self, rounds, previous_scores=None):
        total_score = self.score
        # total_score = self.score if previous_scores is None else previous_scores.get(self.full_name(), self.score)

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

        # Créer l'objet Player avec les données récupérées
        player = cls(firstname, lastname, birth, national_chess_id)

        return player
