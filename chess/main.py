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
        print("3. Afficher la liste des joueurs")
        print("4. Créer un nouveau joueur")
        print("5. Créer un nouveau tournoi")
        print("6. Ajouter des joueurs à un tournoi non commencé")
        print("7. Reprendre un tournoi non terminé")
        print("8. Quitter")

        choice = input("Entrez le numéro de votre choix: ")

        if choice == "1":
            tournament_controller.show_tournaments()
        elif choice == "2":
            tournaments = tournament_controller.show_tournaments()
            total_tournaments = len(tournaments)
            tournament_index = tournament_view.get_tournament_index_from_user(total_tournaments)
            tournament_name = tournament_controller.get_tournament_name_by_index(tournaments, tournament_index)
            tournament_controller.get_tournament_details(tournament_name)
        elif choice == "3":
            player_repository.load_players()
            player_repository.display_players_by_index()
        elif choice == "4":
            new_player = player_controller.get_player_info_from_user()
            player_repository.add_player(new_player)
        elif choice == "5":
            name, place, date_start, date_end, rounds, director_notes = tournament_view.get_new_tournament_details()
            tournament = tournament_controller.create_new_tournament(name, place, date_start, date_end, rounds,
                                                                     director_notes)

            # Initialiser la liste des joueurs du tournoi
            if tournament_view.prompt_add_players():
                tournament_controller.add_players_to_tournament(tournament)
                if tournament_view.prompt_play_tournament():
                    tournament_controller.play_tournament(tournament)

        elif choice == "6":
            tournament_controller.resume_unstarted_tournament()
        elif choice == "7":
            tournament_controller.resume_tournament()
        elif choice == "8":
            print("Au revoir!")
            break
        else:
            print("Choix invalide. Veuillez entrer un numéro valide.")


if __name__ == "__main__":
    main()
