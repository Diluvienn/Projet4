"""
This module contains the definition of the Tournament class, which represents a chess tournament.
It also includes functions to add players, update scores, and retrieve player information.

Classes:
    Tournament: A class representing a chess tournament.

Functions:
    None

Usage:
    # Create a tournament instance
    # Add players to the tournament
    # Update scores based on match results
    # Get player scores
    # Get all scores
        # Print tournament information
"""
import os
import json

from .player import Player
from typing import List, Dict


class Tournament:
    """A class representing a chess tournament."""

    def __init__(self, name: str, place: str, date_start: str, date_end: str, rounds: int = 4, current_round: int = 1):
        """Initialize a Tournament object.

       Args:
           name (str): The name of the tournament.
           place (str): The location of the tournament.
           date_start (str): The start date of the tournament (format: 'dd-mm-yyyy').
           date_end (str): The end date of the tournament (format: 'dd-mm-yyyy').
           rounds (int, optional): The number of rounds in the tournament. Defaults to 4.
           current_round (int, optional): The current round of the tournament. Defaults to 1.

       Raises:
           ValueError: If the date formats are invalid.
       """

        self.name: str = name
        self.place: str = place
        self.date_start: str = date_start
        self.date_end: str = date_end
        self.rounds: int = rounds
        self.current_round: int = current_round
        self.players_list: List[str] = []
        self.players_score: Dict[str, int] = {}
        self.director_notes: str = ""


    def tournament_to_json(self):
        return {
            'name': self.name,
            'place': self.place,
            'date_start': self.date_start,
            'date_end': self.date_end,
            'rounds': self.rounds,
            'current_round': self.current_round,
            'players_list': self.players_list,
            'players_score': self.players_score,
            'director_note': self.director_notes
        }

    def add_player(self, player):
        """Add a player to the tournament.

        Args:
            player (Player): The player object to be added to the tournament.

        Returns:
            None
        """
        player_name = f"{player.firstname} {player.lastname}"
        self.players_list.append(player_name)
        print(f"self.players_list : {self.players_list}")
        self.players_score[player_name] = 0
        print(f"self.player_score : {self.players_score}")


    def get_players(self):
        """Get the list of players registered for the tournament.

        Returns:
            list: A list of formatted player names.
        """
        # return [f"{player.firstname} {player.lastname}" for player in self.players_list]
        return self.players_list

    def add_director_notes(self, note):
        """Add notes from the tournament director.

        Args:
            note (str): The note to be added.

        Returns:
            None
        """
        self.director_notes += note + "\n"

    def update_scores(self, match):
        """Update the scores of players based on the match results.

        Args:
            match (Match): The match object containing the match results.

        Returns:
            None
        """
        players, scores = match.players, match.scores
        print("Players in the match:", players)
        print("Scores in the match:", scores)
        # Mettre à jour les scores des joueurs
        for player, score in zip(players, scores):
            # Vérifier si le joueur est dans le dictionnaire player_score
            if player in self.players_score:
                # Mettre à jour le score du joueur en additionnant le score du match
                self.players_score[player] += score
            else:
                # Si le joueur n'est pas déjà dans le dictionnaire, l'ajouter avec le score du match
                self.players_score[player] = score


    def get_player_score(self, player):
        """Get the score of a player.

       Args:
           player (str): The name of the player.

       Returns:
           int: The score of the player. Returns 0 if the player is not found in the scores dictionary.
       """
        return self.players_score.get(player, 0)

    def get_all_scores(self):
        """Get all scores of players in the tournament.

        Returns:
            str: A string containing the scores of all players in the tournament.
        """
        scores_string = "Tabelau des scores :\n"
        for player_name, score in self.players_score.items():
            scores_string += f"{player_name}: {score}\n"
        return scores_string

    def __str__(self):
        """Return a string representation of the tournaments."""
        return (f"Tournament: {self.name}\nLocation: {self.place}\nStart: {self.date_start}\n"
                f"End: {self.date_end}\nRounds: {self.rounds}\n"
                f"Current Round: {self.current_round}\nDirector Notes: {self.director_notes}")


class TournamentRepository:
    def __init__(self, filename='tournament.json'):
        data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
        self.filename = os.path.join(data_dir, filename)

    def add_tournament(self, tournament):
        tournaments = self.load_tournaments()
        tournaments.append(tournament.tournament_to_json())

        with open(self.filename, 'w') as file:
            json.dump(tournament.tournament_to_json(), file, indent=4)

    def load_tournaments(self):
        # Si le fichier n'existe pas encore, retournez une liste vide
        if not os.path.exists(self.filename):
            return []

        # Chargez les tournois à partir du fichier JSON
        with open(self.filename, 'r') as file:
            tournaments = json.load(file)
        return tournaments

    def get_tournaments_by_alphabetical_order(self):
        tournaments = self.load_tournaments()
        sorted_tournaments = sorted(tournaments, key=lambda x: x['name'])
        formatted_output = []
        for tournament_data in sorted_tournaments:
            formatted_output.append(f"{tournament_data['name']}")
        return formatted_output

    def get_tournament_details(self):
        tournaments = self.load_tournaments()
        sorted_tournaments = sorted(tournaments, key=lambda x: x['name'])
        formatted_output = []
        for tournament_data in sorted_tournaments:
            formatted_output.append(
                f"Name: {tournament_data['name']}, Place: {tournament_data['place']}, Date Start: {tournament_data['date_start']}, Date End: {tournament_data['date_end']}")
        return formatted_output

if __name__ == "__main__":
    pass
