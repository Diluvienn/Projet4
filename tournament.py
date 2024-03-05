from player import Player


class Tournament:
    """Tournament"""

    def __init__(self, name, place, start, end, rounds=4, current_round=1):
        self.name = name
        self.place = place
        self.start = start
        self.end = end
        self.rounds = rounds
        self.current_round = current_round
        self.rounds_list = []
        self.registered_players_list = []
        self.director_notes = ""

    def add_player(self, player):
        if isinstance(player, Player):
            self.registered_players_list.append(player)
        else:
            print("Error: Invalid player object.")

    def add_director_notes(self, note):
        self.director_notes += note + "\n"

    def add_round(self, round):
        self.rounds_list.append(round)

    def __str__(self):
        return (f"Tournament: {self.name}\nLocation: {self.place}\nStart: {self.start}\n"
                f"End: {self.end}\nRounds: {self.rounds}\n"
                f"Current Round: {self.current_round}\nDirector Notes: {self.director_notes}")


if __name__ == "__main__":
    pass
