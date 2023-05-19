def manquant(defis):
    """
    Fonction permettant de trouver le premier nombre manquant dans une liste de nombres.
    :return: int: Le premier nombre manquant dans la liste de nombres.
    """
    list_color = []  # Utilisation d'un ensemble pour stocker les couleurs disponibles
    list_numbers_color1 = []  # Utilisation d'un ensemble pour stocker les nombres de couleur 1
    list_numbers_color2 = []  # Utilisation d'un ensemble pour stocker les nombres de couleur 2

    # Permet de récupérer une couleur disponible et de les mettre dans "list_color"
    couleur = defis["numbers"][0][-1]

    # Permet de récupérer les nombres et de les mettre dans leur ensemble respectif
    for color in defis["numbers"]:
        if color[-1] == couleur:
            list_numbers_color1.append(int(color[:-1]))
        else:
            list_numbers_color2.append(int(color[:-1]))

    list_numbers_color1 = sorted(list_numbers_color1, key=int)
    list_numbers_color2 = sorted(list_numbers_color2, key=int)

    # Trouver le premier nombre manquant dans list_numbers_color1
    for number in range(len(list_numbers_color1)-1):
        if list_numbers_color1[number+1] != list_numbers_color1[number]+1:
            return list_numbers_color1[number]+1

    # Trouver le premier nombre manquant dans list_numbers_color2
    for number in range(len(list_numbers_color2)-1):
        if list_numbers_color2[number+1] != list_numbers_color2[number]+1:
            return list_numbers_color2[number]+1

    return False  # Retourner False si tous les nombres sont présents