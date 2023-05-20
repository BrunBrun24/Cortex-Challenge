from collections import Counter
import math
import heapq

def couleur2(defis):
    """
    Vérifie si les couleurs dans les défis sont valides en comparant avec des listes de couleurs en français et en anglais.
    :return: la clef du dictionnaire colors correspondant à la même couleur que sa clef, sinon False
    """
    # Création d'un dictionnaire inversé pour les couleurs en français
    dict = {"silver": "argent",
            "beige": "beige",
            "white": "blanc",
            "blue": "bleu",
            "coral": "corail",
            "indigo": "indigo",
            "yellow": "jaune",
            "lavender": "lavande",
            "magenta": "magenta",
            "brown": "marron",
            "mauve": "mauve",
            "black": "noir",
            "olive": "olive",
            "gold": "or",
            "orange": "orange",
            "orchid": "orchidée",
            "pink": "rose",
            "red": "rouge",
            "salmon": "saumon",
            "green": "vert"}

    for cle, valeur in defis["colors"].items():
        for c, v in dict.items():
            if cle == valeur:
                return cle
            elif (cle == c) and (valeur == v):
                return cle
            elif (cle == v) and (valeur == c):
                return cle
    return False

def reflexion2(defis):
    return deplacement_lumiere(defis, 5, 2, "haut")

def verifier_obstacle(defis, ligne, colonne, direction):
    """
    Vérifie si la case à la position (ligne, colonne) de la map contient un obstacle "/" ou "\\" et
    renvoie la nouvelle direction en fonction de l'obstacle.
    :param ligne: Entier représentant la ligne.
    :param colonne: Entier représentant la colonne.
    :param direction: String représentant la direction ("haut", "bas", "gauche", "droite").
    :return: String représentant la nouvelle direction.
    """
    obstacle = defis["map"][ligne][colonne]
    correspondances = {("/","haut"): "droite", ("/","bas"): "gauche", ("/","droite"): "haut", ("/","gauche"): "bas",
                    ("\\","haut"): "gauche", ("\\","bas"): "droite", ("\\","droite"): "bas", ("\\","gauche"): "haut"}
    return correspondances.get((obstacle, direction), direction)

def deplacement_lumiere(defis, ligne, colonne, direction):
    """
    Recherche la position de la lampe "L" dans la map et déplace la lumière en suivant les règles du jeu.
    :param ligne: Entier représentant la ligne de départ de la lumière.
    :param colonne: Entier représentant la colonne de départ de la lumière.
    :param direction: String représentant la direction initiale de la lumière ("haut", "bas", "gauche", "droite").
    :return: Entier représentant la valeur de la case atteinte par la lumière.
    """
    while True:
        # Vérifier si la case actuelle est un entier
        if isinstance(defis["map"][ligne][colonne], int):
            return defis["map"][ligne][colonne]
        else:
            # Appeler la fonction vérifier_obstacle pour obtenir la direction à suivre
            direction = verifier_obstacle(defis, ligne, colonne, direction)

            # Mettre à jour les coordonnées en fonction de la direction
            if direction == "bas":
                ligne += 1
            elif direction == "haut":
                ligne -= 1
            elif direction == "droite":
                colonne += 1
            elif direction == "gauche":
                colonne -= 1

def calcul2(defis):
    """
    Trouve les ensembles de nombres dans la liste 'numbers' qui s'additionnent pour obtenir le résultat 'result'.
    Returns:
        list: Une liste de listes contenant les ensembles de nombres qui s'additionnent pour obtenir le résultat cible.
    """
    result = defis["result"]
    numbers = defis["numbers"]
    res = []
    numbers.sort()  # Trie les nombres pour obtenir les combinaisons dans l'ordre croissant
    trouver_combinaisons_recursif(0, result, [], numbers, res)  # Appel initial de la fonction auxiliaire avec un total cible de 'result'
    
    output = []
    for solution in res:
        solution.sort()
        output.append('+'.join([str(x) for x in solution]))
    
    if len(output) > 0:
        return output[0]

def trouver_combinaisons_recursif(start, target, path, numbers, res):
    """
    Fonction auxiliaire pour effectuer un parcours récursif avec retour en arrière.
    
    Args:
        start (int): L'indice de départ pour le parcours.
        target (int): La somme cible à atteindre.
        path (list): La liste des nombres sélectionnés jusqu'à présent.
        numbers (list): La liste de nombres.
        res (list): La liste des résultats.
    """
    if target == 0:
        # Si la somme cible est atteinte, ajouter la liste de nombres dans les résultats
        res.append(path[:])
    elif target < 0:
        # Si la somme cible est dépassée, revenir en arrière
        return
    else:
        for i in range(start, len(numbers)):
            # Parcourir la liste de nombres à partir de l'indice 'start'
            if i > start and numbers[i] == numbers[i-1]:
                # Ignorer les doublons pour éviter de répéter les nombres dans la combinaison
                continue
            if numbers[i] not in path:
                # Ignorer les nombres qui sont déjà dans la combinaison
                path.append(numbers[i])
                trouver_combinaisons_recursif(i + 1, target - numbers[i], path, numbers, res)  # Appel récursif avec le nouveau total cible
                path.pop()  # Retour en arrière (trouver_combinaisons_recursif)

def frequence2(defis):
    """
    :return: Le mot le moins représenté (str)
    """
    word_count = Counter()
    for ligne in defis["words"]:
        word_count.update(ligne)
    
    return min(word_count, key=word_count.get)

def manquant2(defis):
    """
    Fonction permettant de trouver le premier nombre manquant dans une liste de nombres.
    :return: int: Le premier nombre manquant dans la liste de nombres.
    """
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

def labyrinthe2(donnees):
    labyrinth = donnees["map"]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Haut, Bas, Gauche, Droite
    start_pos = None
    goal_pos = [("1", (0, 0)), ("2", (0, len(labyrinth[0])-1)), ("3", (len(labyrinth)-1, len(labyrinth[0])-1)), ("4", (len(labyrinth)-1, 0))]  # Positions des sorties

    for i in range(len(labyrinth)):
        for j in range(len(labyrinth[i])):
            if labyrinth[i][j] == "D":
                start_pos = (i, j)

    queue = []
    visited = set()
    heapq.heappush(queue, (0, start_pos, []))  # File d'attente avec la priorité basée sur la distance

    while queue:
        _, current_pos, path = heapq.heappop(queue)

        if current_pos in [pos for _, pos in goal_pos]:
            goal = [key for key, value in goal_pos if value == current_pos][0]
            return int(goal)

        visited.add(current_pos)

        for direction in directions:
            new_pos = (current_pos[0] + direction[0], current_pos[1] + direction[1])

            if is_valid_position(new_pos, labyrinth) and new_pos not in visited:
                new_path = path + [current_pos]
                g_score = len(new_path)
                h_score = heuristic(new_pos, goal_pos)
                f_score = g_score + h_score
                heapq.heappush(queue, (f_score, new_pos, new_path))
                visited.add(new_pos)

    raise ValueError("Aucun chemin trouvé jusqu'à la sortie.")

def is_valid_position(position, labyrinth):
    x, y = position
    if 0 <= x < len(labyrinth) and 0 <= y < len(labyrinth[0]) and labyrinth[x][y] != "X":
        return True
    return False

def heuristic(position, goal_pos):
    x1, y1 = position
    min_distance = math.inf

    for _, (x2, y2) in goal_pos:
        distance = abs(x1 - x2) + abs(y1 - y2)
        min_distance = min(min_distance, distance)

    return min_distance

def doublon2(defis):
    """
    Recherche un mot en double dans la liste de mots fournie.
    :return: (str) Le mot en double s'il existe, sinon un message indiquant qu'il n'y a pas de mot en double.
    """
    word_count = {}
    for ligne in defis["words"]:
        for word in ligne:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    # Retourne le mot en double
    for cle, valeur in word_count.items():
        if valeur == 2:
            return cle
        
    return "Il n'y a pas de mot en double"

def raisonnement2(defis):
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