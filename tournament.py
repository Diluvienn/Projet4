from player import Player
from formatvalidator import validate_date_format


class Tournament:
    """A class representing a chess tournament."""

    def __init__(self, name, place, start, end, rounds=4, current_round=1):
        if not validate_date_format(start):
            raise ValueError("Invalid date format. Please use 'dd-mm-yyyy' format.")
        if not validate_date_format(end):
            raise ValueError("Invalid date format. Please use 'dd-mm-yyyy' format.")
        self.name = name
        self.place = place
        self.start = start
        self.end = end
        self.rounds = rounds
        self.current_round = current_round
        self.rounds_list = []
        self.players_list = []
        self.director_notes = ""

    def add_player(self, player):
        """Add a player to the tournament.

            Args:
                player (Player): The player object to be added to the tournament.

            """
        self.players_list.append(player)


    def get_players(self):
        """Get the list of players registered for the tournament."""
        return [f"{player.firstname} {player.lastname}" for player in self.players_list]

    def add_director_notes(self, note):
        """Add notes from the tournament director.

        Args:
            note (str): The note to be added.

        Returns:
            None
        """
        self.director_notes += note + "\n"

    def add_round(self, round):
        """Add a round to the tournament.

        Args:
            round: The round object to be added to the tournament.
        """
        self.rounds_list.append(round)

    def __str__(self):
        return (f"Tournament: {self.name}\nLocation: {self.place}\nStart: {self.start}\n"
                f"End: {self.end}\nRounds: {self.rounds}\n"
                f"Current Round: {self.current_round}\nDirector Notes: {self.director_notes}")


if __name__ == "__main__":
    pass
