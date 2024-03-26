from datetime import datetime

from view.viewmain import main_user_choice
from view.viewnewtournament import create_tournament_from_cli, add_player_to_tournament_from_cli, add_player_from_cli
from model.tournament import TournamentRepository, Tournament, calculate_leaderboard

from model.player import PlayerRepository


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
                    break
                elif play_first_round != "y" and play_first_round != "n":
                    print("veuillez effectuer un choix valide")
                else:
                    while tournament.current_round < len(tournament.rounds):
                        current_round = tournament.rounds[tournament.current_round]
                        print("*" * 100)
                        print(f"Round {tournament.current_round + 1} :")
                        # Définir l'heure de début du round
                        tournament.rounds[tournament.current_round].start_time = datetime.now()

                        # Générer les paires de matchs pour ce round
                        tournament.generate_pairs_for_round()

                        # Mettre à jour les paires déjà jouées
                        tournament.update_played_pairs()

                        # Définir l'heure de début du round
                        tournament.rounds[tournament.current_round].start_time = datetime.now()

                        for match in current_round.matches:
                            player1 = list(match.players.keys())[0]
                            player2 = list(match.players.keys())[1]
                            player1_name = f"{player1.firstname} {player1.lastname}"
                            player2_name = f"{player2.firstname} {player2.lastname}"
                            score1 = match.players[player1]
                            score2 = match.players[player2]
                            print(f"Match: {player1_name} vs {player2_name}, Scores: {score1}-{score2}")
                            print(f"Start Time: {current_round.start_time}, End Time: {current_round.end_time}")

                        # Calculer et afficher le classement provisoire
                        calculate_leaderboard(tournament)

                        tournament.current_round += 1
                        # Demander si vous voulez jouer le prochain round

                        if tournament.current_round == len(tournament.rounds) - 1:
                            break

                        play_next_round = input("Voulez-vous jouer le round suivant ? (y/n): ")
                        if play_next_round == "n":
                            tournament_repository = TournamentRepository()
                            tournament_repository.add_tournament(tournament)
                            break
                        elif play_next_round != "y":
                            print("Veuillez effectuer un choix valide.")
                            continue


        elif choice == "6":
            tournament_repository = TournamentRepository()
            chosen_tournament = tournament_repository.resume_tournament()
            tournament = Tournament.from_json(chosen_tournament)
            tournament.play_tournament(tournament)

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
