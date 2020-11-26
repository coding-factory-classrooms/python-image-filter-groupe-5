import cv2


def TransformZeTeam(img):

    # font
    font = cv2.FONT_HERSHEY_SIMPLEX

    # org
    orgA = (0, 25)
    orgK = (0, 50)
    # fontScale
    fontScale = 1

    # Blue color in BGR
    color = (255, 0, 0)

    # Line thickness of 2 px
    thickness = 2

    line_type = cv2.LINE_AA

    img = cv2.putText(img, f"Amandine", orgA, font, fontScale, color, thickness, line_type)
    img = cv2.putText(img, f"Killian", orgK, font, fontScale, color, thickness, line_type)

    return img
