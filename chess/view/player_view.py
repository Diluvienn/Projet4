class PlayerView:
    def __init__(self, player_repository):
        self.player_repository = player_repository

    def show_players(self):
        self.player_repository.load_players()
        self.player_repository.display_players_by_index()
