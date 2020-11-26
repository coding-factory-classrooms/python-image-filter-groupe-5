import cv2


# Fonction qui permet de transformer l'image en noir et blanc
def TransformNetB(img):
    # Ligne qui permet de dire que l'image entrée en paramètre va etre converti en noir et blanc
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Et on retourne la couleur noir et blanc (le filtre)
    return img
