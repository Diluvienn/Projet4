from model.tournament import Tournament, TournamentRepository
from model.player import Player, PlayerRepository
from utils.formatvalidator import validate_date_format, validate_national_chess_id_format



def create_tournament_from_cli():
    print("Création d'un nouveau tournoi:")
    name = input("Nom du tournoi : ")
    place = input("Lieu du tournoi : ")

    # Validation de la date de début
    while True:
        date_start = input("Date de début (format DD-MM-YYYY) : ")
        if validate_date_format(date_start):
            break
        print("Erreur : Format de date invalide. Veuillez saisir une date au format DD-MM-YYYY.")

    # Validation de la date de fin
    while True:
        date_end = input("Date de fin (format DD-MM-YYYY) : ")
        if validate_date_format(date_end):
            break
        print("Erreur : Format de date invalide. Veuillez saisir une date au format DD-MM-YYYY.")

    # Validation du nombre de rounds
    while True:
        rounds = input("Nombre de rounds (facultatif, par défaut 4) : ")
        if rounds.strip() == "":
            rounds = 4
            break
        try:
            rounds = int(rounds)
            break
        except ValueError:
            print("Erreur : Le nombre de rounds doit être un entier.")

    tournament = Tournament(name, place, date_start, date_end, rounds)

    print("Toutes les données ont été saisies avec succès.")
    print("Le tournoi a été créé avec succès.")
    return tournament

def add_player_from_cli():

    while True:
        # Validate player's firstname format
        while True:
            firstname = input("Prénom du joueur : ").capitalize()
            if firstname.isalpha():
                break
            print("Le prénom ne doit contenir que des lettres, sans accents ni tiret")

        # Validate player's lastname format
        while True:
            lastname = input("Nom de famille du joueur : ").capitalize()
            if lastname.isalpha():
                break
            print("Le nom de famille ne doit contenir que des lettres, sans accents ni tiret")

        # Validate birthday format
        while True:
            birth = input("Date de naissance du joueur (format DD-MM-YYYY) : ")
            if validate_date_format(birth):
                break
            print("Erreur : Format de date invalide. Veuillez saisir une date au format DD-MM-YYYY.")

        # Validate national chess id format
        while True:
            national_chess_id = input("Identifiant national d'échecs : ")
            if validate_national_chess_id_format(national_chess_id):
                break
            print("Erreur : Le numéro national d'échecs doit être du format AB12345.")

        print("Toutes les données ont été saisies avec succès.")
        break
    # Créer une instance de la classe Player avec les données fournies
    new_player = Player(firstname, lastname, birth, national_chess_id)
    print(f"Le joueur {new_player.firstname} {new_player.lastname} a été ajouté avec succès.")
    print("-" * 50)

    return new_player

    # Ajouter le nouveau joueur au référentiel des joueurs



def add_player_to_tournament_from_cli():
    player_repository = PlayerRepository()
    players = player_repository.load_players()
    selected_players = []

    # Affichage de la liste des joueurs avec leurs informations dans la console
    print("Liste des joueurs déjà enregistrés :")
    for i, player in enumerate(players):
        print(f"{i + 1}. {player['firstname']} {player['lastname']}")

    # Demande à l'utilisateur de sélectionner un joueur
    while True:
        user_choice_for_add_player = input("souhaitez-vous ajouter un joueur au tournoi depuis la liste (1), "
                                           "ajouter un nouveau joueur (2) "
                                           "ou arrêter l'ajout de joueurs (3) ?: ")
        if user_choice_for_add_player == "1":
            while True:
                try:
                    selection = int(input("Sélectionnez un joueur en entrant son numéro : "))
                    selected_player = player_repository.get_player_by_index(
                        selection - 1)  # -1 pour convertir le numéro de base 1 en index de base 0
                    selected_players.append(selected_player)
                    break
                except (ValueError, IndexError):
                    print("Veuillez entrer un numéro valide.")
            print(f"Ajout du joueur {selected_player.firstname} {selected_player.lastname}")
            print("-" * 50)


        elif user_choice_for_add_player == "2":
            new_player = add_player_from_cli()
            # Ajouter le nouveau joueur à la liste des joueurs sélectionnés
            selected_players.append(new_player)

            # Ajouter le nouveau joueur au référentiel des joueurs
            player_repository.add_player(new_player)
        #     while True:
        #         # Validate player's firstname format
        #         while True:
        #             firstname = input("Prénom du joueur : ").capitalize()
        #             if firstname.isalpha():
        #                 break
        #             print("Le prénom ne doit contenir que des lettres, sans accents ni tiret")
        #
        #         # Validate player's lastname format
        #         while True:
        #             lastname = input("Nom de famille du joueur : ").capitalize()
        #             if lastname.isalpha():
        #                 break
        #             print("Le nom de famille ne doit contenir que des lettres, sans accents ni tiret")
        #
        #
        #         # Validate birthday format
        #         while True:
        #             birth = input("Date de naissance du joueur (format DD-MM-YYYY) : ")
        #             if validate_date_format(birth):
        #                 break
        #             print("Erreur : Format de date invalide. Veuillez saisir une date au format DD-MM-YYYY.")
        #
        #         # Validate national chess id format
        #         while True:
        #             national_chess_id = input("Identifiant national d'échecs : ")
        #             if validate_national_chess_id_format(national_chess_id):
        #                 break
        #             print("Erreur : Le numéro national d'échecs doit être du format AB12345.")
        #
        #         print("Toutes les données ont été saisies avec succès.")
        #         break
        #     # Créer une instance de la classe Player avec les données fournies
        #     new_player = Player(firstname, lastname, birth, national_chess_id)
        #     print(f"Le joueur {new_player.firstname} {new_player.lastname} a été ajouté avec succès.")
        #     print("-" * 50)
        #
        #     # Ajouter le nouveau joueur à la liste des joueurs sélectionnés
        #     selected_players.append(new_player)
        #
        #     # Ajouter le nouveau joueur au référentiel des joueurs
        #     player_repository.add_player(new_player)
        #
        #
        elif user_choice_for_add_player == "3":
            break
        else:
            print("Veuillez indiquer un choix valide")

    # Initialiser les scores des joueurs sélectionnés à zéro
    for player in selected_players:
        player_name = f"{player.firstname} {player.lastname}"
        player.player_score = 0

    # Retourner à la fois les noms complets des joueurs en tant que chaînes de caractères et les objets Player
    return selected_players, [f"{player.firstname} {player.lastname}" for player in selected_players]

    # # return selected_players
    # # Retourner à la fois les noms complets des joueurs en tant que chaînes de caractères et les objets Player
    # return selected_players, [f"{player.firstname} {player.lastname}" for player in selected_players]

if __name__ == "__main__":

    players_list = add_player_to_tournament_from_cli()
    tournament = create_tournament_from_cli(players_list)

    # Affichage de tous les attributs du tournoi
    print("Attributs du tournoi :")
    for attribute, value in vars(tournament).items():
        if attribute == 'players_list':
            players_names = ", ".join([f"{player.firstname} {player.lastname}" for player in value])
            print(f"{attribute}: {players_names}")
        else:
            print(f"{attribute}: {value}")
