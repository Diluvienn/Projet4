def add_director_notes_to_tournament():
    notes = input("Avez-vous des notes de directeurs à ajouter (y/N) ? :")
    if notes == "y":
        notes = input("Vous pouvez les ajouter ici : ")
    else:
        notes = ""

    return notes
