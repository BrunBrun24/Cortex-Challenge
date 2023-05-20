def reflexion(defis):
    return parcours_lampe_torche(defis, "haut", 5, 2)

def parcours_lampe_torche(donnees, direction, ligne, colonne):
    """
    Parcours la map en suivant le faisceau lumineux
    :param:
        direction : "string"
        ligne : "int"
        colonne : "int"
    :return: un entier (int)
    """
    if type(donnees["map"][ligne][colonne]) == int:
        result = [donnees["map"][ligne][colonne]]
        return result

    direction = si_miroir(donnees, direction, ligne, colonne)

    if direction == "bas":
        return parcours_lampe_torche(donnees, direction, ligne+1, colonne)
    elif direction == "haut":
        return parcours_lampe_torche(donnees, direction, ligne-1, colonne)
    elif direction == "droite":
        return parcours_lampe_torche(donnees, direction, ligne, colonne+1)
    else:
        return parcours_lampe_torche(donnees, direction, ligne, colonne-1)

def si_miroir(donnees, direction, ligne, colonne):
    """
    Indique si sur les coordonnées pris en paramètres, il y a un miroir
    :param:
        direction : "string"
        ligne : "int"
        colonne : "int"
    :return: la direction (string)
    """
    if donnees["map"][ligne][colonne] == "/":
        if direction == "haut":
            return "droite"
        elif direction == "bas":
            return "gauche"
        elif direction == "droite":
            return "haut"
        elif direction == "gauche":
            return "bas"
    elif donnees["map"][ligne][colonne] == "\\":
        if direction == "haut":
            return "gauche"
        elif direction == "bas":
            return "droite"
        elif direction == "droite":
            return "bas"
        elif direction == "gauche":
            return "haut"
        
    return direction


d = {
  "code" : "RE-001",
  "type" : "réflexion",
  "map" : [
    [" ",  1, 2, 3, 4, ""],
    [15, "", "", "", "", 5],
    [14, "", "/", "", "/", 6],
    [13, "", "", "", "", 7],
    [12, "", "", "", "", 8],
    ["", 11, "L", 10, 9, ""]
  ]
}

print(reflexion(d))