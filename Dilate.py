import cv2
import numpy as np


# Fonction qui permet de dilater l'image avec en paramètre l'image a modifié et la valeur de dilation voulu
def TransformDilate(img, dilate):
    # Ce qui permet de dilater une image
    kernel = np.ones((5, 5), np.uint8)
    # iterations c'est si on veut qu'elle soit beaucoup dilater ou non
    img = cv2.dilate(img, kernel, iterations=dilate)
    # On retourne le filtre
    return img
