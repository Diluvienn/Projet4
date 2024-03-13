from view.view import create_tournament_from_cli
from model.tournament import Tournament, TournamentRepository



def main():
    tournament_data = create_tournament_from_cli()
    tournament = Tournament(**tournament_data)

    tournament_repositiry = TournamentRepository
    tournament_repositiry.add_tournament(tournament)



    # Création d'une instance de Tournoi
    # tournament = Tournament("Chess Tournament", "City", "01-01-2023", "11-02-2023")
    # round_controller = RoundController(tournament)

    # Generate 6 random players and add them to the tournament
    # Then, print the list of tournament players and the scores of all players.


    #     tournament.add_player(random_player_instance)
    # print(f"Tournament players : {tournament.get_players()}")
    # print("-" * 50)
    # print(tournament.get_all_scores())
    #
    # # Loop until the tournament reaches round 5.
    # while tournament.current_round < 5:
    #     # Ask the user if they want to start the current round.
    #     new_round_choice = input(f"Voulez-vous faire le {tournament.current_round} round ? (y/n) : ")
    #
    #     # If the user chooses to start the round, proceed.
    #     if new_round_choice == "y":
    #         # Create a new round and generate matches.
    #         round_controller.generate_matches()
    #         round_controller.play_round()
    #
    #         # Update scores for each match in the round.
    #
    #         for match in round_controller.matches:
    #             tournament.update_scores(match)
    #
    #         # Print the scores of all players.
    #         print(tournament.get_all_scores())
    #         print("-" * 50)
    #     else:
    #         break
    #
    # # Triez le dictionnaire player_score par valeur (score) en ordre décroissant
    # sorted_scores = sorted(tournament.player_score.items(), key=lambda x: x[1], reverse=True)
    #
    # # Sélectionnez les trois premiers éléments (joueurs avec les scores les plus élevés)
    # top_three_players = sorted_scores[:3]
    #
    # # Affichez les trois meilleurs joueurs et leurs scores
    # print("Les 3 meilleurs joueurs du tournoi :")
    # for player, score in top_three_players:
    #     print(f"Joueur : {player}, Score : {score}")
    #

if __name__ == "__main__":
    main()
