from model.tournament import Tournament, calculate_leaderboard
from model.round import Round
from datetime import datetime
from repository.tournament_repository import TournamentRepository


class TournamentController:
    def __init__(self, tournament_repository, tournament_view, player_repository, player_controller):
        self.tournament_repository = tournament_repository
        self.tournament_view = tournament_view
        self.player_repository = player_repository
        self.player_controller = player_controller
        self.num_players = 0

    def show_tournaments(self):
        tournaments = self.tournament_repository.get_tournaments_by_alphabetical_order()
        total_tournaments = len(tournaments)
        print(f" total tournaments dans show tournaments : {total_tournaments}")
        self.tournament_view.display_tournament_list(tournaments, total_tournaments)
        return tournaments

    def get_tournament_name_by_index(self, tournaments, tournament_index):
        """Get the name of the tournament corresponding to the given index."""
        if 1 <= tournament_index <= len(tournaments):
            return tournaments[tournament_index - 1].name
        else:
            return None

    def get_tournament_details(self, tournament_name):
        tournament_details = self.tournament_repository.get_tournament_details(tournament_name)
        if tournament_details:
            # Afficher les détails du tournoi
            self.tournament_view.display_tournament_details(tournament_details)
        else:
            print("Le tournoi spécifié n'existe pas ou n'a pas été trouvé.")

    def create_new_tournament(self, name, place, date_start, date_end, director_note, rounds):
        """Crée un nouveau tournoi."""
        new_tournament = Tournament(name=name, place=place, date_start=date_start, date_end=date_end,
                                    director_note=director_note)
        for round_details in rounds:
            round_name = round_details["name"]
            start_time = round_details["start_time"]
            end_time = round_details["end_time"]
            matches = round_details.get("matches", [])
            new_round = Round(round_name, matches, start_time, end_time)
            new_tournament.add_round(new_round)
        self.tournament_repository.add_tournament(new_tournament)
        return new_tournament

    def add_director_notes_to_tournament(self):
        notes = input("Ajouter des notes du directeur (y/n) ? : ")
        if notes.lower() == "y":
            notes_text = input("Entrez les notes du directeur : ")
            return notes_text
        elif notes.lower() == "n":
            return ""
        else:
            print("Choix invalide.")
            return self.add_director_notes_to_tournament()

    def add_players_to_tournament(self, tournament):
        """Add players to the tournament."""
        selected_players_index = []
        selected_players = []
        sorted_players_list = self.player_repository.display_players_by_index()
        while True:
            self.tournament_view.display_add_player_menu(self.num_players)
            user_choice = self.tournament_view.get_user_choice()
            if user_choice == "1":
                selected_player, index = self.player_repository.get_selected_player(sorted_players_list)
                # Vérifier si le joueur est déjà dans le tournoi
                if index in selected_players_index:
                    print(selected_players_index)
                    print("Ce joueur est déjà ajouté au tournoi.")
                    continue
                # Ajouter le joueur au tournoi
                selected_players_index.append(index)
                selected_players.append(selected_player)
                self.num_players += 1
                print(f"Ajout du joueur {selected_player.firstname} {selected_player.lastname}")
                print("Joueurs inscrits dans le tournoi:")
                for player in selected_players:
                    print(f"- {player.firstname} {player.lastname}")

            elif user_choice == "2":
                # Ajouter un nouveau joueur
                new_player = self.player_controller.get_player_info_from_user()

                # Ajouter le joueur au tournoi
                selected_players.append(new_player)
                self.num_players += 1
                print(f"Ajout du joueur {new_player.firstname} {new_player.lastname}")
                print("Joueurs inscrits dans le tournoi:")
                for player in selected_players:
                    print(f"- {player.firstname} {player.lastname}")

                # Enregistrer le nouveau joueur dans le repository
                self.player_repository.add_player(new_player)

            elif user_choice == "3":
                # Vérifier si le nombre de joueurs est pair et au moins 6
                if len(selected_players) >= 6 and len(selected_players) % 2 == 0:
                    for player in selected_players:
                        tournament.players_list.append(player)
                    self.tournament_repository.add_tournament(tournament)
                    print("Les joueurs ont bien été ajoutés.")
                    break  # Retourner au code appelant après avoir quitté la boucle
                else:
                    print("Le nombre d'inscrits doit être pair et au moins égal à 6.")
            else:
                print("Veuillez indiquer un choix valide.")

    def select_existing_player_for_tournament(self, players):
        """Allow user to select an existing player."""
        for i, player in enumerate(players):
            print(f"{i + 1}. {player.firstname} {player.lastname}")

        while True:
            try:
                selection = int(input("Sélectionnez un joueur en entrant son numéro : "))
                selected_player = players[selection - 1]
                return selected_player
            except (ValueError, IndexError):
                print("Veuillez entrer un numéro valide.")

    def resume_tournament(self):
        """Reprend un tournoi non terminé."""
        chosen_tournament = self.tournament_repository.resume_tournament()
        print(f"chosen_tournament dans le control : {chosen_tournament}")
        if chosen_tournament:
            tournament = Tournament.from_json(chosen_tournament)
            print("Détails du tournoi dans le contrôleur de reprise :")
            print(f"Nom du tournoi : {tournament.name}")
            print(f"Lieu : {tournament.place}")
            print(f"Date de début : {tournament.date_start}")
            print(f"Date de fin : {tournament.date_end}")
            print(f"Note du directeur : {tournament.director_note}")
            print("Détails des rounds :")
            for round_num, round_data in enumerate(tournament.rounds, 1):
                print(f"Round {round_num}:")
                print(f"  Nom du round : {round_data.name}")
                print(f"  Heure de début : {round_data.start_time}")
                print(f"  Heure de fin : {round_data.end_time}")
            tournament.current_round += 1
            self.play_tournament(tournament)

    def resume_unstarted_tournament(self):
        chosen_tournament = self.tournament_repository.resume_unstarted_tournament()
        if chosen_tournament:
            tournament = Tournament.from_json(chosen_tournament)
            self.add_players_to_tournament(tournament)

    def play_tournament(self, tournament):
        while tournament.current_round <= len(tournament.rounds):
            current_round = tournament.rounds[tournament.current_round]

            print(f"\nRound {tournament.current_round + 1} :")

            # Définir l'heure de début du round s'il n'est pas déjà défini
            if current_round.start_time is None:
                current_round.start_time = datetime.now().strftime("%d-%m-%Y %H:%M")

            # Générer les paires de matchs pour ce round
            tournament.generate_pairs_for_round()

            for match in current_round.matches:
                player1 = list(match.players.keys())[0]
                player2 = list(match.players.keys())[1]
                player1_name = f"{player1.firstname} {player1.lastname}"
                player2_name = f"{player2.firstname} {player2.lastname}"
                score1 = match.players[player1]
                score2 = match.players[player2]
                print(f"Match: {player1_name} vs {player2_name}, Scores: {score1}-{score2}")
                # print(f"Start Time: {current_round.start_time}, End Time: {current_round.end_time}")

            # Récupérer les scores précédents à partir des données du tournoi
            previous_scores = self.players_score if hasattr(self, 'players_score') else {}

            # Calculer et afficher le classement provisoire
            calculate_leaderboard(tournament, previous_scores)

            if current_round.end_time is None:
                current_round.end_time = datetime.now().strftime("%d-%m-%Y %H:%M")

            # Demander si vous voulez jouer le prochain round

            if tournament.current_round == (len(tournament.rounds) - 1):
                tournament_repository = TournamentRepository()
                tournament_repository.add_tournament(tournament)
                break

            if not self.ask_to_play_next_round():
                tournament_repository = TournamentRepository()
                tournament_repository.add_tournament(tournament)
                break

            tournament.current_round += 1

            # Enregistrer le tournoi une fois terminé
            tournament_repository = TournamentRepository()
            tournament_repository.add_tournament(tournament)

    def ask_to_play_next_round(self):
        play_next_round = input("Voulez-vous jouer le round suivant ? (y/n): ")
        while play_next_round not in ["y", "n"]:
            print("Veuillez effectuer un choix valide.")
            play_next_round = input("Voulez-vous jouer le round suivant ? (y/n): ")
        return play_next_round == "y"
