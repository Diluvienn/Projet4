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
import random
import itertools

from typing import Set, Tuple, Dict, List

from model.round import Round
from model.match import Match
from model.player import Player


class Tournament:
    """A class representing a chess tournament."""

    def __init__(self, name: str, place: str, date_start: str, date_end: str, rounds: int = 4, director_notes: str = "",
                 current_round: int = 0):
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
        self.rounds = []
        self.director_notes: str = director_notes
        self.current_round: int = current_round
        self.players_score: Dict[str, int] = {}
        self.players_list: List[str] = list(self.players_score.keys())
        self.rounds_list = []
        self.played_pairs: Set[Tuple[Player, Player]] = set()

    def tournament_to_json(self):
        """Converts tournament data to a JSON-compatible dictionary.

        Returns:
            dict: A dictionary containing tournament information in a JSON-compatible format.
                  Keys include 'name', 'place', 'date_start', 'date_end', 'rounds', 'current_round',
                  'players_list', 'players_score', and 'director_note'.
        """
        rounds_count = len(self.rounds)  # Calculer le nombre de tours
        return {
            'name': self.name,
            'place': self.place,
            'date_start': self.date_start,
            'date_end': self.date_end,
            'rounds_count': rounds_count,
            'rounds': [round.to_json() for round in self.rounds],
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

    def add_round(self, num_rounds):
        num_rounds = int(num_rounds)  # Convertir en entier
        for i in range(num_rounds):
            round_name = f"Round {i + 1}"
            round_instance = Round(self, round_name)  # Passer le nom du tour en tant qu'argument
            self.rounds.append(round_instance)

    def generate_pairs_for_round(self):

        # Générer les paires pour le premier round
        if self.current_round == 0:
            all_pairs = list(itertools.combinations(self.players_list, 2))
            random.shuffle(all_pairs)  # Mélanger aléatoirement les paires

            round_matches = []
            paired_players = set()  # Pour suivre les joueurs déjà appariés

            for pair in all_pairs:
                player1, player2 = pair
                # Vérifier si les deux joueurs sont déjà appariés
                if player1 in paired_players or player2 in paired_players:
                    continue

                match_instance = Match({player1: 0, player2: 0})
                round_matches.append(match_instance)
                # Jouer le match
                result = match_instance.play_match()

                # Mettre à jour les paires déjà jouées et les joueurs appariés
                self.played_pairs.add((player1, player2))
                self.played_pairs.add((player2, player1))
                paired_players.add(player1)
                paired_players.add(player2)

            # Enregistrez les paires de matchs générées pour ce round
            self.rounds[self.current_round].matches.extend(round_matches)

        else:
            # Classer les joueurs par score
            sorted_players = sorted(self.players_list, key=lambda x: x.score, reverse=True)

            # Associer les joueurs pour les rounds suivants
            round_matches = []
            while len(sorted_players) >= 2:
                player1 = sorted_players[0]

                # Vérifier si les deux derniers joueurs peuvent former une paire
                if len(sorted_players) == 2:
                    player2 = sorted_players[1]
                else:
                    player2 = None
                    # Chercher le joueur avec le score le plus proche
                    min_diff = float('inf')
                    for j in range(1, len(sorted_players)):
                        if (player1, sorted_players[j]) not in self.played_pairs and \
                                (sorted_players[j], player1) not in self.played_pairs:
                            score_diff = abs(player1.score - sorted_players[j].score)
                            if score_diff < min_diff:
                                min_diff = score_diff
                                player2 = sorted_players[j]
                    if player2 is None:
                        break  # Si aucun joueur n'a été trouvé, sortir de la boucle

                match_instance = Match({player1: 0, player2: 0})
                round_matches.append(match_instance)
                result = match_instance.play_match()

                # Mettre à jour les paires déjà jouées
                self.played_pairs.add((player1, player2))
                self.played_pairs.add((player2, player1))

                # Retirer les joueurs associés de la liste des joueurs triés
                sorted_players.remove(player1)
                if len(sorted_players) > 0:
                    sorted_players.remove(player2)

            # Enregistrez les paires de matchs générées pour ce round
            self.rounds[self.current_round].matches.extend(round_matches)

    def update_played_pairs(self):
        if self.current_round > 0:
            previous_round_matches = self.rounds[self.current_round - 1].matches
            for match in previous_round_matches:
                player1 = list(match.players.keys())[0]
                player2 = list(match.players.keys())[1]
                # Ajouter la paire de joueurs à l'ensemble de paires jouées pour ce round
                self.played_pairs.add((player1, player2))
                self.played_pairs.add((player2, player1))



    def __str__(self):
        """Return a string representation of the tournaments."""
        return (f"Tournament: {self.name}\nLocation: {self.place}\nStart: {self.date_start}\n"
                f"End: {self.date_end}\nRounds: {self.rounds}\n"
                f"Current Round: {self.current_round}\nDirector Notes: {self.director_notes}")


def calculate_leaderboard(tournament):
    # Créez une liste de tuples (joueur, score total)
    leaderboard = [(player, player.calculate_total_score(tournament.rounds)) for player in tournament.players_list]
    # Triez la liste en fonction du score total (en ordre décroissant)
    sorted_leaderboard = sorted(leaderboard, key=lambda x: x[1], reverse=True)

    tournament.players_score = {f"{player.firstname} {player.lastname}": score for player, score in sorted_leaderboard}

    # Affichez le classement
    print(f"Classement fin du round {tournament.current_round +1} :")
    for i, (player, score) in enumerate(sorted_leaderboard, start=1):
        print(f"{i}. {player.firstname} {player.lastname} : {score} points")
    print("*" * 100)



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
        tournament_data = tournament.tournament_to_json()
        tournament_data["players_list"] = [player.to_json() for player in tournament.players_list]
        tournament_data["rounds"] = [round.to_json() for round in tournament.rounds]
        tournaments.append(tournament_data)

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

        Returns: List[dict]: A list of dictionaries containing details of the tournaments including players and their
        scores, sorted by name.
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
