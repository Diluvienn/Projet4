from model.player import Player
from repository.player_repository import PlayerRepository
from view.player_view import PlayerView

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
            for player_info in sorted_players:
                print(player_info)

    def add_player(self):
        """Ajoute un nouveau joueur à la liste des joueurs."""
        player_info = self.player_view.get_player_info_from_user()
        if player_info is not None:
            new_player = Player(*player_info)
            self.player_repository.add_player(new_player)

    def get_player_info_from_user(self):
        """Obtient les informations d'un nouveau joueur depuis l'entrée utilisateur."""
        try:
            firstname = input("Entrez le prénom du joueur: ")
            lastname = input("Entrez le nom de famille du joueur: ")
            birth = input("Entrez la date de naissance du joueur (format: dd-mm-yyyy): ")
            national_chess_id = input("Entrez l'identifiant national du joueur (format: AB12345): ")

            new_player = Player(firstname, lastname, birth, national_chess_id)
            return new_player
        except ValueError as e:
            print(f"Erreur lors de la création du joueur: {e}")
            return None

