class PlayerView:
    pass

    # def get_new_player_details(self):
    #     """Demande et récupère les détails d'un nouveau joueur depuis l'utilisateur."""
    #     print("Ajout d'un nouveau joueur :")
    #     firstname = input("Prénom du joueur : ").capitalize()
    #     lastname = input("Nom de famille du joueur : ").capitalize()
    #     birth = input("Date de naissance du joueur (format DD-MM-YYYY) : ")
    #     national_chess_id = input("Identifiant national d'échecs : ").upper()
    #
    #     return {
    #         "firstname": firstname,
    #         "lastname": lastname,
    #         "birth": birth,
    #         "national_chess_id": national_chess_id
    #     }
    #
    # @staticmethod
    # def display_player_list(players):
    #     """Affiche la liste des joueurs."""
    #     print("\nListe des joueurs :")
    #     for player in players:
    #         print(f"- {player['firstname']} {player['lastname']}")
    #
    # @staticmethod
    # def get_player_name():
    #     """Demande et récupère le nom d'un joueur depuis l'utilisateur."""
    #     return input("Entrez le nom du joueur : ")
    #
    # @staticmethod
    # def display_player_details(player):
    #     """Affiche les détails d'un joueur spécifique."""
    #     print("\nDétails du joueur :")
    #     print(f"Prénom : {player['firstname']}")
    #     print(f"Nom de famille : {player['lastname']}")
    #     print(f"Date de naissance : {player['birth']}")
    #     print(f"Identifiant national d'échecs : {player['national_chess_id']}")
    #
    # @staticmethod
    # def get_players_for_tournament():
    #     """Demande et récupère les joueurs à ajouter à un tournoi."""
    #     selected_players = []
    #     player_names = []
    #     print("Ajout de joueurs à un tournoi :")
    #     while True:
    #         player_name = input("Entrez le nom d'un joueur (ou 'fin' pour terminer) : ").capitalize()
    #         if player_name.lower() == 'fin':
    #             break
    #         selected_players.append(player_name)
    #         player_names.append(player_name)
    #     return selected_players, player_names
    #
    # @staticmethod
    # def display_message(message):
    #     """Affiche un message."""
    #     print(message)
