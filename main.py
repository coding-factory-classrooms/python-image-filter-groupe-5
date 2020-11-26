import os

import cv2

import BlackAndWhite
import GaussianBlur
import Dilate

import sys


def args_fonction():
    args = sys.argv
    enter = "imgs"

    with os.scandir(enter) as entries:
        if os.path.exists(enter):
            for entry in entries:
                if not entry.name.endswith((".jpg", ".png")):
                    print(f"Le fichier n'est pas en bon format : {entry.name.split('.')[1]}")
                    continue
                img = cv2.imread(f"{enter}/{entry.name}")
                if args[1] == "-h":
                    print(f"---help")
                elif args[1] == "-i" and args[3] == "-o" and args[5] == "--filters":
                    enter = args[2]
                    print(enter)
                    leave = args[4]
                    print(leave)
                    filters_args = args[6]
                    print(f"{enter}, {leave}, {filters_args}")
                    print("--filters, vous avez choisi un filtre")
                    if not os.path.exists(leave):
                        os.mkdir(leave)
                    if filters_args == 'grayscale':
                        img = BlackAndWhite.TransformNetB(img)
                        print(f"Filtre Grayscale Appliqué = {entry.name}")
                    elif filters_args == 'blur':
                        img = GaussianBlur.TransformBlur(img)
                        print(f"Filtre Blur Appliqué = {entry.name}")
                    elif filters_args == 'dilate':
                        img = Dilate.TransformDilate(img)
                        print(f"Filtre Dilate Appliqué = {entry.name}")
                    else:
                        print("filtre non valide")
                    print(f"FILTERS={filters_args}")
                    cv2.imwrite(f"{leave}/{entry.name}", img)
        else:
            print("Le dossier n'existe pas")


args_fonction()

