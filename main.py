import os

import cv2

import BlackAndWhite
import GaussianBlur
import Dilate
import ZeTeam

import logger as log

import listFilters as list

import sys


# Fonction du Programme
def args_fonction():
    """
    Permet de faire tourner le logiciel, condition pour les filtres selon ce qui est entrée en ligne de commandes,
    Vérification des dossiers si ils existes ou pas, vérification du .png ou .jpg pour les photos à transformer,
    Gestion de tout les erreurs possibles, récupération des arguments, variable crée pour évite le code en dur,
    Adaptable si changement de valeur,
    Implémentation des logs, affiche du menu et des logs
    """
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
                    # On saute le fichier et on lui indique que ce n'est pas le bon format et le nom du format
                    print(f"Le fichier n'est pas en bon format : {entry.name.split('.')[1]}")
                    # On log la même chose dans le fichier log pour avoir une trace
                    log.log(f"Le fichier n'est pas en bon format : {entry.name.split('.')[1]}")
                    # Et on continue le programme
                    continue
                # On stock dans la variable image, le dossier à lire grâce à openCV
                img = cv2.imread(f"{enter}/{entry.name}")
                # On vérifie les arguments entrée dans la CLI
                # Si le premier argument est "-h" alors on lui affiche la page d'aide
                if args[1] == "-h":
                    log.log(f"On affiche la liste d'aides des commandes à entrer")
                    print(f"Liste des commandes permises")
                    print(f"Fichier d'entrée : -i [nom du fichier d'entrée] (1er et 2ème argument)")
                    print(f"Fichier de sortie : -o [nom du fichier de sortie] (3ème et 4ème argument)")
                    print(f"Avoir de l'aide : -h (1er argument)")
                    print(f"Ajoute un filtre : --filters [nom du filtre ou des filtres]"
                          f" exemple 1: 'grayscale' ou 'blur'"
                          f" exemple 2 : 'grayscale|blur:3|dilate:5 (5ème et 6ème argument)")
                    print(f"Afficher les logs : --config-file (1er argument)")
                    print(f"Fichier de configuration : --config-file image.ini (1er argument)")
                    print(f"Liste des filtres disponible --list-filters (1er argument)")
                elif args[1] == "--list-filters":
                    list.affichage()
                # Si le premier argument est "--config-file" alors on lui affiche les logs
                elif args[1] == "--config-file":
                    log.dump_log()
                    log.log("On affiche les logs en console")
                # Sinon si le 1er argument est "-i" et que le 3ème est "-o" et le 5ème est "--filters" alors
                elif args[1] == "-i" and args[3] == "-o" and args[5] == "--filters":
                    # La variable enter vaux l'argument 2 soit le dossier dans lequel est situé les images à modifié
                    enter = args[2]
                    # La variable leave vaux l'argument 4 soit le dossier dans lequel seront stockées les images modifé
                    leave = args[4]
                    # La variable filters_args vaux l'argument 6 soit le filtre choisi "blur, grayscale ou dilate"
                    filters_args = args[6]
                    log.log("Vous avez choisi d'ajoute un filtre")
                    print("--filters, vous avez choisi un filtre")

                    # Si dans le chemin d'accès le dossier entrer dans leave n'existe pas
                    if not os.path.exists(leave):
                        # Alors on le crée
                        log.log("Création d'un dossier de sortie")
                        os.mkdir(leave)

                    # Ca supprimer toutes les barres au sein de la chaine de caractères et envoie les mots sous
                    # forme de liste
                    strBarre = filters_args.split("|")

                    # On boucle sur la liste renvoyé sans les barres
                    for a in strBarre:
                        # Si la liste commence par blur alors
                        if a.startswith("blur"):
                            # Si il y a deux points dans la variable a alors
                            if ":" in a:
                                # Alors on split pour récupérer la valeur d'après les deux points
                                value = a.split(":")[1]
                                # On applique le filtre blur sur tout les photos, on lui met la valeur donné par l'user
                                img = GaussianBlur.TransformBlur(img, int(value))
                                # On lui dit que c'est fait
                                print(f"Filtre Blur Appliqué = {entry.name}")
                                log.log(f"Filtre Blur Appliqué = {entry.name}")
                        # Si la liste commence par grayscale alors
                        elif a.startswith("grayscale"):
                            # On applique le filtre n&b sur tout les photos
                            img = BlackAndWhite.TransformNetB(img)
                            # On lui dit que c'est fait
                            print(f"Filtre Grayscale Appliqué = {entry.name}")
                            log.log(f"Filtre Grayscale Appliqué = {entry.name}")
                        # Si la liste commence par dilate alors
                        elif a.startswith("dilate"):
                            # Si il y a deux points dans la variable a alors
                            if ":" in a:
                                # Alors on split pour récupérer la valeur d'après les deux points
                                value = a.split(":")[1]
                                # On applique le filtre dilate sur tout les photos,on lui met la valeur donné par l'user
                                img = Dilate.TransformDilate(img, int(value))
                                # On lui dit que c'est fait
                                print(f"Filtre Dilate Appliqué = {entry.name}")
                                log.log(f"Filtre Dilate Appliqué = {entry.name}")
                            # Sinon on lui dit que le filtre n'est pas valide en lui mettant ce qu'il a entrée
                        # Si la liste commence par zeTeam alors
                        elif a.startswith("zeTeam"):
                            # On applique le filtre zeTeam sur tout les photos,
                            img = ZeTeam.TransformZeTeam(img)
                            # On lui dit que c'est fait
                            print(f"Filtre ZeTeam Appliqué = {entry.name}")
                            log.log(f"Filtre ZeTeam Appliqué = {entry.name}")
                        else:
                            log.log("Le nom du filtre est invalide")
                            print("filtre non valide")
                        print(f"FILTERS={filters_args}")
                        # On applique les filtres et on crée les fichiers si pas ou modifie
                        cv2.imwrite(f"{leave}/{entry.name}", img)
        # Sinon
        else:
            # On lui dit que le dossier d'entrée n'existe pas et on le crée
            log.log("Création d'un dossier d'entrée car le dossier d'entrée n'existe pas")
            print("Le dossier n'existe pas")
            os.mkdir(enter)


# On rappel la fonction
args_fonction()
