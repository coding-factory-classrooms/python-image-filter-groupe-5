import cv2


def TransformZeTeam(img):
    """
    Permet de transformer plusieurs images avec notre prénom des membres de l'équipe
    :param img: dossier de l'image que l'on doit transformer
    :return: le filtre zeTeam est appliqué sur l'image
    """

    # font Type de police
    font = cv2.FONT_HERSHEY_SIMPLEX

    # org Cordonnée X et Y
    orgA = (0, 25)
    orgK = (0, 50)

    # fontScale
    fontScale = 1

    # Blue color in BGR
    color = (255, 0, 0)

    # Line thickness of 2 px Epaisseur du txt
    thickness = 2

    # Type de ligne à utiliser
    line_type = cv2.LINE_AA

    img = cv2.putText(img, f"Amandine", orgA, font, fontScale, color, thickness, line_type)
    img = cv2.putText(img, f"Killian", orgK, font, fontScale, color, thickness, line_type)

    return img
