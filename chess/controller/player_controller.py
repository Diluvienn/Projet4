from model.player import Player
from repository.player_repository import PlayerRepository
from utils.formatvalidator import validate_date_format, validate_national_chess_id_format


class PlayerController:
    def __init__(self, player_repository, player_view):
        self.player_repository = PlayerRepository()
        self.player_view = player_view

    def show_players(self):
        """Affiche la liste des joueurs."""
        sorted_players = self.player_repository.get_player_by_alphabetical_order()
        if not sorted_players:
            print("Aucun joueur enregistré pour le moment.")
        else:
            print("Liste des joueurs :\n")
            for index, player_info in enumerate(sorted_players, start=1):
                print(f"{index}. {player_info['lastname']} {player_info['firstname']}")

            while True:
                choice = input("\nSouhaitez-vous les détails d'un joueur ? (y/n): ").lower()
                if choice == "n":
                    break
                elif choice == "y":
                    player_index = input("Veuillez indiquer l'index du joueur : ")
                    try:
                        player_index = int(player_index)
                        if 1 <= player_index <= len(sorted_players):
                            player_info = sorted_players[player_index - 1]
                            print("\nDétails du joueur :\n")
                            print(f"Nom: {player_info['lastname']} {player_info['firstname']}")
                            print(f"Date de naissance: {player_info['birth']}")
                            print(f"Identifiant national d'échecs: {player_info['national chess ID']}")
                        else:
                            print("Index invalide.")
                    except ValueError:
                        print("Veuillez entrer un index valide.")
                else:
                    print("Choix invalide. Veuillez entrer 'y' pour oui ou 'n' pour non.")

    def add_player(self):
        """Ajoute un nouveau joueur à la liste des joueurs."""
        player_info = self.player_view.get_player_info_from_user()
        if player_info is not None:
            new_player = Player(*player_info)
            self.player_repository.add_player(new_player)

    def create_new_player(self):
        new_player = self.get_player_info_from_user()
        self.player_repository.add_player(new_player)

    def get_player_info_from_user(self):
        """Obtient les informations d'un nouveau joueur depuis l'entrée utilisateur."""
        while True:
            firstname = input("\nEntrez le prénom du joueur: ")
            if firstname.replace(' ', '').isalpha():
                break
            else:
                print("Le prénom ne peut contenir que des lettres et des espaces. Veuillez réessayer.")

        while True:
            lastname = input("Entrez le nom de famille du joueur: ")
            if lastname.replace(' ', '').isalpha():
                break
            else:
                print("Le nom de famille ne peut contenir que des lettres et des espaces. Veuillez réessayer.")

        while True:
            birth = input("Entrez la date de naissance du joueur (format: dd-mm-yyyy): ")
            if validate_date_format(birth):
                break
            else:
                print("Format de date invalide. Veuillez utiliser le format 'dd-mm-yyyy'. Veuillez réessayer.")

        while True:
            national_chess_id = input("Entrez l'identifiant national du joueur (format: AB12345): ")
            if validate_national_chess_id_format(national_chess_id):
                break
            else:
                print(
                    "Format d'identifiant national invalide. Veuillez utiliser le format 'AB12345'.")

        new_player = Player(firstname, lastname, birth, national_chess_id)
        print(f"La joueuse ou le joueur {new_player.firstname} {new_player.lastname} a bien été ajouté.e à la liste.")
        return new_player
