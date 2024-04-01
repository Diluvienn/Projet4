"""
Module for managing rounds in a tournament.

This module provides a RoundController class that handles the generation and playing of rounds
in a tournament. It also defines a Match class for representing individual matches.

Classes:
    - RoundController: Controller for managing rounds in a tournament.
    - Match: Represents an individual match between two players.

Dependencies:
    - model.match.Match: Class representing individual matches.
    - typing.List: Used for type hints in defining lists.
    - random.shuffle: Function for shuffling player lists to generate random matches.
"""

from model.match import Match
from typing import List

class RoundController:
    """Controller for managing rounds in a tournament."""

    def __init__(self, tournament):
        self.tournament = tournament
        self.played_pairs = set()
        # self.get_current_round = None
        self.matches: List[Match] = []
        self.current_round_index = 0



if __name__ == "__main__":
    pass

