from utils.formatvalidator import validate_date_format, validate_national_chess_id_format


def get_player_info_from_user():
    """Obtient les informations d'un nouveau joueur depuis l'entrée utilisateur."""
    while True:
        firstname = input("\nEntrez le prénom du joueur: ").title()
        if all(char.isalpha() or char == '-' for char in firstname):
            break
        else:
            print("Le prénom ne peut contenir que des lettres et des tirets. Veuillez réessayer.")

    while True:
        lastname = input("Entrez le nom de famille du joueur: ").title()
        if lastname.replace(' ', '').isalpha():
            break
        else:
            print("Le nom de famille ne peut contenir que des lettres et des espaces. Veuillez réessayer.")

    while True:
        birth = input("Entrez la date de naissance du joueur (format: dd-mm-yyyy): ")
        if validate_date_format(birth):
            break
        else:
            print("Format de date invalide. Veuillez utiliser le format 'dd-mm-yyyy'. Veuillez réessayer.")

    while True:
        national_chess_id = input("Entrez l'identifiant national du joueur (format: AB12345): ").upper()
        if validate_national_chess_id_format(national_chess_id):
            break
        else:
            print(
                "Format d'identifiant national invalide. Veuillez utiliser le format 'AB12345'.")

    return firstname, lastname, birth, national_chess_id


class PlayerView:
    def __init__(self, player_repository):
        self.player_repository = player_repository

    def show_players(self):
        self.player_repository.load_players()
        self.player_repository.display_players_by_index()
