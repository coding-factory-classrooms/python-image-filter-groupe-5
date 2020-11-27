import cv2


# Fonction qui permet de flouter l'image avec en paramètre l'image a modifié et la valeur du flou voulu
def TransformBlur(img, flou):
    """
    Permet de flouter plusieurs images
    :param img: dossier de l'image que l'on doit transformer
    :param flou: valeur défini par l'utilisateur, selon le floutage en nombre qu'il souhaite
    :return: le filtre blur (flou) appliqué sur l'image
    """
    # On défini un flou (Toujours Impair jamais pair sinon erreur)
    # On le modulo par deux pour avoir son reste décimal qui nous servira pour gérer les erreurs de s'il a mit entrée
    # un chiffre pair ou impair
    result = flou % 2
    # On fait un tryExecpt pour gérer les erreurs lié au CV2 de openCV
    try:
        # Si le flou est inférieur à 0 alors le chiffre est négatif, donc on lui de mettre un chiffre positif
        if flou < 0:
            print("La valeur entrée est négative, veuillez mettre un chiffre positif")
        # Si la valeur est strictement égale à 0, alors le chiffre est pair donc ça ne fonctionnera pas, il faut
        # mettre un chiffre impair
        if result == 0:
            print("Veuillez entrez des chiffres impair dans la taille du flou")
        # On applique les paramètres
        img = cv2.GaussianBlur(img, (flou, flou), 0)
    except cv2.error as e:
        # On affiche l'erreur
        print(e)

    # On retour le filtre
    return img
