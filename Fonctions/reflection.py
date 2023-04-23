<<<<<<< HEAD
def reflection(donnee):
    """
    Recherche la position de la lampe "L" dans la map.
    :param map: Liste de listes représentant la map.
    :return: Tuple (ligne, colonne) représentant la position de la lampe, sinon False.
    """
    ligne_lampe = None
    colonne_lampe = None
    for i, ligne in enumerate(donnee["map"]):
        if "L" in ligne:
            ligne_lampe = i
            colonne_lampe = ligne.index("L")
            if i == 0:
                direction_lampe = "bas"
            elif i == len(donnee["map"])-1:
                direction_lampe = "haut"
            elif colonne_lampe == 0:
                direction_lampe = "droite"
            elif colonne_lampe == len(ligne)-1:
                direction_lampe = "gauche"
            
            return deplacement_lumiere(donnee, ligne_lampe, colonne_lampe, direction_lampe)
    return False
        
def verifier_obstacle(donnee, ligne, colonne, direction):
    """
    Vérifie si la case à la position (ligne, colonne) de la map contient un obstacle "/" ou "\\" et
    renvoie la nouvelle direction en fonction de l'obstacle.
    :param ligne: Entier représentant la ligne.
    :param colonne: Entier représentant la colonne.
    :param direction: String représentant la direction ("haut", "bas", "gauche", "droite").
    :return: String représentant la nouvelle direction.
    """
    obstacle = donnee["map"][ligne][colonne]
    correspondances = {("/","haut"): "droite", ("/","bas"): "gauche", ("/","droite"): "haut", ("/","gauche"): "bas",
                    ("\\","haut"): "gauche", ("\\","bas"): "droite", ("\\","droite"): "bas", ("\\","gauche"): "haut"}
    return correspondances.get((obstacle, direction), direction)

def deplacement_lumiere(donnee, ligne, colonne, direction):
    """
    Recherche la position de la lampe "L" dans la map et déplace la lumière en suivant les règles du jeu.
    :param ligne: Entier représentant la ligne de départ de la lumière.
    :param colonne: Entier représentant la colonne de départ de la lumière.
    :param direction: String représentant la direction initiale de la lumière ("haut", "bas", "gauche", "droite").
    :return: Entier représentant la valeur de la case atteinte par la lumière.
    """
    while True:
        # Vérifier si la case actuelle est un entier
        if isinstance(donnee["map"][ligne][colonne], int):
            return donnee["map"][ligne][colonne]
        else:
            # Appeler la fonction vérifier_obstacle pour obtenir la direction à suivre
            direction = verifier_obstacle(donnee,ligne, colonne, direction)

            # Mettre à jour les coordonnées en fonction de la direction
            if direction == "bas":
                ligne += 1
            elif direction == "haut":
                ligne -= 1
            elif direction == "droite":
                colonne += 1
            elif direction == "gauche":
                colonne -= 1


donnees = {"code": "RE-001", "type": "reflexion", "map": [[" ", 1, 2, 3, 4, ""], [15, "", "", "", "", 5], [14, "", "/", "", "/", 6], [13, "", "", "", "", 7], [12, "", "", "", "", 8], ["", 11, "L", 10, 9, ""]]}

output = reflection(donnees)
print(output)
=======
def reflection(donnee):
    """
    Recherche la position de la lampe "L" dans la map.
    :param map: Liste de listes représentant la map.
    :return: Tuple (ligne, colonne) représentant la position de la lampe, sinon False.
    """
    ligne_lampe = None
    colonne_lampe = None
    for i, ligne in enumerate(donnee["map"]):
        if "L" in ligne:
            ligne_lampe = i
            colonne_lampe = ligne.index("L")
            if i == 0:
                direction_lampe = "bas"
            elif i == len(donnee["map"])-1:
                direction_lampe = "haut"
            elif colonne_lampe == 0:
                direction_lampe = "droite"
            elif colonne_lampe == len(ligne)-1:
                direction_lampe = "gauche"
            
            return deplacement_lumiere(donnee, ligne_lampe, colonne_lampe, direction_lampe)
    return False
        
def verifier_obstacle(donnee, ligne, colonne, direction):
    """
    Vérifie si la case à la position (ligne, colonne) de la map contient un obstacle "/" ou "\\" et
    renvoie la nouvelle direction en fonction de l'obstacle.
    :param ligne: Entier représentant la ligne.
    :param colonne: Entier représentant la colonne.
    :param direction: String représentant la direction ("haut", "bas", "gauche", "droite").
    :return: String représentant la nouvelle direction.
    """
    obstacle = donnee["map"][ligne][colonne]
    correspondances = {("/","haut"): "droite", ("/","bas"): "gauche", ("/","droite"): "haut", ("/","gauche"): "bas",
                    ("\\","haut"): "gauche", ("\\","bas"): "droite", ("\\","droite"): "bas", ("\\","gauche"): "haut"}
    return correspondances.get((obstacle, direction), direction)

def deplacement_lumiere(donnee, ligne, colonne, direction):
    """
    Recherche la position de la lampe "L" dans la map et déplace la lumière en suivant les règles du jeu.
    :param ligne: Entier représentant la ligne de départ de la lumière.
    :param colonne: Entier représentant la colonne de départ de la lumière.
    :param direction: String représentant la direction initiale de la lumière ("haut", "bas", "gauche", "droite").
    :return: Entier représentant la valeur de la case atteinte par la lumière.
    """
    while True:
        # Vérifier si la case actuelle est un entier
        if isinstance(donnee["map"][ligne][colonne], int):
            return donnee["map"][ligne][colonne]
        else:
            # Appeler la fonction vérifier_obstacle pour obtenir la direction à suivre
            direction = verifier_obstacle(donnee,ligne, colonne, direction)

            # Mettre à jour les coordonnées en fonction de la direction
            if direction == "bas":
                ligne += 1
            elif direction == "haut":
                ligne -= 1
            elif direction == "droite":
                colonne += 1
            elif direction == "gauche":
                colonne -= 1


donnees = {"code": "RE-001", "type": "reflexion", "map": [[" ", 1, 2, 3, 4, ""], [15, "", "", "", "", 5], [14, "", "/", "", "/", 6], [13, "", "", "", "", 7], [12, "", "", "", "", 8], ["", 11, "L", 10, 9, ""]]}

output = reflection(donnees)
print(output)
>>>>>>> 6e34e0d79324732dd1b147a0914c1d5e98739c19
