from model.tournament import Tournament, TournamentRepository
# from view.view import add_player_from_cli
from model.player import Player

repository = TournamentRepository


def register_new_tournament(name: str, place: str, date_start: str, date_end: str, rounds: int = 4, current_round: int =1):
    tournament = Tournament(name, place, date_start, date_end, rounds, current_round)
    repository.add_tournament(tournament)

# # def add_players_to_tournament(tournament):
# #         player = add_player_from_cli()
# #         tournament.add_player(player)
#
# def add_players_to_tournament(tournament: Tournament):
#     while True:
#         player = Player.from_cli()  # Utiliser une méthode de classe pour créer un joueur depuis l'interface CLI
#         tournament.add_player(player)  # Ajouter le joueur au tournoi
#
#         # Demander à l'utilisateur s'il souhaite ajouter un autre joueur
#         choice = input("Voulez-vous ajouter un autre joueur ? (oui/non) : ")
#         if choice.lower() != "oui":
#             break
