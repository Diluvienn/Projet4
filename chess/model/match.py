"""This module contains the definition of the Match class, which represents a match
in a chess tournament. It provides methods to initialize a match with players and scores,
simulate playing the match, and obtain a string representation of the match.

Classes:
    Match: A class representing a match in a chess tournament.

Usage:
    # Create a Match instance
    # Play the match
    # Get the string representation of the match
"""

import datetime
import random

possible_score = [(0, 1), (0.5, 0.5), (1, 0)]


class Match:
    """A class representing a match in a chess tournament."""

    def __init__(self, players: list, scores: list = [0, 0]):
        """Initialize a Match object with the given players and scores.

        Args:
            players (list): A list containing exactly two Player objects representing the players in the match.
            scores (list, optional): A list containing exactly two integers representing the initial scores of the players. Defaults to [0, 0].

        Raises:
            ValueError: If the length of the 'players' list is not 2 or if the length of the 'scores' list is not 2.
        """
        if len(players) != 2:
            raise ValueError("A match must have exactly 2 players.")
        if len(scores) != 2:
            raise ValueError("A match must have exactly 2 scores.")
        self.players: list = players
        self.scores: list = scores
        self.name: str = "Round 1"
        self.start: str = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.end: str = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    def __str__(self):
        """Return a string representation of the Match object."""
        return f"Match: {self.players[0]} vs {self.players[1]}, Scores: {self.scores[0]}-{self.scores[1]}"

    def play_match(self):
        """Simulate the playing of the match by randomly selecting scores."""
        random.shuffle(possible_score)
        score = random.choice(possible_score)
        self.scores = score


if __name__ == "__main__":
    pass
