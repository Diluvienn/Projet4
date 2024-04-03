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

from datetime import datetime
from typing import Dict, List
from unidecode import unidecode

from model.round import Round
from model.match import Match
from model.player import Player


class Tournament:
    """A class representing a chess tournament."""

    def __init__(self, name: str, place: str, date_start: str, date_end: str, rounds: int = 4,
                 director_notes: str = "", current_round: int = 0):
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
        self.played_pairs = set()

    def __getitem__(self, key):
        """Get an item from the tournament by key.

        Args:
            key: The key (or index) to retrieve the item.

        Returns:
            Any: The value associated with the key.

        Raises:
            KeyError: If the key is not found.
        """
        if key == 'name':
            return self.name
        elif key == 'place':
            return self.place
        elif key == 'date_start':
            return self.date_start
        elif key == 'date_end':
            return self.date_end
        elif key == 'rounds':
            return self.rounds
        elif key == 'director_notes':
            return self.director_notes
        elif key == 'current_round':
            return self.current_round
        elif key == 'players_score':
            return self.players_score
        elif key == 'players_list':
            return self.players_list
        elif key == 'played_pairs':
            return self.played_pairs
        else:
            raise KeyError(f"Invalid key: {key}")

    def to_json(self):
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
            'director_note': self.director_notes,
            'rounds': [round.to_json() for round in self.rounds],
            'current_round': self.current_round,
            'players_score': self.players_score,
            'played_pairs': [{'player1': pair[0].to_json(), 'player2': pair[1].to_json()} for pair in self.played_pairs]

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
            round_instance = Round(round_name)  # Passer le nom du tour en tant qu'argument
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
                # self.update_played_pairs()
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
                match_instance.play_match()

                # Mettre à jour les paires déjà jouées
                self.played_pairs.add((player1, player2))
                self.played_pairs.add((player2, player1))
                # self.update_played_pairs()

                # Retirer les joueurs associés de la liste des joueurs triés
                sorted_players.remove(player1)
                if len(sorted_players) > 0:
                    sorted_players.remove(player2)

            # Enregistrez les paires de matchs générées pour ce round
            self.rounds[self.current_round].matches.extend(round_matches)

    def play_tournament(self):
        while self.current_round <= len(self.rounds):
            current_round = self.rounds[self.current_round]

            print("*" * 100)
            print(f"Round {self.current_round + 1} :")
            # Définir l'heure de début du round
            self.rounds[self.current_round].start_time = datetime.now()

            # Générer les paires de matchs pour ce round
            self.generate_pairs_for_round()

            # Définir l'heure de début du round
            self.rounds[self.current_round].start_time = datetime.now()

            for match in current_round.matches:
                player1 = list(match.players.keys())[0]
                player2 = list(match.players.keys())[1]
                player1_name = f"{player1.firstname} {player1.lastname}"
                player2_name = f"{player2.firstname} {player2.lastname}"
                score1 = match.players[player1]
                score2 = match.players[player2]
                print(f"Match: {player1_name} vs {player2_name}, Scores: {score1}-{score2}")
                # print(f"Start Time: {current_round.start_time}, End Time: {current_round.end_time}")

                # Récupérer les scores précédents à partir des données du tournoi
                previous_scores = self.players_score if hasattr(self, 'players_score') else {}

            # Calculer et afficher le classement provisoire
            calculate_leaderboard(self, previous_scores)

            # Demander si vous voulez jouer le prochain round

            if self.current_round == (len(self.rounds) - 1):
                tournament_repository = TournamentRepository()
                tournament_repository.add_tournament(self)
                break

            play_next_round = input("Voulez-vous jouer le round suivant ? (y/n): ")
            while play_next_round not in ["y", "n"]:
                print("Veuillez effectuer un choix valide.")
                play_next_round = input("Voulez-vous jouer le round suivant ? (y/n): ")

            if play_next_round == "n":
                self.current_round += 1
                tournament_repository = TournamentRepository()
                tournament_repository.add_tournament(self)
                break

            self.current_round += 1

    @classmethod
    def from_json(cls, json_data):
        """Crée un objet Tournament à partir des données JSON.

        Args:
            json_data (dict): Les données JSON représentant le tournoi.

        Returns:
            Tournament: L'objet Tournament créé à partir des données JSON.
        """
        # Extraire les données du JSON
        name = json_data['name']
        place = json_data['place']
        date_start = json_data['date_start']
        date_end = json_data['date_end']
        current_round = json_data['current_round']
        director_notes = json_data['director_note']

        # Convertir les joueurs de JSON en objets Player
        players_list_data = json_data['players_list']
        players_list = [Player.from_json(player_data) for player_data in
                        players_list_data]  # Convertir en objets Player

        # Convertir les paires jouées de JSON en objets Player
        played_pairs_data = json_data.get('played_pairs', [])
        played_pairs = set()
        for pair_data in played_pairs_data:
            player1_data = pair_data['player1']
            player2_data = pair_data['player2']
            player1 = Player.from_json(player1_data)
            player2 = Player.from_json(player2_data)
            played_pairs.add((player1, player2))

        players_score = json_data['players_score']
        rounds_data = json_data['rounds']

        # Créer l'objet Tournament avec les données récupérées
        tournament = cls(name, place, date_start, date_end, director_notes, current_round)
        tournament.players_list = players_list
        tournament.players_score = players_score
        tournament.played_pairs = played_pairs
        tournament.current_round = current_round

        # Créer les objets Round à partir des données JSON
        rounds = [Round.from_json(round_data, tournament) for round_data in rounds_data]
        tournament.rounds = rounds
        return tournament

    def __str__(self):
        """Return a string representation of the tournaments."""
        return (f"Tournament: {self.name}\nLocation: {self.place}\nStart: {self.date_start}\n"
                f"End: {self.date_end}\nRounds: {self.rounds}\n"
                f"Current Round: {self.current_round}\nDirector Notes: {self.director_notes}")


def calculate_leaderboard(tournament, previous_scores=None):
    # Créez une liste de tuples (joueur, score total)
    leaderboard = [(player, player.calculate_total_score(tournament.rounds, previous_scores))
                   for player in tournament.players_list]
    # Triez la liste en fonction du score total (en ordre décroissant)
    sorted_leaderboard = sorted(leaderboard, key=lambda x: x[1], reverse=True)

    tournament.players_score = {f"{player.firstname} {player.lastname}": score for player, score in sorted_leaderboard}
    # Affichez le classement
    print(f"Classement fin du round {tournament.current_round + 1} :")
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
        tournament_data = tournament.to_json()

        # Convertir les joueurs en JSON
        players_json = []
        for player in tournament.players_list:
            player_json = player.to_json()
            players_json.append(player_json)
        tournament_data["players_list"] = players_json

        # Convertir les paires jouées en JSON
        played_pairs_json = []
        for pair in tournament.played_pairs:
            player1_json = pair[0].to_json()
            player2_json = pair[1].to_json()
            played_pair_json = {"player1": player1_json, "player2": player2_json}
            played_pairs_json.append(played_pair_json)
        tournament_data["played_pairs"] = played_pairs_json

        # Convertir les rounds en JSON
        rounds_json = []
        for round in tournament.rounds:
            round_json = round.to_json()
            rounds_json.append(round_json)
        tournament_data["rounds"] = rounds_json

        # Recherchez le tournoi existant et mettez à jour ses données s'il existe déjà
        for i, existing_tournament in enumerate(tournaments):
            if existing_tournament["name"] == tournament.name:
                tournaments[i] = tournament_data
                break
        else:
            # Si le tournoi n'existe pas, ajoutez-le simplement à la liste
            tournaments.append(tournament_data)

        # Enregistrez la liste mise à jour des tournois dans le fichier
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

    def find_unfinished_tournaments(self):
        tournaments = self.load_tournaments()
        unfinished_tournaments = []

        for tournament in tournaments:
            round_count = len(tournament["rounds"])
            round_count = int(round_count)
            if tournament["current_round"] < (round_count - 1):
                unfinished_tournaments.append(tournament)
        return unfinished_tournaments

    def resume_tournament(self):
        unfinished_tournaments = self.find_unfinished_tournaments()
        if not unfinished_tournaments:
            print("Aucun tournoi non terminé trouvé.")
            return
        print("Tournois non terminés :")
        for idx, tournament in enumerate(unfinished_tournaments, 1):
            print(f"{idx}. {tournament['name']} à {tournament['place']}")
        choice = int(input("Choisissez le numéro du tournoi à reprendre : "))
        chosen_tournament = unfinished_tournaments[choice - 1]
        print(f"Vous avez choisi de reprendre le tournoi {chosen_tournament['name']} à {chosen_tournament['place']}")
        return chosen_tournament

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
        # Obtenir les noms des tournois
        tournament_names = self.get_tournaments_by_alphabetical_order()
        for name in tournament_names:
            print(name)
        print("*" * 100)
        # Demander à l'utilisateur de choisir un tournoi
        user_tournament_choice = input(
            "Indiquez le nom du tournoi dont vous souhaitez les informations : ").capitalize()

        user_tournament_choice_normalized = unidecode(user_tournament_choice)

        # Obtenir les détails du tournoi choisi
        for tournament_data in self.load_tournaments():
            tournament_name_normalized = unidecode(tournament_data['name'].capitalize())
            if user_tournament_choice_normalized == tournament_name_normalized:
                tournament_details = {
                    "name": tournament_data["name"],
                    "place": tournament_data["place"],
                    "date_start": tournament_data["date_start"],
                    "date_end": tournament_data["date_end"],
                    "director_note": tournament_data["director_note"],
                    "players_score": tournament_data['players_score'],
                    "rounds": tournament_data['rounds']
                }
                current_round = tournament_data['current_round']
                rounds_count = len(tournament_data['rounds'])
                if current_round == rounds_count:
                    tournament_details["tournament_status"] = " Tournoi terminé"
                else:
                    tournament_details["tournament_status"] = f"Round actuel : {current_round} sur {rounds_count}"
                return tournament_details
        return None


if __name__ == "__main__":
    pass