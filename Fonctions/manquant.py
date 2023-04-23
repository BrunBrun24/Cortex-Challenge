<<<<<<< HEAD
def manquant(donnee):
    """
    Fonction permettant de trouver le premier nombre manquant dans une liste de nombres.
    :return: int: Le premier nombre manquant dans la liste de nombres.
    """
    list_color = []  # Utilisation d'un ensemble pour stocker les couleurs disponibles
    list_numbers_color1 = []  # Utilisation d'un ensemble pour stocker les nombres de couleur 1
    list_numbers_color2 = []  # Utilisation d'un ensemble pour stocker les nombres de couleur 2

    # Permet de récupérer les couleurs disponibles et de les mettre dans "list_color"
    for color in donnee["numbers"]:
        list_color.append(color[-1])  # Ajouter la dernière lettre de chaque couleur à l'ensemble list_color

    # Permet de récupérer les nombres et de les mettre dans leur ensemble respectif
    for color in donnee["numbers"]:
        if color[-1] == list(list_color)[0]:  # Comparer la dernière lettre de la couleur avec la première lettre de list_color (converti en liste)
            list_numbers_color1.append(int(color[:-1]))  # Ajouter le nombre à l'ensemble list_numbers_color1 (en convertissant la chaîne de caractères en entier)
        else:
            list_numbers_color2.append(int(color[:-1]))  # Ajouter le nombre à l'ensemble list_numbers_color2 (en convertissant la chaîne de caractères en entier)

    list_numbers_color1.sort()
    list_numbers_color2.sort()

    # Trouver le premier nombre manquant dans list_numbers_color1
    for number in range(len(list_numbers_color1)-1):
        if list_numbers_color1[number+1] != list_numbers_color1[number]+1:
            return list_numbers_color1[number]+1

    # Trouver le premier nombre manquant dans list_numbers_color2
    for number in range(len(list_numbers_color2)-1):
        if list_numbers_color2[number+1] != list_numbers_color2[number]+1:
            return list_numbers_color2[number]+1

    return False  # Retourner False si tous les nombres sont présents


donnees = {"code": "MA-001", "type": "manquant", "numbers": ["1R", "4R", "5R", "4B", "7B", "8B", "2R", "3R", "5B"]}

output = manquant(donnees)
print(output)
=======
def manquant(donnee):
    """
    Fonction permettant de trouver le premier nombre manquant dans une liste de nombres.
    :return: int: Le premier nombre manquant dans la liste de nombres.
    """
    list_color = []  # Utilisation d'un ensemble pour stocker les couleurs disponibles
    list_numbers_color1 = []  # Utilisation d'un ensemble pour stocker les nombres de couleur 1
    list_numbers_color2 = []  # Utilisation d'un ensemble pour stocker les nombres de couleur 2

    # Permet de récupérer les couleurs disponibles et de les mettre dans "list_color"
    for color in donnee["numbers"]:
        list_color.append(color[-1])  # Ajouter la dernière lettre de chaque couleur à l'ensemble list_color

    # Permet de récupérer les nombres et de les mettre dans leur ensemble respectif
    for color in donnee["numbers"]:
        if color[-1] == list(list_color)[0]:  # Comparer la dernière lettre de la couleur avec la première lettre de list_color (converti en liste)
            list_numbers_color1.append(int(color[:-1]))  # Ajouter le nombre à l'ensemble list_numbers_color1 (en convertissant la chaîne de caractères en entier)
        else:
            list_numbers_color2.append(int(color[:-1]))  # Ajouter le nombre à l'ensemble list_numbers_color2 (en convertissant la chaîne de caractères en entier)

    list_numbers_color1.sort()
    list_numbers_color2.sort()

    # Trouver le premier nombre manquant dans list_numbers_color1
    for number in range(len(list_numbers_color1)-1):
        if list_numbers_color1[number+1] != list_numbers_color1[number]+1:
            return list_numbers_color1[number]+1

    # Trouver le premier nombre manquant dans list_numbers_color2
    for number in range(len(list_numbers_color2)-1):
        if list_numbers_color2[number+1] != list_numbers_color2[number]+1:
            return list_numbers_color2[number]+1

    return False  # Retourner False si tous les nombres sont présents


donnees = {"code": "MA-001", "type": "manquant", "numbers": ["1R", "4R", "5R", "4B", "7B", "8B", "2R", "3R", "5B"]}

output = manquant(donnees)
print(output)
>>>>>>> 6e34e0d79324732dd1b147a0914c1d5e98739c19
