import cv2


def TransformBlur():
    # Story 2
    flou = 9
    result = flou % 2
    try:
        if flou < 0:
            print("La valeur entrée est négative, veuillez mettre un chiffre positif")
        img = cv2.imread("imgs/Logo_Tirna.jpg")
        if result == 0:
            print("Veuillez entrez des chiffres impair dans la taille du flou")
        img = cv2.GaussianBlur(img, (flou, flou), 0)
        cv2.imwrite("output/Logo_Tirna_Blur.jpg", img)
    except cv2.error as e:
        print(e)
