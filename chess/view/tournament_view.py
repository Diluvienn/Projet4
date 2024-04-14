from utils.formatvalidator import validate_date_format
from controller.tournament_controller import TournamentController

class TournamentView:
    def __init__(self, tournament_controller):
        self.tournament_controller = tournament_controller

    @staticmethod
    def display_menu():
        """Affiche le menu principal de gestion des tournois."""
        print("\nMenu Principal:")
        print("1. Afficher la liste des tournois")
        print("2. Afficher les détails d'un tournoi")
        print("3. Créer un nouveau tournoi")
        print("4. Reprendre un tournoi non terminé")
        print("5. Quitter")

    @staticmethod
    def display_tournament_list(tournaments):
        """Affiche la liste des tournois."""
        print("\nListe des tournois:")
        for tournament in tournaments:
            print(f"- {tournament.name}")

    @staticmethod
    def display_tournament_details(tournament_details):
        if tournament_details:
            print("Détails du tournoi:")
            print(f"Nom: {tournament_details['name']}")
            print(f"Lieu: {tournament_details['place']}")
            print(f"Date de début: {tournament_details['date_start']}")
            print(f"Date de fin: {tournament_details['date_end']}")
            print(f"Notes du directeur: {tournament_details['director_note']}")
            print(f"Statut du tournoi: {tournament_details['tournament_status']}")
            # Afficher les autres détails du tournoi
        else:
            print("Le tournoi spécifié n'existe pas ou n'a pas été trouvé.")

    @staticmethod
    def display_message(message):
        """Affiche un message spécifique."""
        print(message)


    def get_new_tournament_details(self):
        """Demande à l'utilisateur de saisir les détails pour créer un nouveau tournoi."""
        print("*" * 100)
        print("Création d'un nouveau tournoi:")
        name = input("Nom du tournoi : ").capitalize()
        place = input("Lieu du tournoi : ").capitalize()
        # Demander au contrôleur d'ajouter des notes du directeur
        director_notes = self.tournament_controller.add_director_notes_to_tournament()
        while True:
            date_start = input("Date de début (format DD-MM-YYYY) : ")
            if validate_date_format(date_start):
                break
            else:
                print("Format de date incorrect. Veuillez saisir une date au format DD-MM-YYYY.")
        while True:
            date_end = input("Date de fin (format DD-MM-YYYY) : ")
            if validate_date_format(date_end):
                break
            else:
                print("Format de date incorrect. Veuillez saisir une date au format DD-MM-YYYY.")
        rounds = input("Nombre de rounds (facultatif, par défaut 4) : ")

        return name, place, date_start, date_end, rounds, director_notes

    def display_add_player_menu(self, num_players):
        if num_players >= 6 and num_players % 2 == 0:
            print("\nSouhaitez-vous ajouter un joueur existant (1), créer un nouveau joueur (2) "
                  "ou arrêter l'ajout de joueur (3) ?: ")
        else:
            print("\nSouhaitez-vous ajouter un joueur existant (1) ou créer un nouveau joueur (2) ?: ")

    def get_user_choice(self):
        return input("Votre choix : ")

    def get_tournament_name_from_user(self):
        """Ask the user to enter the name of the tournament."""
        return input("Entrez le nom du tournoi dont vous souhaitez voir les détails : ").capitalize()
