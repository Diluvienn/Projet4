class TournamentView:
    @staticmethod
    def display_menu():
        """Affiche le menu principal de gestion des tournois."""
        print("\nMenu Principal:")
        print("1. Afficher la liste des tournois")
        print("2. Afficher les détails d'un tournoi")
        print("3. Créer un nouveau tournoi")
        print("4. Reprendre un tournoi non terminé")
        print("5. Quitter")

    @staticmethod
    def display_tournament_list(tournaments):
        """Affiche la liste des tournois."""
        print("\nListe des tournois:")
        for tournament in tournaments:
            print(f"- {tournament.name}")

    @staticmethod
    def display_tournament_details(tournament):
        """Affiche les détails d'un tournoi spécifique."""
        print("\nDétails du tournoi:")
        print(f"Nom: {tournament.name}")
        print(f"Lieu: {tournament.place}")
        print(f"Date de début: {tournament.date_start}")
        print(f"Date de fin: {tournament.date_end}")
        print(f"Nombre de rounds: {tournament.rounds}")
        # Afficher d'autres détails du tournoi si nécessaire

    @staticmethod
    def display_message(message):
        """Affiche un message spécifique."""
        print(message)

    @staticmethod
    def get_new_tournament_details():
        """Demande à l'utilisateur de saisir les détails pour créer un nouveau tournoi."""
        print("*" * 100)
        print("Création d'un nouveau tournoi:")
        name = input("Nom du tournoi : ").capitalize()
        place = input("Lieu du tournoi : ").capitalize()
        date_start = input("Date de début (format DD-MM-YYYY) : ")
        date_end = input("Date de fin (format DD-MM-YYYY) : ")
        rounds = input("Nombre de rounds (facultatif, par défaut 4) : ")
        return name, place, date_start, date_end, rounds
