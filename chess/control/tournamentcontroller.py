def add_director_notes_to_tournament():
    notes = input("Avez-vous des notes de directeurs à ajouter (y/n) ? :")
    if notes == "y":
        notes = input("Vous pouvez les ajouter ici : ")
    elif notes == "n":
        notes = ""
    else:
        print("Veuillez effectuer un choix valide.")

    return notes
