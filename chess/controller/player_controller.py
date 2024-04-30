from model.player import Player
from view.player_view import get_player_info_from_user


class PlayerController:
    def __init__(self, player_repository, player_view):
        self.player_repository = player_repository
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

    def create_new_player(self):
        """Obtient les informations du joueur et crée un objet Player."""
        firstname, lastname, birth, national_chess_id = get_player_info_from_user()
        new_player = Player(firstname, lastname, birth, national_chess_id)
        print(f"La joueuse ou le joueur {new_player.firstname} {new_player.lastname} a bien été ajouté.e à la liste.")
        self.player_repository.add_player(new_player)
        return new_player

    def add_player(self):
        """Ajoute un nouveau joueur à la liste des joueurs."""
        player_info = self.player_view.create_player()
        if player_info is not None:
            new_player = Player(*player_info)
            self.player_repository.add_player(new_player)
