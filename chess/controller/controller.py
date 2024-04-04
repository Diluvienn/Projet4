from view.viewmain import main_user_choice
from view.viewnewtournament import create_tournament_from_cli, add_player_to_tournament_from_cli, add_player_from_cli
from model.tournament import TournamentRepository
from model.player import PlayerRepository
from controller.player_controller import PlayerController
from controller.tournament_controller import TournamentController


class Controller:
    def __init__(self):
        self.player_controller = PlayerController()
        self.tournament_controller = TournamentController()

    def run(self):
        while True:
            choice = main_user_choice()

            if choice == "1":
                self.player_controller.show_players()

            elif choice == "2":
                self.tournament_controller.show_tournaments()

            elif choice == "3":
                self.tournament_controller.show_tournament_details()

            elif choice == "4":
                self.player_controller.add_player()

            elif choice == "5":
                self.tournament_controller.create_new_tournament()

            elif choice == "6":
                self.tournament_controller.resume_tournament()

            elif choice == "7":
                print("A bientôt !")
                break

            else:
                print("Veuillez indiquer un choix valide")


if __name__ == "__main__":
    controller = Controller()
    controller.run()
