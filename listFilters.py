# Version du pauvre (Pour le moment)

list = ["grayscale", "blur", "dilate", "blur:[number]", "dilate:[number]", "grayscale|blur:[number]|dilate:[number]"]


def affichage():
    for a in list:
        print(f"List des filtres disponibles")
        print(a)


affichage()
