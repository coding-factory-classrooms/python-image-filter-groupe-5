# Version du pauvre (Pour le moment)

list = ["grayscale", "blur", "dilate", "blur:[number]", "dilate:[number]", "grayscale|blur:[number]|dilate:[number]"]


def affichage():
    """
    Affichage de liste des filtres disponibles
    """
    for a in list:
        print(f"List des filtres disponibles")
        print(a)


affichage()
