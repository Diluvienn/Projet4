from model.tournament import Tournament
from repository.tournament_repository import TournamentRepository



class TournamentController:
    def __init__(self, tournament_repository, tournament_view):
        self.tournament_repository = tournament_repository
        self.tournament_view = tournament_view

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

    def create_new_tournament(self):
        """Crée un nouveau tournoi."""
        name, place, date_start, date_end, rounds = self.tournament_view.get_new_tournament_details()
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

    def resume_tournament(self):
        """Reprend un tournoi non terminé."""
        chosen_tournament = self.tournament_repository.resume_tournament()
        if chosen_tournament:
            tournament = Tournament.from_json(chosen_tournament)
            tournament.play_tournament()
