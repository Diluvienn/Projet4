from model.tournament import Tournament
from repository.tournament_repository import TournamentRepository



class TournamentController:
    def __init__(self, tournament_repository, tournament_view):
        self.tournament_repository = tournament_repository
        self.tournament_view = tournament_view

    def show_tournaments(self, tournaments):
        self.tournament_view.display_tournaments(tournaments)

    def get_tournament_details(self, tournament):
        self.tournament_view.display_tournament_details(tournament)

    def create_new_tournament(self):
        """Crée un nouveau tournoi."""
        name = self.tournament_view.get_tournament_name()
        place = self.tournament_view.get_tournament_place()
        date_start = self.tournament_view.get_tournament_start_date()
        date_end = self.tournament_view.get_tournament_end_date()
        director_notes = self.tournament_view.get_director_notes()
        rounds = self.tournament_view.get_number_of_rounds()

        new_tournament = Tournament(name, place, date_start, date_end, director_notes, rounds)
        self.tournament_repository.add_tournament(new_tournament)

    def resume_tournament(self):
        """Reprend un tournoi non terminé."""
        chosen_tournament = self.tournament_repository.resume_tournament()
        if chosen_tournament:
            tournament = Tournament.from_json(chosen_tournament)
            tournament.play_tournament()
