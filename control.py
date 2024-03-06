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

        # Créez des paires de joueurs et des matchs correspondants
        for i in range(0, len(players), 2):
            player1 = players[i]
            player2 = players[i + 1]
            match = Match(player1, player2)
            self.tournament.add_match(match)