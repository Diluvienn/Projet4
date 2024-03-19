from view.viewmain import main_user_choice
from view.viewnewtournament import create_tournament_from_cli, add_player_to_tournament_from_cli, add_player_from_cli
from model.tournament import TournamentRepository
from control.roundcontroller import RoundController
from model.player import PlayerRepository


def main():
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

        # choix 3 : Voir toutes les informations d'un tournoi donné
        elif choice == "3":
            tournament_repository = TournamentRepository()
            tournaments = tournament_repository.get_tournament_details()
            user_tournament_choice = (input("Indiquez le nom du tournoi dont vous souhaitez les informations : ")
                                      .capitalize())
            for tournament_info in tournaments:
                if user_tournament_choice in tournament_info:
                    print("*" * 100)
                    print(tournament_info)
                    print("*" * 100)
                    break
            else:
                print("*" * 100)
                print("Le tournoi spécifié n'existe pas.")
                print("*" * 100)

        # choix 4 : Ajouter un nouveau joueur à la liste déjà existante
        elif choice == "4":
            player_repository = PlayerRepository()
            new_player = add_player_from_cli()
            print(f"new_player {new_player}")
            player_repository.add_player(new_player)

        # choix 5 Créer et jouer un nouveau tournoi
        elif choice == "5":
            players_list_objects, players_list_names = add_player_to_tournament_from_cli()
            new_tournament = create_tournament_from_cli()

            for player_name in players_list_names:
                new_tournament.players_list.append(player_name)
            print(f"Players_list {new_tournament.players_list}")
            for player_name in new_tournament.players_list:
                new_tournament.players_score[player_name] = 0
            print(f"Players_score {new_tournament.players_score}")

            tournament_repository = TournamentRepository()
            tournament_repository.add_tournament(new_tournament)


            # Affichage de tous les attributs du tournoi
            print("Attributs du tournoi :")
            for attribute, value in vars(new_tournament).items():
                if attribute == 'players_list':
                    players_names = ", ".join(new_tournament.players_list)
                    print(f"{attribute}: {players_names}")
                elif attribute == 'players_score':
                    player_score_str = ', '.join([f"{name}: {score}" for name, score in value.items()])
                    print(f"{attribute}: {player_score_str}")
                else:
                    print(f"{attribute}: {value}")

            # Loop until the tournament reaches round 5.
            while new_tournament.current_round < 5:
                # Ask the user if they want to start the current round.
                new_round_choice = input(f"Voulez-vous faire le {new_tournament.current_round} round ? (y/n) : ")

                # If the user chooses to start the round, proceed.
                if new_round_choice == "y":
                    # Create a new round and generate matches.
                    round_controller = RoundController(new_tournament)
                    round_controller.generate_matches()
                    round_controller.play_round()

                    # Update scores for each match in the round.

                    for match in round_controller.matches:
                        new_tournament.update_scores(match)

                    # Print the scores of all players.
                    print(new_tournament.get_all_scores())
                    print("*" * 100)
                else:
                    break

            # Triez le dictionnaire player_score par valeur (score) en ordre décroissant
            sorted_scores = sorted(new_tournament.players_score.items(), key=lambda x: x[1], reverse=True)

            # Sélectionnez les trois premiers éléments (joueurs avec les scores les plus élevés)
            top_three_players = sorted_scores[:3]

            # Affichez les trois meilleurs joueurs et leurs scores
            print("Les 3 meilleurs joueurs du tournoi :")
            for player, score in top_three_players:
                print(f"Joueur : {player}, Score : {score}")
            print("*" * 100)


        # choix 6 : quitter le logiciel
        elif choice == "6":
            break

        else:
            print("-" * 50)
            print("Veuillez indiquer un choix valide")
            print("-" * 50)


if __name__ == "__main__":
    main()


