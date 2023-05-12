def raisonnement(defis):
    """
    Applique un raisonnement sur le dessin en utilisant différentes méthodes pour vérifier s'il y a une solution possible.
    :return: Le nom de la solution trouvée, sinon (str) "Aucune de ces solutions n'est la bonne".
    """
    drawing = defis["drawing"]
    pieces = defis["pieces"]

    # On regarde si il y a possibilité d'enlever des colonnes à droite du dessin
    decalage = decalage_raisonnement(drawing)

    # On décale chaque ligne du dessin par "decalage"
    new_drawing = [ligne[decalage:] for ligne in drawing if "" in ligne]

    # On regarde si il y a possibilité d'enlever des colonnes à gauche du dessin mais pour cela on va inverser chaque ligne du dessin
    new_drawing = retourne_raisonnement(new_drawing)
    # On regarde si il y a possibilité d'enlever des colonnes à droite du dessin
    decalage_new_drawing = decalage_raisonnement(new_drawing)

    # On décale chaque ligne du dessin par "decalage_new_drawing"
    finish_drawing = [ligne[decalage_new_drawing:] for ligne in new_drawing if "" in ligne]

    # On remet le dessin à l'endroit
    finish_drawing = retourne_raisonnement(finish_drawing)
    # On inverse le vide ("") avec les murs ("X")
    finish_drawing = inversion_raisonnement(finish_drawing)
    # On regarde si une solution est possible
    for nom, map in pieces.items():
        if finish_drawing == map:
            return nom

    return "Aucune de ces solutions n'est la bonne"

def decalage_raisonnement(drawing):
    """
    Recherche le décalage possible le plus à gauche du dessin en vérifiant chaque ligne.
    :param drawing: (list) Le dessin représenté sous forme de liste de listes.
    :return: (int) Le décalage possible le plus à gauche du dessin.
    """
    possibilite_decalage = []
    arrete_for = False
    # On parcourt chaque ligne de "drawing"
    for ligne in drawing:
        decalage = 0
        compteur = 0 # Pour savoir si on est au début de la ligne
        # On parcourt chaque symbole surla ligne
        for symbole in ligne:
            # Si le symbole est un trou et qu'il se trouve au début de la ligne
            if (symbole == "") and (compteur == 0):
                decalage = 0
                return decalage
            elif symbole == "X":
                decalage += 1
            # Sinon on arrête les boucles "for"
            else:
                possibilite_decalage.append(decalage)
                break
            
            compteur += 1

        if arrete_for:
            break

    return min(possibilite_decalage)

def retourne_raisonnement(drawing):
    """
    Retourne horizontalement chaque ligne du dessin.
    :param drawing: (list) Le dessin représenté sous forme de liste de listes.
    :return: (list) Le dessin modifié avec chaque ligne retournée horizontalement.
    """
    new_drawing = []
    for ligne in drawing:
        new_drawing.append(ligne[::-1])

    return new_drawing

def inversion_raisonnement(drawing):
    """
    Inverse les cases vides ("") avec les cases pleines ("X") dans le dessin.
    :param drawing: (list) Le dessin représenté sous forme de liste de listes.
    :return: (list) Le dessin modifié avec les cases inversées.
    """
    for ligne in range(len(drawing)):
        for colonne in range(len(drawing[ligne])):
            if drawing[ligne][colonne] == "":
                drawing[ligne][colonne] = "X"
            else:
                drawing[ligne][colonne] = ""
    return drawing