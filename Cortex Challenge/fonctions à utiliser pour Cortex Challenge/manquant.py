def manquant(donnees):
    """
    Fonction permettant de trouver le premier nombre manquant dans une liste de nombres.
    :return: int: Le premier nombre manquant dans la liste de nombres.
    """
    list_color = [] # List des couleurs disponible
    list_numbers_color1 = []
    list_numbers_color2 = []
    # Permet de récupérer les couleurs disponible et de les mettre dans "list_color"
    for color in donnees["numbers"]:
        # On sait que l'initiale de la couleur est au dernier caractère
        if color[-1] not in list_color:
            list_color.append(color[-1])
    # Permet de récupérer les nombres et de les mettres dans leur list respective
    for color in donnees["numbers"]:
        if color[-1] == list_color[0]:
            list_numbers_color1.append(color[:-1])
        else:
            list_numbers_color2.append(color[:-1])

    # On trie les listes avec les nombres
    list_numbers_color1.sort()
    list_numbers_color2.sort()

    for number in range(len(list_numbers_color1)-1):
        n = list(map(int, list_numbers_color1))
        if n[number+1] != n[number]+1:
            return n[number]+1

    for number in range(len(list_numbers_color2)-1):
        n = list(map(int, list_numbers_color2))
        if n[number+1] != n[number]+1:
            return n[number]+1

    return False