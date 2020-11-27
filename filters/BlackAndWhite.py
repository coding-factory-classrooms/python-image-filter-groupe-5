import cv2


# Fonction qui permet de transformer l'image en noir et blanc
def TransformNetB(img):
    """
    Permet de transformer plusieurs images en noir et blanc
    :param img: dossier de l'image que l'on doit transformer
    :return: le filtre noir et blanc appliqué sur l'image
    """
    try:
        # Ligne qui permet de dire que l'image entrée en paramètre va etre converti en noir et blanc
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    except cv2.error as e:
        print(e)
    # Et on retourne la couleur noir et blanc (le filtre)
    return img
