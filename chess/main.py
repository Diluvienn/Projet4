from datetime import datetime

from view.viewmain import main_user_choice
from view.viewnewtournament import create_tournament_from_cli, add_player_to_tournament_from_cli, add_player_from_cli
from model.tournament import TournamentRepository, Tournament, calculate_leaderboard

from model.player import PlayerRepository, Player


def main():
    """Main function to run the chess tournament management system."""
    while True:
        choice = main_user_choice()

        # choix 1 : Voir la liste des joueurs enregistrés par ordre alphabétique
        if choice == "1":
            player_repository = PlayerRepository()
            sorted_players = player_repository.get_player_by_alphabetical_order()
            print("*" * 100)
            for player_info in sorted_players:
                print(player_info)
            print("*" * 100)

        # choix 2 : Voir la liste des tournois enregistrés par ordre alphabétique
        elif choice == "2":
            tournament_repository = TournamentRepository()
            tournaments = tournament_repository.get_tournaments_by_alphabetical_order()
            print("*" * 100)
            for tournament in tournaments:
                print(tournament)
            print("*" * 100)

        elif choice == "3":
            tournament_repository = TournamentRepository()
            tournaments = tournament_repository.get_tournament_details()

            user_tournament_choice = input(
                "Indiquez le nom du tournoi dont vous souhaitez les informations : ").capitalize()

            found = False
            for tournament_info in tournaments:
                if user_tournament_choice == tournament_info['name']:
                    print("*" * 100)
                    print("Tournament:", tournament_info['name'])
                    print("Place:", tournament_info['place'])
                    print("Start date:", tournament_info['date_start'])
                    print("End date:", tournament_info['date_end'])
                    print("Director's note:", tournament_info['director_note'])
                    print("Players and Scores:")
                    for player_score in tournament_info['players_scores']:
                        print(f"- {player_score['name']}: {player_score['score']}")
                    print("*" * 100)
                    found = True
                    break

            if not found:
                print("*" * 100)
                print("Le tournoi spécifié n'existe pas.")
                print("*" * 100)

        # choix 4 : Ajouter un nouveau joueur à la liste déjà existante
        elif choice == "4":
            player_repository = PlayerRepository()
            new_player = add_player_from_cli()
            if new_player is not None:
                player_repository.add_player(new_player)

        elif choice == "5":

            # Récupérer les informations du tournoi et les joueurs sélectionnés depuis la fonction
            tournament_info = create_tournament_from_cli()
            selected_players, players_names = add_player_to_tournament_from_cli()

            # Créer le tournoi avec les informations fournies, y compris le nombre de rounds
            tournament = Tournament(tournament_info[0], tournament_info[1], tournament_info[2], tournament_info[3],
                                    tournament_info[4])
            num_rounds = tournament_info[-2]

            tournament.add_round(num_rounds)

            # Ajouter les joueurs sélectionnés au tournoi
            tournament.players_list = selected_players
            tournament.players_score = {f"{player.firstname} {player.lastname}": 0 for player in selected_players}

            while True:
                # Demander si l'utilisateur veut jouer le premier round
                play_first_round = input("Voulez-vous jouer le premier round ? (y/n): ").lower()

                # Si l'utilisateur ne veut pas jouer le premier round, sortir de la boucle principale
                if play_first_round == "n":
                    tournament_repository = TournamentRepository()
                    tournament_repository.add_tournament(tournament)
                    print("Le tournoi est enregistré.")
                    play_main_menu = False
                    break

                elif play_first_round != "y" and play_first_round != "n":
                    print("veuillez effectuer un choix valide")
                else:
                    print(f"current round : {tournament.current_round}")
                    print(f" len de round : {len(tournament.rounds)}")
                    tournament.play_tournament()
                    break

        elif choice == "6":
            tournament_repository = TournamentRepository()
            chosen_tournament_data = tournament_repository.resume_tournament()
            print(f"chosen_tournament {chosen_tournament_data}")

            # Extraire les scores précédemment enregistrés dans le JSON
            previous_scores = chosen_tournament_data.get("players_score", {})
            print(f"previous score à sa rceation dans le main : {previous_scores}")
            tournament = Tournament.from_json(chosen_tournament_data)
            print("attribust de tournament, dans main, après re création de l'objet")
            print(vars(tournament))
            print(f"current round après le +1 dans le main de 6 : {tournament.current_round}")

            tournament.play_tournament()



        # choix 7 : quitter le logiciel
        elif choice == "7":
            print("A bientôt !")
            break

        else:
            print("-" * 50)
            print("Veuillez indiquer un choix valide")
            print("-" * 50)


if __name__ == "__main__":
    main()
