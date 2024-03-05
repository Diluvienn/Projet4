import datetime


class Player:
    """Player"""

    def __init__(self, lastname: str, firstname: str, birth: str):
        if not lastname.isalpha():
            raise ValueError("Lastname must contain only letters without accent or hypen.")
        if not firstname.isalpha():
            raise ValueError("Firstname must contain only letters without accent or hypen..")
        if not self.validate_date_format(birth):
            raise ValueError("Invalid date format. Please use 'dd-mm-yyyy' format.")
        self.lastname = lastname.capitalize()
        self.firstname = firstname.capitalize()
        self.birth = birth

    def validate_date_format(self, date_string: str) -> bool:
        try:
            datetime.datetime.strptime(date_string, '%d-%m-%Y')
            return True
        except ValueError:
            return False


if __name__ == "__main__":
    pass
