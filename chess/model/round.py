"""
This module contains the definition of the Round class, which represents a round
in a chess tournament. It also provides methods to generate matches for the round,
play all matches, and retrieve the list of matches in the round.

Classes:
    Round: A class representing a round in a tournament.

Usage:
    # Get the list of matches in the round
"""

from model.match import Match


class Round:
    """Class representing a round in a tournament."""

    def __init__(self, name, matches, start_time, end_time):
        self.name = name
        self.matches = []
        self.played_pairs = set()
        self.start_time = None
        self.end_time = None

    def to_json(self):
        start_time_str = str(self.start_time) if self.start_time else None
        end_time_str = str(self.end_time) if self.end_time else None
        return {
            "name": self.name,
            "matches": [match.to_json() for match in self.matches],
            "start_time": start_time_str,
            "end_time": end_time_str
        }

    @classmethod
    def from_json(cls, round_data, tournament):
        name = round_data["name"]
        matches_data = round_data["matches"]
        matches = [Match.from_json(match_data, tournament) for match_data in matches_data]
        start_time = round_data.get("start_time")
        end_time = round_data.get("end_time")
        round = cls(name, matches, start_time, end_time)
        round.matches.extend(matches)
        round.start_time = start_time
        round.end_time = end_time

        return round

    def add_match(self, match):
        """Ajoute un match à ce round."""
        self.matches.append(match)

    def get_matches(self):
        """Get the list of matches in the round.

        Returns:
            list: A list of Match objects representing the matches in the round.
        """
        return self.matches


if __name__ == "__main__":
    pass
