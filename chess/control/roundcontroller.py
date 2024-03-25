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

import random
from model.match import Match
from typing import List
import itertools

class RoundController:
    """Controller for managing rounds in a tournament."""

    def __init__(self, tournament):
        self.tournament = tournament
        self.played_pairs = set()
        # self.get_current_round = None
        self.matches: List[Match] = []
        self.current_round_index = 0


    def generate_matches(self):
        """Generate matches for this round.

        This method creates matches by pairing up players randomly from the tournament's player list.
        Each player is paired with another player who they have not yet played against in the tournament.

        Raises:
            ValueError: If the number of players in the tournament is not even, making it impossible to create pairs.
        """
        players = self.tournament.get_players()
        random.shuffle(players)

        # Check if the number of players is even to form pairs
        if len(players) % 2 != 0:
            raise ValueError("Le nombre de joueurs doit être pair pour former des paires de matchs.")

        # Generate matches by pairing players who haven't played against each other yet
        unique_pairs = []
        for i in range(0, len(players), 2):
            player1 = players[i]
            player2 = players[i + 1]
            pair = frozenset([player1, player2])
            if pair not in self.played_pairs:
                unique_pairs.append(pair)
            match = Match([player1, player2], [0, 0])
            self.matches.append(match)

    def get_current_round(self):
        """Returns the current round object."""
        if 0 <= self.current_round_index < len(self.tournament.rounds_list):
            return self.tournament.rounds_list[self.current_round_index]
        else:
            return None

    def already_played_in_previous_round(self, player1, player2):
        """Check if the given pair of players has already played in a previous round."""
        round_number = self.tournament.current_round
        for round_index in range(round_number - 1):
            for match in self.tournament.rounds_list[round_index].matches:
                if player1 in match.players and player2 in match.players:
                    return True
        return False


    def find_next_opponent(self, player, players):
        """Find the next opponent for the given player."""
        available_opponents = [p for p in players if p != player and frozenset([player, p]) not in self.played_pairs]
        return random.choice(available_opponents) if available_opponents else None
    def play_round(self):
        """Play all matches of this round.

        This method iterates through the matches of the round, plays each match,
        updates the scores, and increments the round counter of the tournament.

        After playing all matches, it prints the results of each match.

        Note:
        This method assumes that matches have already been generated using generate_matches().
        """
        print(f"Round {self.tournament.current_round}")

        # Play each match of the round
        for match in self.matches:
            player1, player2 = match.players
            print(f"Start : {player1} vs {player2}")
            match.play_match()
            score1, score2 = match.scores
            print(f"End : {player1} score : {score1}, {player2} score : {score2}")

        # Increment the round counter of the tournament
        self.tournament.current_round += 1
        print("-" * 50)


if __name__ == "__main__":
    pass

    # def generate_matches(self):
    #     """Generate matches for this round.
    #
    #     This method creates matches by pairing up players randomly from the tournament's player list.
    #     Each player is paired with another player who they have not yet played against in the tournament.
    #
    #     Raises:
    #         ValueError: If the number of players in the tournament is not even, making it impossible to create pairs.
    #     """
    #     players = self.tournament.get_players()
    #     random.shuffle(players)
    #
    #     # Check if the number of players is even to form pairs
    #     if len(players) % 2 != 0:
    #         raise ValueError("Le nombre de joueurs doit être pair pour former des paires de matchs.")
    #
    #     # Generate matches by pairing players who haven't played against each other yet
    #     unique_pairs = []
    #     for i in range(0, len(players), 2):
    #         player1 = players[i]
    #         player2 = players[i + 1]
    #         pair = frozenset([player1, player2])
    #         if pair not in self.played_pairs:
    #             unique_pairs.append(pair)
    #         match = Match([player1, player2], [0, 0])
    #         self.matches.append(match)


    # def get_current_round_matches(self):
    #     """Get the matches of the current round.
    #
    #     Returns:
    #         List[Match]: List of Match objects representing the matches of the current round.
    #                      If there are no matches in the current round, an empty list is returned.
    #     """
    #     if self.current_round is not None:
    #         return self.current_round.get_matches()
    #     else:
    #         return []

