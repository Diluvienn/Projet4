"""
This module contains a function to validate the format of a date string and ensure it conforms to
the 'dd-mm-yyyy' format.

"""

import datetime


def validate_date_format(date_string: str) -> bool:
    """Validate the format of a date string.

    Args:
        date_string (str): A string representing a date in the format 'dd-mm-yyyy'.

    Returns:
        bool: True if the date string has the correct format, False otherwise.
    """
    try:
        datetime.datetime.strptime(date_string, '%d-%m-%Y')
        return True
    except ValueError:
        return False


def validate_national_chess_id_format(national_chess_id: str) -> bool:
    if len(national_chess_id) != 7:
        return False
    if not national_chess_id[:2].isalpha():
        return False
    if not national_chess_id[2:].isdigit():
        return False

    return True


if __name__ == "__main__":
    pass
