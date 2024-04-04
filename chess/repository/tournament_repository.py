import os
import json

from typing import List
from unidecode import unidecode


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
