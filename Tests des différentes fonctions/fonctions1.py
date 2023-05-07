def couleur(donnees):
    """
    Vérifie si les couleurs dans les défis sont valides en comparant avec des listes de couleurs en français et en anglais.
    :return: la clef du dictionnaire colors correspondant à la même couleur que sa clef, sinon False
    """
    couleur_fr = ("argent", "beige", "blanc", "bleu", "corail", "indigo", "jaune", "lavande", "magenta", "marron", "mauve", "noir", "olive", "or", "orange", "orchidée", "rose", "rouge", "saumon", "vert")
    couleur_en = ("silver", "beige", "white", "blue", "coral", "indigo", "yellow", "lavender", "magenta", "brown", "mauve", "black", "olive", "gold", "orange", "orchid", "pink", "red", "salmon", "green")
    
    # On parcourt la liste des couleurs
    for cle,valeur in donnees["colors"].items():
        if cle == valeur:
            return cle
        elif cle in couleur_fr:
            # On sauvegarde la position de "cle" ce trouvant dans "couleur_fr"
            position_couleur = couleur_fr.index(cle)
            # On regarde si la valeur ce trouve à la même position que la "cle" dans "couleur_en"
            if (valeur in couleur_en) and (valeur == couleur_en[position_couleur]):
                return cle
        else:
            position_couleur = couleur_en.index(cle)
            if (valeur in couleur_fr) and (valeur == couleur_fr[position_couleur]):
                return cle
    
    return False

def reflexion(donnees):
    """
    Cherche où se trouve la lampe dans la map
    :return: la fonction "parcours_lampe_torche"
    """
    direction_lampe_torche = None
    ligne_lampe = None
    colonne_lampe = None

    # On récupère la direction de la lampe torche et ses coordonnées
    for i, ligne in enumerate(donnees["map"]):
        # Si la lampe se trouve sur la première ligne
        if "L" in ligne and i == 0:
            direction_lampe_torche = "bas"
            ligne_lampe = i
            colonne_lampe = ligne.index("L")
        # Si la lampe se trouve sur la dernière ligne
        elif "L" in ligne and i == len(donnees["map"])-1:
            direction_lampe_torche = "haut"
            ligne_lampe = i
            colonne_lampe = ligne.index("L")
        # Si la lampe se trouve sur la gauche
        elif ligne[0] == "L":
            direction_lampe_torche = "droite"
            ligne_lampe = i
            colonne_lampe = 0
        # Si la lampe se trouve sur la droite
        elif ligne[-1] == "L":
            direction_lampe_torche = "gauche"
            ligne_lampe = i
            colonne_lampe = len(ligne)-1

    return parcours_lampe_torche(donnees, direction_lampe_torche, ligne_lampe, colonne_lampe)

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
        return donnees["map"][ligne][colonne]

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

def calcul(donnees):
    """
    Fonction qui trouve toutes les combinaisons de nombres dans la liste qui, additionnées ensemble, donnent le nombre cible.

    Args:
        nombre_cible (int): Le nombre cible à atteindre.
        nombres (list): Une liste de nombres.

    Returns:
        list: Une liste de toutes les combinaisons trouvées. Si aucune combinaison n'est trouvée, retourne une liste vide.
    """
    nombre_cible = donnees["result"]
    nombres = donnees["numbers"]
    combinaisons = []
    trouver_combinaisons_recursif(donnees, nombre_cible, nombres, 0, [], combinaisons)

    # Convertir les listes de nombres en chaînes de caractères avec des "+" comme séparateurs
    combinaisons = ['+'.join(map(str, combinaison)) for combinaison in combinaisons]

    return combinaisons

def trouver_combinaisons_recursif(donnees, nombre_cible, nombres, index, combinaison_actuelle, combinaisons):
    """
    Fonction récursive qui trouve toutes les combinaisons de nombres dans la liste qui, additionnés ensemble, donnent le nombre cible.

    Args:
        nombre_cible (int): Le nombre cible à atteindre.
        nombres (list): Une liste de nombres.
        index (int): L'index actuel pour parcourir la liste de nombres.
        combinaison_actuelle (list): La combinaison actuelle en cours de construction.
        combinaisons (list): La liste de toutes les combinaisons trouvées jusqu'à présent.

    Returns:
        None
    """
    # Cas de base : si le nombre cible est atteint, ajouter la combinaison actuelle à la liste de combinaisons
    if nombre_cible == 0:
        combinaisons.append(list(combinaison_actuelle))
        return
    # Cas de base : si on a parcouru tous les nombres, retourner
    elif index == len(nombres):
        return

    # Ne pas inclure le nombre actuel dans la combinaison
    trouver_combinaisons_recursif(donnees, nombre_cible, nombres, index + 1, combinaison_actuelle, combinaisons)

    # Inclure le nombre actuel dans la combinaison
    if nombre_cible >= nombres[index]:
        # Ajouter le nombre actuel à la combinaison
        combinaison_actuelle.append(nombres[index])
        trouver_combinaisons_recursif(donnees, nombre_cible - nombres[index], nombres, index + 1, combinaison_actuelle, combinaisons)
        # Retirer le nombre actuel de la combinaison pour explorer d'autres possibilités
        combinaison_actuelle.pop()

def frequence(donnees):
    """
    :return: Le mot le moins représenté (str)
    """
    occurence_words = {}  # Dictionnaire pour stocker les occurrences de chaque mot
    for ligne in donnees["words"]:
        for word in ligne:
            if word not in occurence_words:
                occurence_words[word] = 0  # Initialiser l'occurrence du mot à 0 s'il n'est pas déjà présent
            occurence_words[word] += 1  # Incrémenter l'occurrence du mot

    word = None  # Variable pour stocker le mot le moins représenté
    little_occurence = float('inf')  # Variable pour stocker le nombre d'occurrences du mot le moins représenté, initialisée à une valeur positive infinie
    for cle, valeur in occurence_words.items():
        if valeur < little_occurence:  # Si le nombre d'occurrences du mot actuel est inférieur au nombre d'occurrences du mot le moins représenté actuel
            word = cle  # Mettre à jour le mot le moins représenté
            little_occurence = valeur  # Mettre à jour le nombre d'occurrences du mot le moins représenté

    return word  # Retourner le mot le moins représenté

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

def labyrinthe(donnees):
    """
    Cherche les coordonnées de la case départ
    :return: la fonction "parcours_labyrinthe"
    """
    ligne_start = None
    colonne_start = None
    position = 0
    # On récupère la ligne de la position de départ 
    for ligne in donnees["map"]:
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

    return parcours_labyrinthe(donnees, ligne_start, colonne_start, derniere_direction = "")

def parcours_labyrinthe(donnees, ligne, colonne, derniere_direction):
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
    case = donnees["map"][ligne][colonne]

    if case == "1":
        return 1
    elif case == "2":
        return 2
    elif case == "3":
        return 3
    elif case == "4":
        return 4

    max_ligne = len(donnees["map"])  # Nombre de lignes
    max_colonne = len(donnees["map"][0])  # Nombre de colonnes (en supposant que toutes les lignes ont la même longueur)
    arrivees = ["1", "2", "3", "4"]
    # Si la ligne se trouve sur la map et que les coordonnées (avec ligne+1) sont dans "arrivees"
    if (ligne < max_ligne-1) and (donnees["map"][ligne+1][colonne] == "" or donnees["map"][ligne+1][colonne] in arrivees) and ((derniere_direction != "bas") or (derniere_direction == "")):
        derniere_direction = "haut"
        return parcours_labyrinthe(donnees, (ligne+1), colonne, derniere_direction)
    # Si la ligne se trouve sur la map et que les coordonnées (avec ligne-1) sont dans "arrivees"
    elif (ligne > 0) and (donnees["map"][ligne-1][colonne] == "" or donnees["map"][ligne-1][colonne] in arrivees) and ((derniere_direction != "haut") or (derniere_direction == "")):
        derniere_direction = "bas"
        return parcours_labyrinthe(donnees, (ligne-1), colonne, derniere_direction)
    # Si la colonne se trouve sur la map et que les coordonnées (avec colonne+1) sont dans "arrivees"
    elif (colonne < max_colonne-1) and (donnees["map"][ligne][colonne+1] == "" or donnees["map"][ligne][colonne+1] in arrivees) and ((derniere_direction != "droite") or (derniere_direction == "")):
        derniere_direction = "gauche"
        return parcours_labyrinthe(donnees, ligne, (colonne+1), derniere_direction)
    # Si la colonne se trouve sur la map et que les coordonnées (avec colonne-1) sont dans "arrivees"
    elif (colonne > 0) and (donnees["map"][ligne][colonne-1] == "" or donnees["map"][ligne][colonne-1] in arrivees) and ((derniere_direction != "gauche") or (derniere_direction == "")):
        derniere_direction = "droite"
        return parcours_labyrinthe(donnees, ligne, (colonne-1), derniere_direction)

def doublon(donnees):
    """
    Recherche un mot en double dans la liste de mots fournie.
    :return: (str) Le mot en double s'il existe, sinon un message indiquant qu'il n'y a pas de mot en double.
    """
    all_words = []
    list_words = []
    dict_words = {}
    # Met tous les mots dans une seul liste
    for ligne in donnees["words"]:
        for word in ligne:
            all_words.append(word)
    # Initialiser la liste pour stocker les différents mots (sans les répéter)
    for word in all_words:
        if word not in list_words:
            list_words.append(word)
    # Initialiser le dictionnaire pour stocker les occurrences de mots et les initialise à 0
    for word in list_words:
        dict_words[word] = 0
    # Ajoute +1 à chaque fois un mot est dans le "dict_words"
    for word in all_words:
        if word in dict_words:
            dict_words[word] += 1
    # Retourne le mot en double
    for cle, valeur in dict_words.items():
        if valeur == 2:
            return cle
        
    return "Il n'y a pas de mot en double"

def raisonnement(donnees):
    """
    Applique un raisonnement sur le dessin en utilisant différentes méthodes pour vérifier s'il y a une solution possible.
    :return: Le nom de la solution trouvée, sinon (str) "Aucune de ces solutions n'est la bonne".
    """
    drawing = donnees["drawing"]
    # On regarde si il y a possibilité d'enlever des colonnes à droite du dessin
    decalage = decalage_raisonnement(drawing)

    # On décale chaque ligne du dessin par "decalage"
    new_drawing = []
    for ligne in drawing:
        if "" in ligne:
            new_drawing.append(ligne[decalage:])

    # On regarde si il y a possibilité d'enlever des colonnes à gauche du dessin mais pour cela on va inverser chaque ligne du dessin
    new_drawing = retourne_raisonnement(new_drawing)
    # On regarde si il y a possibilité d'enlever des colonnes à droite du dessin
    decalage_new_drawing = decalage_raisonnement(new_drawing)

    # On décale chaque ligne du dessin par "decalage_new_drawing"
    finish_drawing = []
    for ligne in new_drawing:
        if "" in ligne:
            finish_drawing.append(ligne[decalage_new_drawing:])

    # On remet le dessin à l'endroit
    finish_drawing = retourne_raisonnement(finish_drawing)
    # On inverse le vide ("") avec les murs ("X")
    finish_drawing = inversion_raisonnement(finish_drawing)
    # On regarde si une solution est possible
    for nom, map in donnees["pieces"].items():
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

