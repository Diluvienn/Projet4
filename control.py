import random
from match import Match


class TournamentController:
    """Contrôleur du tournoi"""

    def __init__(self, tournament):
        self.tournament = tournament

    def create_matches(self):
        # Obtenez la liste des joueurs disponibles pour le tournoi
        players = self.tournament.get_players()

        # Mélangez aléatoirement la liste des joueurs
        random.shuffle(players)

        # Vérifiez que le nombre de joueurs est pair
        if len(players) % 2 != 0:
            raise ValueError("Le nombre de joueurs doit être pair pour former des paires de matchs.")


if __name__ == "__main__":
    pass
