"""
This module contains the definition of the Player class, which represents a player
with a first name, last name, birth date, and score. It also includes a function
to validate the format of a date string.

Classes:
    Player: A class representing a player with a first name, last name, birth date, and score.

Functions:
    validate_date_format: Validate the format of a date string in 'dd-mm-yyyy' format.

Usage:
    from formatvalidator import validate_date_format
    from player import Player

    # Create a player instance with a validated birth date
    player = Player("John", "Doe", "01-01-1990")
"""


from formatvalidator import validate_date_format


class Player:
    """Player"""

    def __init__(self, firstname: str, lastname: str, birth: str):
        if not firstname.isalpha():
            raise ValueError("Firstname must contain only letters without accent or hypen..")
        if not lastname.isalpha():
            raise ValueError("Lastname must contain only letters without accent or hypen.")
        if not validate_date_format(birth):
            raise ValueError("Invalid date format. Please use 'dd-mm-yyyy' format.")
        self.firstname = firstname.capitalize()
        self.lastname = lastname.capitalize()
        self.birth = birth
        self.score = 0


if __name__ == "__main__":
    pass
