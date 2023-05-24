from itertools import combinations
from collections import Counter
import math
import heapq



def couleur(donnees: dict) -> str or None:
    """
    Vérifie si les couleurs dans les défis sont valides en comparant avec des listes de couleurs en français et en anglais.
    Args:donnees (dict): Un dictionnaire contenant couleurs -> "colors".
    :return: la clef du dictionnaire colors correspondant à la même couleur que sa clef, sinon None.
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


def reflexion(donnees: dict) -> int:
    """
    Parcours la map en cherchant où va la lumière de la lampe
    Args:donnees (dict): Un dictionnaire contenant la map.
    :return: un entier
    """
    return parcours_lampe_torche(donnees, "haut", 5, 2)

def parcours_lampe_torche(donnees: dict, direction: str, ligne: str, colonne: str) -> int:
    """
    Parcours la map en suivant le faisceau lumineux
    :param:
        donnees : "dict"
        direction : "string"
        ligne : "int"
        colonne : "int"
    :return: un entier (int)
    """
    if type(donnees["map"][ligne][colonne]) == int:
        return int(donnees["map"][ligne][colonne])

    direction = si_miroir(donnees, direction, ligne, colonne)

    if direction == "bas":
        return parcours_lampe_torche(donnees, direction, ligne+1, colonne)
    elif direction == "haut":
        return parcours_lampe_torche(donnees, direction, ligne-1, colonne)
    elif direction == "droite":
        return parcours_lampe_torche(donnees, direction, ligne, colonne+1)
    else:
        return parcours_lampe_torche(donnees, direction, ligne, colonne-1)

def si_miroir(donnees: dict, direction: str, ligne: str, colonne: str):
    """
    Indique si sur les coordonnées pris en paramètres, il y a un miroir
    :param:
        donnees : "dict"
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


def calcul(donnees: dict) -> str or None:
    """
    Fonction qui recherche une combinaison de nombres dans la liste 'numbers' dont la somme est égale à 'result'.
    Args:donnees (dict): Un dictionnaire contenant les clés 'result' et 'numbers'.
    Returns: str or None: Une chaîne de caractères représentant la combinaison trouvée, si une combinaison satisfaisant la condition est trouvée. Sinon, renvoie None.
    """
    result = donnees["result"]
    numbers = donnees["numbers"]
    for i in range(1, len(numbers) + 1):
        for combo in combinations(numbers, i):
            if sum(combo) == result:
                combo_str = "+".join(str(num) for num in combo)
                return combo_str
            
    return None 


def frequence(donnees: dict) -> str:
    """
    :param:
        donnees : "dict"
    :return: Le mot le moins représenté (str)
    """
    word_count = Counter()
    for ligne in donnees["words"]:
        word_count.update(ligne)
    
    return min(word_count, key=word_count.get)


def manquant(donnees: dict) -> int or None:
    """
    Fonction permettant de trouver le premier nombre manquant dans une liste de nombres.
    :param:
        donnees : "dict"
    :return: int: Le premier nombre manquant dans la liste de nombres.
    """
    list_numbers_color1 = []  # Utilisation d'un ensemble pour stocker les nombres de couleur 1
    list_numbers_color2 = []  # Utilisation d'un ensemble pour stocker les nombres de couleur 2

    # Permet de récupérer une couleur disponible et de les mettre dans "list_color"
    couleur = donnees["numbers"][0][-1]

    # Permet de récupérer les nombres et de les mettre dans leur ensemble respectif
    for color in donnees["numbers"]:
        if color[-1] == couleur:
            list_numbers_color1.append(int(color[:-1]))
        else:
            list_numbers_color2.append(int(color[:-1]))

    list_numbers_color1 = sorted(list_numbers_color1, key=int)
    list_numbers_color2 = sorted(list_numbers_color2, key=int)

    # Trouver le premier nombre manquant dans list_numbers_color1
    for number in range(len(list_numbers_color1)-1):
        if list_numbers_color1[number+1] != list_numbers_color1[number]+1:
            return int(list_numbers_color1[number]+1)

    # Trouver le premier nombre manquant dans list_numbers_color2
    for number in range(len(list_numbers_color2)-1):
        if list_numbers_color2[number+1] != list_numbers_color2[number]+1:
            return int(list_numbers_color2[number]+1)

    return None


def labyrinthe(donnees: dict) -> int or None:
    """
    Cherche la sortie du labyrinthe
    :param:
        donnees : "dict"
    :return: un entier étant l'arrivée    
    """
    labyrinth = donnees["map"]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Haut, Bas, Gauche, Droite
    start_pos:None = None
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

    return None

def is_valid_position(position: tuple, labyrinth: list) -> True or False:
    """
    Vérifie si une position donnée est valide dans le labyrinthe.

    Paramètres :
        - position : Un tuple représentant la position à vérifier, avec les coordonnées (x, y).
        - labyrinth : Une liste de listes représentant le labyrinthe.

    Retour :
        - True si la position est valide et ne correspond pas à un mur ('X') dans le labyrinthe.
        - False sinon.
    """
    x, y = position
    if 0 <= x < len(labyrinth) and 0 <= y < len(labyrinth[0]) and labyrinth[x][y] != "X":
        return True
    return False

def heuristic(position, goal_pos) -> int:
    """
    Calcule l'heuristique (estimation) de distance entre une position donnée et une ou plusieurs positions buts.

    Paramètres :
        - position : Un tuple représentant la position de départ, avec les coordonnées (x, y).
        - goal_pos : Une liste de tuples représentant les positions buts, avec les coordonnées (x, y).

    Retour :
        - Un entier représentant la distance heuristique minimale entre la position de départ et une position but.
    """
    x1, y1 = position
    min_distance = math.inf

    for _, (x2, y2) in goal_pos:
        distance = abs(x1 - x2) + abs(y1 - y2)
        min_distance = min(min_distance, distance)

    return min_distance


def doublon(donnees: dict) -> str or None:
    """
    Recherche un mot en double dans la liste de mots fournie.
    :param:
        donnees : "dict"
    :return: (str) Le mot en double s'il existe, sinon None.
    """
    word_count = {}
    for ligne in donnees["words"]:
        for word in ligne:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    # Retourne le mot en double
    for cle, valeur in word_count.items():
        if valeur == 2:
            return str(cle)
        
    return None


def raisonnement(donnees: dict) -> str or None:
    """
    Applique un raisonnement sur le dessin en utilisant différentes méthodes pour vérifier s'il y a une solution possible.
    :param:
        donnees : "dict"
    :return: Le nom de la solution trouvée, sinon None.
    """
    drawing = donnees["drawing"]
    pieces = donnees["pieces"]

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
            return str(nom)

    return None

def decalage_raisonnement(drawing: list) -> int:
    """
    Recherche le décalage possible le plus à gauche du dessin en vérifiant chaque ligne.
    :param drawing: (list) Le dessin représenté sous forme de liste de listes.
    :return: (int) Le décalage possible le plus à gauche du dessin.
    """
    possibilite_decalage = []
    arrete_for:bool = False
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

def retourne_raisonnement(drawing: list) -> list:
    """
    Retourne horizontalement chaque ligne du dessin.
    :param drawing: (list) Le dessin représenté sous forme de liste de listes.
    :return: (list) Le dessin modifié avec chaque ligne retournée horizontalement.
    """
    new_drawing = []
    for ligne in drawing:
        new_drawing.append(ligne[::-1])
    return new_drawing

def inversion_raisonnement(drawing: list) -> list:
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
