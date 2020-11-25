import os
import BlackAndWhite
import GaussianBlur
import Dilate

enter = "imgs/"
leave = "output/"

if not os.path.exists(leave):
    os.mkdir(leave)

with os.scandir(enter) as entries:
    if os.path.exists("imgs"):
        for entry in entries:
            if not entry.name.endswith((".jpg", ".png")):
                print(f"Le fichier n'est pas en bon format : {entry.name.split('.')[1]}")
            print(entry.name)
            BlackAndWhite.TransformNetB()
            GaussianBlur.TransformBlur()
            Dilate.TransformDilate()
    else:
        print("Le dossier n'existe pas")

