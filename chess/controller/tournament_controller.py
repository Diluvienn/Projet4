from model.tournament import Tournament
from model.player import Player



class TournamentController:
    def __init__(self, tournament_repository, tournament_view,  player_repository, player_controller):
        self.tournament_repository = tournament_repository
        self.tournament_view = tournament_view
        self.player_repository = player_repository
        self.player_controller = player_controller
        self.num_players = 0

    def show_tournaments(self):
        tournaments = self.tournament_repository.get_tournaments_by_alphabetical_order()
        self.tournament_view.display_tournament_list(tournaments)

    def get_tournament_details(self, tournament_name):
        tournament_details = self.tournament_repository.get_tournament_details(tournament_name)
        if tournament_details:
            # Afficher les détails du tournoi
            self.tournament_view.display_tournament_details(tournament_details)
        else:
            print("Le tournoi spécifié n'existe pas ou n'a pas été trouvé.")

    def create_new_tournament(self, name, place, date_start, date_end, rounds, director_note):
        """Crée un nouveau tournoi."""
        # Créez un nouvel objet Tournament avec les détails obtenus
        new_tournament = Tournament(name, place, date_start, date_end, rounds)
        # Ajoutez le tournoi à votre repository
        self.tournament_repository.add_tournament(new_tournament)

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

    def add_players_to_tournament(self):
        """Add players to the tournament."""
        selected_players = []
        while True:
            self.tournament_view.display_add_player_menu(self.num_players)
            user_choice = self.tournament_view.get_user_choice()
            if user_choice == "1":
                selected_player = self.player_repository.get_player_by_index()
                # Obtenir le joueur à partir de l'index
                if selected_player:
                    # Vérifier si le joueur est déjà ajouté au tournoi
                    if selected_player in selected_players:
                        print("Ce joueur est déjà ajouté au tournoi.")
                        continue

                    # Ajouter le joueur au tournoi
                    selected_players.append(selected_player)
                    self.num_players += 1
                    print(f"Ajout du joueur {selected_player.firstname} {selected_player.lastname}")
                    print("Joueurs inscrits dans le tournoi:")
                    for player in selected_players:
                        print(f"- {player.firstname} {player.lastname}")

                elif user_choice == "2":
                    # Ajouter un nouveau joueur
                    new_player = self.player_controller.get_player_info_from_user()
                    if new_player:
                        # Vérifier si le joueur est déjà ajouté au tournoi
                        if new_player in selected_players:
                            print("Ce joueur est déjà ajouté au tournoi.")
                            continue

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
                        break
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
        if chosen_tournament:
            tournament = Tournament.from_json(chosen_tournament)
            tournament.play_tournament()
