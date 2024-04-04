# Import des classes de repository
from repository.tournament_repository import TournamentRepository
from repository.player_repository import PlayerRepository

# Import des classes de controller
from controller.tournament_controller import TournamentController
from controller.player_controller import PlayerController

# Import des classes de vue
from view.tournament_view import TournamentView
from view.player_view import PlayerView

# Import des modules utilitaires
from utils.formatvalidator import validate_date_format, validate_national_chess_id_format


def main():
    # Initialisation des instances nécessaires
    tournament_repository = TournamentRepository()
    player_repository = PlayerRepository()


    tournament_view = TournamentView()
    player_view = PlayerView()
    tournament_controller = TournamentController(tournament_repository, tournament_view)
    player_controller = PlayerController(player_repository, player_view)

    while True:
        print("\nMenu Principal:")
        print("1. Afficher la liste des tournois")
        print("2. Afficher les détails d'un tournoi")
        print("3. Créer un nouveau tournoi")
        print("4. Reprendre un tournoi non terminé")
        print("5. Quitter")

        choice = input("Entrez le numéro de votre choix: ")

        if choice == "1":
            tournament_controller.show_tournaments()
        elif choice == "2":
            tournament_name = tournament_view.get_tournament_name_from_user()
            tournament_controller.get_tournament_details(tournament_name)
        elif choice == "3":
            tournament_controller.create_new_tournament()
        elif choice == "4":
            tournament_controller.resume_tournament()
        elif choice == "5":
            print("Au revoir!")
            break
        else:
            print("Choix invalide. Veuillez entrer un numéro valide.")


if __name__ == "__main__":
    main()
