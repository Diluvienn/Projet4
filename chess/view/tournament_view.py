from utils.formatvalidator import validate_date_format


class TournamentView:
    def __init__(self, tournament_controller):
        self.tournament_controller = tournament_controller

    # @staticmethod
    # def display_menu():
    #     """Affiche le menu principal de gestion des tournois."""
    #     print("\nMenu Principal:")
    #     print("1. Afficher la liste des tournois")
    #     print("2. Afficher les détails d'un tournoi")
    #     print("3. Créer un nouveau tournoi")
    #     print("4. Reprendre un tournoi non terminé")
    #     print("5. Quitter")


    # def display_tournament_list(self, tournaments):
    #     """Affiche la liste des tournois."""
    #     print("\nListe des tournois:")
    #     for index, tournament in enumerate(tournaments, 1):
    #         print(f"{index}. {tournament.name} à {tournament.place}")
    def display_tournament_list(self, tournaments,total_tournaments):
        """Affiche la liste des tournois."""
        formatted_output = tournaments

        print("\nListe des tournois:")
        for index, tournament in enumerate(formatted_output, 1):
            print(f"{index}. {tournament.name} à {tournament.place}")

    @staticmethod
    def display_tournament_details(tournament_details):
        if tournament_details:
            print("Détails du tournoi:")
            print(f"Nom: {tournament_details['name']}")
            print(f"Lieu: {tournament_details['place']}")
            print(f"Date de début: {tournament_details['date_start']}")
            print(f"Date de fin: {tournament_details['date_end']}")
            print(f"Notes du directeur: {tournament_details['director_note']}")
            if not tournament_details['players_list']:
                print("Aucun joueur n'a encore été ajouté au tournoi.")
            if tournament_details['rounds'][0]['matches']:
                print(tournament_details['tournament_status'])
            for round_data in tournament_details['rounds']:
                matches = round_data['matches']
                if matches:
                    print(f"{round_data['name']}:")
                    print(f"  Début: {round_data['start_time']}")
                    print(f"  Fin: {round_data['end_time']}")
                    print("  Matches:")
                    for match in round_data['matches']:
                        player1, score1 = list(match['players'].items())[0]
                        player2, score2 = list(match['players'].items())[1]
                        print(f"    '{player1}' vs '{player2}': {score1}-{score2}")
                elif round_data == tournament_details['rounds'][0]:
                    print("Le tournoi n'a pas encore débuté.")
                    break
        else:
            print("Le tournoi spécifié n'existe pas ou n'a pas été trouvé.")

    @staticmethod
    def display_message(message):
        """Affiche un message spécifique."""
        print(message)

    def get_new_tournament_details(self):
        """Demande à l'utilisateur de saisir les détails pour créer un nouveau tournoi."""
        print("\nCréation d'un nouveau tournoi:")
        name = input("Nom du tournoi : ").title()
        place = input("Lieu du tournoi : ").title()
        # Demander au contrôleur d'ajouter des notes du directeur
        director_note = self.tournament_controller.add_director_notes_to_tournament()
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
        rounds_count = input("Nombre de rounds (facultatif, par défaut 4) : ")
        rounds_count = int(rounds_count) if rounds_count else 4
        print(f" rounds_count : {rounds_count}")

        rounds = []
        for i in range(rounds_count):
            print(f" i : {i}")
            round_name = f"Round {i + 1}"
            print(f"round_name : {round_name}")
            round_details = {
                "name": round_name,
                "matches": [],
                "start_time": None,
                "end_time": None
            }
            rounds.append(round_details)

        return name, place, date_start, date_end, director_note, rounds

    def display_add_player_menu(self, num_players):
        if num_players >= 6 and num_players % 2 == 0:
            print("\nSouhaitez-vous ajouter un joueur existant (1), créer un nouveau joueur (2) "
                  "ou arrêter l'ajout de joueur (3) ?: ")
        else:
            print("\nSouhaitez-vous ajouter un joueur existant (1) ou créer un nouveau joueur (2) ?: ")

    def get_user_choice(self):
        return input("Votre choix : ")

    def get_tournament_index_from_user(self, total_tournaments):
        """Ask the user to enter the index of the tournament."""
        while True:
            index_input = input("\nEntrez l'index du tournoi dont vous souhaitez voir les détails : ")
            if index_input.isdigit():
                index = int(index_input)
                if 1 <= index <= total_tournaments:
                    return index
                else:
                    print(f"L'index doit être compris entre 1 et {total_tournaments}.")
            else:
                print("L'index doit être un nombre entier.")

    def prompt_add_players(self):
        """Demande à l'utilisateur s'il souhaite ajouter des joueurs au tournoi."""
        while True:
            add_players_choice = input("Souhaitez-vous ajouter des joueurs au tournoi ? (y/n) : ")
            if add_players_choice.lower() == "y":
                return True
            elif add_players_choice.lower() == "n":
                return False
            else:
                print("Veuillez effectuer un choix valide")

    def prompt_play_tournament(self):
        """Demande à l'utilisateur s'il souhaite lancer le tournoi."""
        while True:
            play_tournament_choice = input("Souhaitez-vous lancer le tournoi ? (y/n) : ")
            if play_tournament_choice.lower() == "y":
                return True
            elif play_tournament_choice.lower() == "n":
                return False
            else:
                print("Veuillez effectuer un choix valide")
