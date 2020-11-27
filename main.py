import os

import cv2

from filters import BlackAndWhite, GaussianBlur, Dilate, ZeTeam

import logger as log

import listFilters as list

import configparser

import sys


# Fonction du Programme
def args_fonction():
    """
    Permet de faire tourner le logiciel, condition pour les filtres selon ce qui est entrée en ligne de commandes,
    Vérification des dossiers si ils existes ou pas, vérification du .png ou .jpg pour les photos à transformer,
    Gestion de tout les erreurs possibles, récupération des arguments, variable crée pour évite le code en dur,
    Adaptable si changement de valeur,
    Implémentation des logs, affiche du menu et des logs,
    Gestion de tout le programmes
    """
    # On récupère les arguments
    args = sys.argv
    # Variable qui stocke le dossier où se trouve les images à modifier
    enter = ""
    leave = ""
    filters_args = ""
    i = 0

    # Si le premier argument est "--config-file" alors on lui affiche les logs
    if "--config-file" in args:
        index_ini = args.index("--config-file")
        file_ini = args[index_ini + 1]
        config = configparser.ConfigParser()
        config.read(file_ini)
        enter = config["general"]["input_dir"]
        leave = config["general"]["output_dir"]
        filters_args = config["filters"]["content"]
        print(f"enter = {enter}")
        print(f"leave = {leave}")
        print(f"filters_args = {filters_args}")
        log.log("Utilisation du fichier ini pour appliqué les filtres")
    elif "--list-filters" in args:
        list.affichage()
        sys.exit(0)
    elif "--log-file" in args:
        log.dump_log()
        log.log("On affiche les logs en console")
        sys.exit(0)

    for a in args:
        # On vérifie les arguments entrée dans la CLI
        # Si le premier argument est "-h" alors on lui affiche la page d'aide
        if a == "-h":
            log.log(f"On affiche la liste d'aides des commandes à entrer")
            print(f"Liste des commandes permises")
            print(f"Fichier d'entrée : -i [nom du fichier d'entrée]")
            print(f"Fichier de sortie : -o [nom du fichier de sortie]")
            print(f"Avoir de l'aide : -h")
            print(f"Ajoute un filtre : --filters [nom du filtre ou des filtres]"
                  f" exemple 1: 'grayscale' ou 'blur'"
                  f" exemple 2 : 'grayscale|blur:3|dilate:5")
            print(f"Afficher les logs : --config-file [nom du fichier]")
            print(f"Liste des filtres disponible --list-filters")
            sys.exit(0)
        elif a == "-i":
            enter = args[i + 1]
        elif a == "-o":
            leave = args[i + 1]
        elif a == "--filters":
            filters_args = args[i + 1]
            log.log(f"{a}, vous avez choisi un filtre")
        i += 1

    # Si dans le chemin d'accès le dossier entrer dans leave n'existe pas
    if not os.path.exists(leave):
        # Alors on le crée
        log.log("Création d'un dossier de sortie")
        os.mkdir(leave)

    # Ca supprimer toutes les barres au sein de la chaine de caractères et envoie les mots sous
    # forme de liste
    strBarre = filters_args.split("|")

    # Permet de lire les éléments qui se trouve dans le dossier enter et on la renomme avec un alias en "entries"
    with os.scandir(enter) as entries:
        # Si dans le chemin d'accès le dossier indiqué dans la variable enter existe alors
        if os.path.exists(enter):
            # On fait une boucle pour récupérer les objets dans le dossier enter
            for entry in entries:
                # On vérifie que la fin des noms des fichiers est bien en .jpg ou .png sinon
                if not entry.name.endswith((".jpg", ".png")):
                    # On saute le fichier et on lui indique que ce n'est pas le bon format et le nom du format
                    # On log la même chose dans le fichier log pour avoir une trace
                    log.log(f"Le fichier n'est pas en bon format : {entry.name.split('.')[1]}")
                    # Et on continue le programme
                    continue
                # On stock dans la variable image, le dossier à lire grâce à openCV
                img = cv2.imread(f"{enter}/{entry.name}")

                # On boucle sur la liste renvoyé sans les barres
                for a in strBarre:
                    # Si la liste commence par blur alors
                    if a.startswith("blur"):
                        # Alors on split pour récupérer la valeur d'après les deux points
                        value = a.split(":")
                        if len(value) != 2:
                            log.log("Intensité du flou manquante")
                            continue
                        # On applique le filtre blur sur tout les photos, on lui met la valeur donné par l'user
                        img = GaussianBlur.TransformBlur(img, int(value[1]))
                        # On lui dit que c'est fait
                        log.log(f"Filtre Blur Appliqué = {entry.name}")
                    # Si la liste commence par grayscale alors
                    elif a.startswith("grayscale"):
                        # On applique le filtre n&b sur tout les photos
                        img = BlackAndWhite.TransformNetB(img)
                        # On lui dit que c'est fait
                        log.log(f"Filtre Grayscale Appliqué = {entry.name}")
                    # Si la liste commence par dilate alors
                    elif a.startswith("dilate"):
                        value = a.split(":")
                        if len(value) != 2:
                            log.log("Intensité du dilate manquante")
                            continue
                        # On applique le filtre dilate sur tout les photos,on lui met la valeur donné par l'user
                        img = Dilate.TransformDilate(img, int(value[1]))
                        # On lui dit que c'est fait
                        log.log(f"Filtre Dilate Appliqué = {entry.name}")
                        # Sinon on lui dit que le filtre n'est pas valide en lui mettant ce qu'il a entrée
                    # Si la liste commence par zeTeam alors
                    elif a.startswith("zeteam"):
                        # On applique le filtre zeTeam sur tout les photos,
                        img = ZeTeam.TransformZeTeam(img)
                        # On lui dit que c'est fait
                        log.log(f"Filtre ZeTeam Appliqué = {entry.name}")
                    else:
                        log.log("Le nom du filtre est invalide")
                    print(f"FILTERS={filters_args}")
                    try:
                        # On applique les filtres et on crée les fichiers si pas ou modifie
                        cv2.imwrite(f"{leave}/{entry.name}", img)
                    except cv2.error as e:
                        print(e)
        # Sinon
        else:
            # On lui dit que le dossier d'entrée n'existe pas et on le crée
            log.log("Création d'un dossier d'entrée car le dossier d'entrée n'existe pas")
            print("Le dossier n'existe pas")
            os.mkdir(enter)


# On rappel la fonction
args_fonction()
