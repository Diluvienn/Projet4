"""
Module for managing tournament information and storage.

This module defines a Tournament class representing individual chess tournaments and a TournamentRepository class
for managing tournament data storage and retrieval.

Classes:
    - Tournament: Represents a chess tournament with attributes including name, place, start date, end date,
      number of rounds, current round, player list, player scores, and director notes.
    - TournamentRepository: Manages the storage and retrieval of tournament information.
"""
import os
import json

from typing import List, Dict


class Tournament:
    """A class representing a chess tournament."""

    def __init__(self, name: str, place: str, date_start: str, date_end: str, rounds: int = 4, director_notes: str = "",
                 current_round: int = 1):
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
        self.director_notes: str = director_notes
        self.current_round: int = current_round
        self.players_list: List[str] = []
        self.players_score: Dict[str, int] = {}

    def tournament_to_json(self):
        """Converts tournament data to a JSON-compatible dictionary.

        Returns:
            dict: A dictionary containing tournament information in a JSON-compatible format.
                  Keys include 'name', 'place', 'date_start', 'date_end', 'rounds', 'current_round',
                  'players_list', 'players_score', and 'director_note'.
        """
        return {
            'name': self.name,
            'place': self.place,
            'date_start': self.date_start,
            'date_end': self.date_end,
            'rounds': self.rounds,
            'current_round': self.current_round,
            'director_note': self.director_notes,
            'players_list': self.players_list,
            'players_score': self.players_score

        }

    def get_players(self):
        """Get the list of players registered for the tournament.

        Returns:
            list: A list of formatted player names.
        """
        return self.players_list


    def update_scores(self, match):
        """Update the scores of players based on the match results.

        Args:
            match (Match): The match object containing the match results.

        Returns:
            None
        """
        players, scores = match.players, match.scores
        # Mettre à jour les scores des joueurs
        for player, score in zip(players, scores):
            if player in self.players_score:
                self.players_score[player] += score
            else:
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
        scores_string = "**********Tabelau des scores :**********\n"
        for player_name, score in self.players_score.items():
            scores_string += f"{player_name}: {score}\n"
        return scores_string

    def __str__(self):
        """Return a string representation of the tournaments."""
        return (f"Tournament: {self.name}\nLocation: {self.place}\nStart: {self.date_start}\n"
                f"End: {self.date_end}\nRounds: {self.rounds}\n"
                f"Current Round: {self.current_round}\nDirector Notes: {self.director_notes}")


class TournamentRepository:
    """Repository for managing tournament data storage and retrieval."""

    def __init__(self, filename='tournament.json'):
        """Initialize the TournamentRepository.

        Args:
            filename (str, optional): Name of the JSON file to store tournament data. Defaults to 'tournament.json'.
        """
        data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
        self.filename = os.path.join(data_dir, filename)

    def add_tournament(self, tournament):
        """Add a tournament to the repository.

        Args:
            tournament (Tournament): The tournament object to be added to the repository.

        """
        tournaments = self.load_tournaments()
        tournaments.append(tournament.tournament_to_json())

        with open(self.filename, 'w') as file:
            json.dump(tournaments, file, indent=4)

    def load_tournaments(self):
        """Load tournaments from the JSON file.

       Returns:
           List[dict]: A list of dictionaries containing tournament information loaded from the JSON file.
                       If the file does not exist, an empty list is returned.
       """
        if not os.path.exists(self.filename):
            return []

        with open(self.filename, 'r') as file:
            tournaments = json.load(file)
        return tournaments

    def update_tournament_scores(self, tournament):
        """Update the scores of a specific tournament.

        Args:
            tournament_name (str): The name of the tournament to update.
            new_scores (dict): The new scores for the tournament players.
                This should be a dictionary where keys are player names and values are their scores.

        """
        # Chargez tous les tournois existants
        tournaments = self.load_tournaments()

        # Recherchez le tournoi spécifique par son nom
        for index, stored_tournament in enumerate(tournaments):
            if stored_tournament['name'] == tournament.name:
                # Mettez à jour les scores du tournoi spécifique
                tournaments[index] = tournament.tournament_to_json()
                break

        # Écrivez la liste mise à jour des tournois dans le fichier JSON
        with open(self.filename, 'w') as file:
            json.dump(tournaments, file, indent=4)
    def get_tournaments_by_alphabetical_order(self):
        """Get tournaments from the repository sorted alphabetically by name.

        Returns:
            List[str]: A list of tournament names sorted alphabetically.

        Note:
            This method retrieves tournament data from the repository, sorts the tournaments alphabetically
            by name, and returns a list of tournament names.
        """
        tournaments = self.load_tournaments()
        sorted_tournaments = sorted(tournaments, key=lambda x: x['name'])
        formatted_output = []
        for tournament_data in sorted_tournaments:
            formatted_output.append(f"{tournament_data['name']}")
        return formatted_output

    def get_tournament_details(self):
        """Get details of the tournaments including players and their scores, sorted by name.

        Returns:
            List[dict]: A list of dictionaries containing details of the tournaments including players and their scores, sorted by name.
        """
        tournaments = self.load_tournaments()
        formatted_output = []

        # Trier les tournois par ordre alphabétique du nom
        sorted_tournaments = sorted(tournaments, key=lambda x: x["name"])

        for tournament_data in sorted_tournaments:
            tournament_details = {
                "name": tournament_data["name"],
                "place": tournament_data["place"],
                "date_start": tournament_data["date_start"],
                "date_end": tournament_data["date_end"],
                "director_note": tournament_data["director_note"]
            }

            players_scores = []
            for player in tournament_data["players_list"]:
                player_score = {
                    "name": player,
                    "score": tournament_data.get("players_score", {}).get(player, 0)
                    # Get player's score or default to 0 if not found
                }
                players_scores.append(player_score)

            tournament_details["players_scores"] = players_scores
            formatted_output.append(tournament_details)

        return formatted_output



if __name__ == "__main__":
    pass
    # def add_player(self, player):
    #     """Add a player to the tournament.
    #
    #     Args:
    #         player (Player): The player object to be added to the tournament.
    #
    #     """
    #     player_name = f"{player.firstname} {player.lastname}"
    #     self.players_list.append(player_name)
    #     print(f"self.players_list : {self.players_list}")
    #     self.players_score[player_name] = 0
    #     print(f"self.player_score : {self.players_score}")

    # def add_director_notes(self, note):
    #     """Add notes from the tournament director.
    #
    #     Args:
    #         note (str): The note to be added.
    #
    #     Returns:
    #         None
    #     """
    #     self.director_notes += note + "\n"
