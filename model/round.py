"""
This module contains the definition of the Round class, which represents a round
in a chess tournament. It also provides methods to generate matches for the round,
play all matches, and retrieve the list of matches in the round.

Classes:
    Round: A class representing a round in a tournament.

Usage:
    # Get the list of matches in the round
"""


class Round:
    """Class representing a round in a tournament."""

    def __init__(self, tournament):
        self.tournament = tournament
        self.name = f"round {self.tournament.current_round}"
        self.matches = []

    def get_matches(self):
        """Get the list of matches in the round.

        Returns:
            list: A list of Match objects representing the matches in the round.
        """
        return self.matches


if __name__ == "__main__":
    pass
