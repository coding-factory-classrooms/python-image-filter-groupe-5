import os

import cv2

import BlackAndWhite
import GaussianBlur
import Dilate

import sys


# Fonction du Programme
def args_fonction():
    # On récupère les arguments
    args = sys.argv
    # Variable qui stocke le dossier où se trouve les images à modifier
    enter = "imgs"

    # Permet de lire les éléments qui se trouve dans le dossier enter et on la renomme avec un alias en "entries"
    with os.scandir(enter) as entries:
        # Si dans le chemin d'accès le dossier indiqué dans la variable enter existe alors
        if os.path.exists(enter):
            # On fait une boucle pour récupérer les objets dans le dossier enter
            for entry in entries:
                # On vérifie que la fin des noms des fichiers est bien en .jpg ou .png sinon
                if not entry.name.endswith((".jpg", ".png")):
                    # On saute le fichier et on lui indique que ce n'est pas le bon format
                    print(f"Le fichier n'est pas en bon format : {entry.name.split('.')[1]}")
                    # Et on continue le programme
                    continue
                # On stock dans la variable image, le dossier à lire grâce à openCV
                img = cv2.imread(f"{enter}/{entry.name}")
                # On vérifie les arguments entrée dans la CLI
                # Si le premier argument est "-h" alors on lui affiche la page d'aide
                if args[1] == "-h":
                    print(f"---help")
                # Sinon si le 1er argument est "-i" et que le 3ème est "-o" et le 5ème est "--filters" alors
                elif args[1] == "-i" and args[3] == "-o" and args[5] == "--filters":
                    # La variable enter vaux l'argument 2 soit le dossier dans lequel est situé les images à modifié
                    enter = args[2]
                    # La variable leave vaux l'argument 4 soit le dossier dans lequel seront stockées les images modifé
                    leave = args[4]
                    # La variable filters_args vaux l'argument 6 soit le filtre choisi "blur, grayscale ou dilate"
                    filters_args = args[6]
                    print("--filters, vous avez choisi un filtre")
                    # Story 7

                    # Split si après filters_args (blur, grayscale, dilate) il y a une | alors,
                    # c'est qu'il y a un autre argument derrière

                    # Split si après filters_args (blur, dilate) il y a : alors il y a une valeur derrière à récupérer

                    # Les splits sont stockés dans une variable

                    # Boucle sur la variable des splits

                    # 2 lignes à ajouter
                    # Si dans le chemin d'accès le dossier entrer dans leave n'existe pas
                    if not os.path.exists(leave):
                        # Alors on le crée
                        os.mkdir(leave)
                    # Si dans filters_agrs donc l'argument il y marqué
                    # grayscale alors
                    if filters_args == 'grayscale':
                        # On applique le filtre n&b sur tout les photos
                        img = BlackAndWhite.TransformNetB(img)
                        # On lui dit que c'est fait
                        print(f"Filtre Grayscale Appliqué = {entry.name}")
                    # blur alors
                    elif filters_args == 'blur':
                        # On applique le filtre blur sur tout les photos
                        img = GaussianBlur.TransformBlur(img)
                        # On lui dit que c'est fait
                        print(f"Filtre Blur Appliqué = {entry.name}")
                    # dilate alors
                    elif filters_args == 'dilate':
                        # On applique le filtre dilate sur tout les photos
                        img = Dilate.TransformDilate(img)
                        # On lui dit que c'est fait
                        print(f"Filtre Dilate Appliqué = {entry.name}")
                    # Sinon on lui dit que le filtre n'est pas valide en lui mettant ce qu'il a entrée
                    else:
                        print("filtre non valide")
                    print(f"FILTERS={filters_args}")
                    # On applique les filtres et on crée les fichiers si pas ou modifie
                    cv2.imwrite(f"{leave}/{entry.name}", img)
        # Sinon
        else:
            # On lui dit que le dossier d'entrée n'existe pas et on le crée
            print("Le dossier n'existe pas")
            os.mkdir(enter)


# On rappel la fonction
args_fonction()
