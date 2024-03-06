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


if __name__ == "__main__":
    pass
