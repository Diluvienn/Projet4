def main_user_choice():
    """Display main menu options and prompt user for choice.

    Returns:
        str: User's choice selected from the main menu options.

    Note:
        This function displays the main menu options to the user and prompts for user input.
        The user's choice is returned as a string.
    """
    print("Souhaitez-vous :\n"
          "1 : Voir la liste des joueurs\n"
          "2 : Voir la liste des tournois\n"
          "3 : Obtenir des informations sur un tournoi spécifique\n"
          "4 : Ajouter un joueur à la liste des joueurs\n"
          "5 : Créer un nouveau tournoi\n"
          "6 : Reprendre un tournoi non achevé\n"
          "7 : Quitter")

    return input("Mon choix (1, 2, 3, 4, 5, 6 ou 7): ")
