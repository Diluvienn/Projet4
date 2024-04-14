# Import des classes de repository
from repository.tournament_repository import TournamentRepository
from repository.player_repository import PlayerRepository

# Import des classes de controller
from controller.tournament_controller import TournamentController
from controller.player_controller import PlayerController

# Import des classes de vue
from view.tournament_view import TournamentView
from view.player_view import PlayerView


def main():
    # Initialisation des instances nécessaires
    tournament_repository = TournamentRepository()
    player_repository = PlayerRepository()

    # Création de TournamentController
    tournament_controller = TournamentController(tournament_repository, None, player_repository, None)

    # Création de TournamentView avec le contrôleur correspondant
    tournament_view = TournamentView(tournament_controller)

    # Création de PlayerView
    player_view = PlayerView()

    # Création de PlayerController avec le view correspondant
    player_controller = PlayerController(player_repository, player_view)
    tournament_controller = TournamentController(tournament_repository, tournament_view, player_repository,
                                                 player_controller)

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
            name, place, date_start, date_end, rounds, director_notes = tournament_view.get_new_tournament_details()
            tournament_controller.create_new_tournament(name, place, date_start, date_end, rounds, director_notes)
            # Initialiser la liste des joueurs du tournoi
            players = []
            while True:
                add_players_choice = input("Souhaitez-vous ajouter des joueurs au tournoi ? (y/n) : ")
                if add_players_choice.lower() == "y":
                    tournament_controller.add_players_to_tournament()
                    break  # Sortir de la boucle while si les joueurs sont ajoutés
                elif add_players_choice.lower() == "n":
                    break  # Sortir de la boucle while si les joueurs ne sont pas ajoutés
                else:
                    print("Veuillez effectuer un choix valide")
        elif choice == "4":
            tournament_controller.resume_tournament()
        elif choice == "5":
            print("Au revoir!")
            break
        else:
            print("Choix invalide. Veuillez entrer un numéro valide.")


if __name__ == "__main__":
    main()
