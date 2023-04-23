def labyrinthe(donnee):
    """
    Cherche les coordonnées de la case départ
    :return: la fonction "parcours_labyrinthe"
    """
    ligne_start = None
    colonne_start = None
    position = 0
    # On récupère la ligne de la position de départ 
    for ligne in donnee["map"]:
        if "D" in ligne:
            ligne_start = position
            position = 0
            # On récupère la colonne de la position de départ 
            for colonne in ligne:
                if colonne == "D":
                    colonne_start = position
                else:
                    position += 1
            break
        else:
            position += 1

    return parcours_labyrinthe(donnee, ligne_start, colonne_start, derniere_direction = "")

def parcours_labyrinthe(donnee, ligne, colonne, derniere_direction):
    """
    Fonction permettant de parcourir un labyrinthe.

    Args:
        ligne (int): Numéro de la ligne actuelle.
        colonne (int): Numéro de la colonne actuelle.
        derniere_direction (str): Dernière direction prise ("haut", "bas", "gauche", "droite").

    Returns:
        int: 1 si la case est marquée comme "1"
        int: 2 si la case est marquée comme "2"
        int: 3 si la case est marquée comme "3"
        int: 4 si la case est marquée comme "4"
    """
    case = donnee["map"][ligne][colonne]

    if case == "1":
        return 1
    elif case == "2":
        return 2
    elif case == "3":
        return 3
    elif case == "4":
        return 4

    max_ligne = len(donnee["map"])  # Nombre de lignes
    max_colonne = len(donnee["map"][0])  # Nombre de colonnes (en supposant que toutes les lignes ont la même longueur)
    arrivees = ["1", "2", "3", "4"]
    # Si la ligne se trouve sur la map et que les coordonnées (avec ligne+1) sont dans "arrivees"
    if (ligne < max_ligne-1) and (donnee["map"][ligne+1][colonne] == "" or donnee["map"][ligne+1][colonne] in arrivees) and ((derniere_direction != "bas") or (derniere_direction == "")):
        derniere_direction = "haut"
        return parcours_labyrinthe(donnee, (ligne+1), colonne, derniere_direction)
    # Si la ligne se trouve sur la map et que les coordonnées (avec ligne-1) sont dans "arrivees"
    elif (ligne > 0) and (donnee["map"][ligne-1][colonne] == "" or donnee["map"][ligne-1][colonne] in arrivees)and ((derniere_direction != "haut") or (derniere_direction == "")):
        derniere_direction = "bas"
        return parcours_labyrinthe(donnee, (ligne-1), colonne, derniere_direction)
    # Si la colonne se trouve sur la map et que les coordonnées (avec colonne+1) sont dans "arrivees"
    elif (colonne < max_colonne-1) and (donnee["map"][ligne][colonne+1] == "" or donnee["map"][ligne][colonne+1] in arrivees) and ((derniere_direction != "droite") or (derniere_direction == "")):
        derniere_direction = "gauche"
        return parcours_labyrinthe(donnee, ligne, (colonne+1), derniere_direction)
    # Si la colonne se trouve sur la map et que les coordonnées (avec colonne-1) sont dans "arrivees"
    elif (colonne > 0) and (donnee["map"][ligne][colonne-1] == "" or donnee["map"][ligne][colonne-1] in arrivees) and ((derniere_direction != "gauche") or (derniere_direction == "")):
        derniere_direction = "droite"
        return parcours_labyrinthe(donnee, ligne, (colonne-1), derniere_direction)
    

donnees = {"code": "LA-001", "type": "labyrinthe", "map": [["1", "X", "X", "X", "X", "X", "X", "", "", "2"], ["", "", "", "", "", "", "X", "", "X", ""], ["X", "X", "X", "X", "X", "", "X", "", "X", ""], ["X", "X", "X", "X", "X", "D", "X", "X", "X", ""], ["X", "X", "X", "", "", "X", "X", "", "", ""], ["X", "X", "X", "", "X", "X", "X", "", "X", "X"], ["4", "", "", "", "X", "X", "X", "", "", "3"]]}

output = labyrinthe(donnees)
print(output)
