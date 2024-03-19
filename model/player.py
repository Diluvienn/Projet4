"""
This module contains the definition of the Player class, which represents a player
with a first name, last name, birth date, and score. It also includes a function
to validate the format of a date string.

Classes:
    Player: A class representing a player with a first name, last name, birth date, and score.

Functions:
    validate_date_format: Validate the format of a date string in 'dd-mm-yyyy' format.

Usage:
    from formatvalidator import validate_date_format
    from player import Player

    # Create a player instance
    player = Player("John", "Doe", "01-01-1990", "AB12345")
"""
import os
import json

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

    def to_json(self):
        return {
            'firstname': self.firstname,
            'lastname': self.lastname,
            'birth': self.birth,
            'national chess ID': self.national_chess_id
        }


class PlayerRepository:
    def __init__(self, filename='players.json'):
        data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
        self.filename = os.path.join(data_dir, filename)


    def add_player(self, player):
        # Chargez d'abord les joueurs existants depuis le fichier
        players = self.load_players()

        # Ajoutez le nouveau joueur à la liste
        players.append(player.to_json())

        # Écrivez la liste mise à jour dans le fichier JSON
        with open(self.filename, 'w') as file:
            json.dump(players, file)

    def load_players(self):
        # Si le fichier n'existe pas encore, retournez une liste vide
        if not os.path.exists(self.filename):
            return []

        # Chargez les joueurs à partir du fichier JSON
        with open(self.filename, 'r') as file:
            players = json.load(file)
        return players

    # def load_players(self):
    #     with open(self.filename, 'r') as file:
    #         players = json.load(file)
    #     return players

    # Méthode pour récupérer un joueur spécifique à partir de son index dans la liste
    def get_player_by_index(self, index):
        players = self.load_players()
        player_data = players[index]
        print(player_data)
        player_instance = Player(player_data['firstname'], player_data['lastname'], player_data['birth'],
                                 player_data['national chess ID'])
        return player_instance

    # def add_player(self, player):
    #     with open(self.filename, 'a') as file:
    #         json.dump(player.to_json(), file)
    #         file.write('\n')


if __name__ == "__main__":
    pass
