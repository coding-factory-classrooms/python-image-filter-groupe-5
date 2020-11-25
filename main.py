import os

import cv2

import BlackAndWhite
import GaussianBlur
import Dilate


enter = "imgs"
leave = "output"

if not os.path.exists(leave):
    os.mkdir(leave)

with os.scandir(enter) as entries:
    if os.path.exists("imgs"):
        for entry in entries:
            if not entry.name.endswith((".jpg", ".png")):
                print(f"Le fichier n'est pas en bon format : {entry.name.split('.')[1]}")
                continue
            print(entry.name)
            img = cv2.imread(f"{enter}/{entry.name}")
            img = BlackAndWhite.TransformNetB(img)
            img = GaussianBlur.TransformBlur(img)
            img = Dilate.TransformDilate(img)
            cv2.imwrite(f"{leave}/{entry.name}", img)
    else:
        print("Le dossier n'existe pas")

