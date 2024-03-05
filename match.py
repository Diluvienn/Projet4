class Match:
    """Match"""

    def __init__(self, players: list, scores: list):
        if len(players) != 2:
            raise ValueError("A match must have exactly 2 players.")
        if len(scores) != 2:
            raise ValueError("A match must have exactly 2 scores.")
        self.players = players
        self.scores = scores

    def __str__(self):
        return f"Match: {self.players[0]} vs {self.players[1]}, Scores: {self.scores[0]}-{self.scores[1]}"


if __name__ == "__main__":
    pass
