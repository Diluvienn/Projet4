import os
import json

from model.player import Player


class PlayerRepository:
    """Repository for managing player data storage and retrieval."""

    def __init__(self, filename='players.json'):
        """Initialize the PlayerRepository.

        Args:
            filename (str, optional): Name of the JSON file to store player data. Defaults to 'players.json'.
        """
        data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
        self.filename = os.path.join(data_dir, filename)

    def add_player(self, player):
        """Add a player to the repository.

        Args:
            player (Player): The player object to be added.

        Notes:
            This method first loads existing players from the JSON file,
            adds the new player to the list, and then writes the updated list
            back to the JSON file.

        Args:
            player (Player): The player object to be added to the repository.
        """

        players = self.load_players()
        players.append(player.to_json())

        # Écriture de la liste mise à jour dans le fichier JSON
        with open(self.filename, 'w') as file:
            json.dump(players, file, indent=4)

    def load_players(self):
        """Load players from the JSON file.

        Returns:
            List[dict]: A list of dictionaries containing player information loaded from the JSON file.
                        If the file does not exist, an empty list is returned.
        """
        if not os.path.exists(self.filename):
            return []

        with open(self.filename, 'r') as file:
            players = json.load(file)
        return players

    def get_player_by_index(self, index):
        """Get a player from the repository by index.

        Args:
            index (int): The index of the player in the repository.

        Returns:
            Player: The player object corresponding to the given index.

        Note:
            This method retrieves player data from the repository by index,
            creates a Player object from the data, and returns the Player instance.

        """
        players = self.load_players()
        player_data = players[index]
        player_instance = Player(player_data['firstname'], player_data['lastname'], player_data['birth'],
                                 player_data['national chess ID'])
        return player_instance

    def get_player_by_alphabetical_order(self):
        """Get players from the repository sorted alphabetically by last name.

        Returns:
            List[str]: A list of formatted strings representing player information sorted alphabetically
                       by last name.

        Note:
            This method retrieves player data from the repository, sorts the players alphabetically
            by last name, formats the player information, and returns a list of formatted strings.
        """
        players = self.load_players()
        sorted_players = sorted(players, key=lambda x: x['lastname'])
        formatted_output = []
        for player_data in sorted_players:
            player_details = [
                f"Nom: {player_data['lastname']} {player_data['firstname']}",
                f"Date de naissance: {player_data['birth']}",
                f"National chess ID: {player_data['national chess ID']}",
                f"~" * 25
            ]
            formatted_output.extend(player_details)

        return formatted_output


if __name__ == "__main__":
    pass
