import os

from numpy.core.defchararray import lower


def affichage():
    """
    Affichage de liste des filtres disponibles
    """
    print(f"List des filtres disponibles (Tout en minuscules)")
    with os.scandir("filters") as entries:
        for entry in entries:
            var = entry.name.split(".py")
            for a in var:
                print(lower(a))
