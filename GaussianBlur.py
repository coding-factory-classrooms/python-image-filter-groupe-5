import cv2


def TransformBlur(img):
    # Story 2
    flou = 9
    result = flou % 2
    try:
        if flou < 0:
            print("La valeur entrée est négative, veuillez mettre un chiffre positif")
        if result == 0:
            print("Veuillez entrez des chiffres impair dans la taille du flou")
        img = cv2.GaussianBlur(img, (flou, flou), 0)
    except cv2.error as e:
        print(e)

    return img
