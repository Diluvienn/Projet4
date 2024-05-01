# Import des classes de repository
from repository.tournament_repository import TournamentRepository
from repository.player_repository import PlayerRepository

# Import des classes de controller
from controller.tournament_controller import TournamentController
from controller.player_controller import PlayerController

# Import des classes de vue
from view.tournament_view import TournamentView
from view.player_view import PlayerView
from view.main_view import MainView


class MainController:
    def __init__(self):

        # Initialisation des instances nécessaires
        _tournament_repository = TournamentRepository()
        _player_repository = PlayerRepository()

        # Création de TournamentController
        self._tournament_controller = TournamentController(_tournament_repository, None,
                                                           _player_repository, None)

        # Création de TournamentView avec le contrôleur correspondant
        _tournament_view = TournamentView(self._tournament_controller)

        # Création de PlayerView
        _player_view = PlayerView(_player_repository)

        self._main_view = MainView()

        # Création de PlayerController avec le view correspondant
        self._player_controller = PlayerController(_player_repository, _player_view)
        self._tournament_controller = TournamentController(_tournament_repository, _tournament_view,
                                                           _player_repository, self._player_controller)

    def run(self):

        while True:
            self._main_view.display_main_menu()

            choice = input("Entrez le numéro de votre choix: ")

            if choice == "1":
                self._tournament_controller.show_tournaments()
            elif choice == "2":
                self._tournament_controller.show_tournament_details()
            elif choice == "3":
                self._player_controller.show_players()
            elif choice == "4":
                self._player_controller.create_new_player()
            elif choice == "5":
                self._tournament_controller.create_new_tournament()
            elif choice == "6":
                self._tournament_controller.resume_unstarted_tournament()
            elif choice == "7":
                self._tournament_controller.resume_tournament()
            elif choice == "8":
                print("\nA bientôt !")
                break
            else:
                print("Choix invalide. Veuillez entrer un numéro valide.")


if __name__ == "__main__":
    pass
