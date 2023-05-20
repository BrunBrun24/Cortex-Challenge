import random
from random import randint


# Créer un dictionnaire de couleurs aléatoires
def create_color_dict():
    size = randint(1,1000)
    dict = {}
    # Liste des couleurs disponibles
    colors = ["argent", "beige", "blanc", "bleu", "corail", "indigo", "jaune", "lavande", "magenta", "marron", "mauve", "noir", "olive", "or", "orange", "orchidée", "rose", "rouge", "saumon", "vert",
          "silver", "beige", "white", "blue", "coral", "indigo", "yellow", "lavender", "magenta", "brown", "mauve", "black", "olive", "gold", "orange", "orchid", "pink", "red", "salmon", "green"]
    color_dict = {}
    for i in range(size):
        color = random.choice(colors)
        color_dict[color] = random.choice(colors)
    dict["colors"] = color_dict
    return dict


# Créer une map pour le jeu réflection
def map_reflexion():
    dict = {}
    map_list = [
        ['', 1, 2, 3, 4, ''],
        [15, '', '', '', 5],
        [14, '', '', '', 6],
        [13, '', '', '', 7],
        [12, '', '', '', 8],
        ['', 11, "L", 10, 9, '']
    ]

    empty_coordinates = []  # Liste des coordonnées des cases vides

    for i in range(len(map_list)):
        for j in range(len(map_list[i])):
            if map_list[i][j] == '':
                empty_coordinates.append((i, j))

    random.shuffle(empty_coordinates)  # Mélanger les coordonnées des cases vides

    count = 0  # Compteur de modifications effectuées
    for coord in empty_coordinates:
        i, j = coord
        if (i, j) not in [(0, 0), (0, 5), (5, 0), (5, 5)]:
            map_list[i][j] = random.choice(['/', '\\'])
            count += 1
            if count == 4:  # Limiter à 4 modifications
                break

    dict["map"] = map_list
    return dict


# Créer une list de nombre (taille = 6)
def list_number():
    numbers = []
    for i in range(6):
        numbers.append(randint(1,50))

    result = randint(1,50)

    dict = {}
    dict["result"] = result
    dict["numbers"] = numbers
    return dict


# Créer une matrice contenant à l'interieur plusieurs list de words
def list_words():
    dict = {}
    size_matrice = randint(1,100)
    size_list = randint(1,100)
    words = ["cow", "dog", "cat", "chicken", "firefox", "rabbit"]
    m = []
    for i in range(size_matrice):
        l = []
        for word in range(size_list):
            l.append(random.choice(words))
        m.append(l)
    dict["words"] = m
    return dict


# Créer une matrice contenant à l'interieur un labyrinthe avec 4 sorties
def map_labyrinthe():
    dict = {}
    # On définie la taille de la map
    size_matrice = randint(4,50)
    size_list = randint(4,50)

    # On créer la map
    map = []

    # On initialise la map
    for i in range(size_matrice):
        l = []
        for word in range(size_list):
            l.append("")
        map.append(l)

    # On place le départ n'importe où sur la map
    ligne_depart = randint(0,size_matrice-1); colonne_depart = randint(0,size_list-1)
    while ((ligne_depart == 0) and (colonne_depart == 0)) or ((ligne_depart == 0) and (colonne_depart == size_list-1)) or ((ligne_depart == size_matrice-1) and (colonne_depart == size_list-1)) or ((ligne_depart == size_matrice-1) and (colonne_depart == 0)):
        ligne_depart = randint(0,size_matrice-1); colonne_depart = randint(0,size_list-1)

    # Placement des sorties
    map[0][0] = 1; map[0][size_list-1] = 2; map[size_matrice-1][size_list-1] = 3 ; map[size_matrice-1][0] = 4

    # On créer un chemin vers une sortie
    ligne = ligne_depart; colonne = colonne_depart
    position_de_depart = map[ligne][colonne]
    direction = ["N", "S", "E", "W"]
    solutions = []
    
    while position_de_depart == "":
        if ligne < size_matrice-1 and map[ligne+1][colonne] != "":
            break
        if ligne > 0 and map[ligne-1][colonne] != "":
            break
        if colonne < size_list-1 and map[ligne][colonne+1] != "":
            break
        if colonne > 0 and map[ligne][colonne-1] != "":
            break

        direction_suivante = random.choice(direction)
        if direction_suivante == "N" and ligne != 0:
            ligne -= 1
        elif direction_suivante == "S" and ligne != size_matrice-1:
            ligne += 1
        elif direction_suivante == "E" and colonne != size_list-1:
            colonne += 1
        elif direction_suivante == "W" and colonne != 0:
            colonne -= 1

        position_de_depart = map[ligne][colonne]
        if (ligne, colonne) not in solutions:
            solutions.append((ligne, colonne))

    # Si les coordonnées ne sont pas dans solutions alors on les remplaces par "X"
    for ligne in range(size_matrice):
        for colonne in range(size_list):
            if (ligne, colonne) not in solutions:
                map[ligne][colonne] = "X"

    # Pour l'affichage de la map on place le "D"
    map[ligne_depart][colonne_depart] = "D"

    # Placement des sorties
    map[0][0] = 1; map[0][size_list-1] = 2; map[size_matrice-1][size_list-1] = 3 ; map[size_matrice-1][0] = 4

    dict["map"] = map
    return dict


# Créer une list de nombre avec pour chaque nombre une couleur soit B soit R
def list_numbers_colors():
    dict = {}
    taille = randint(6, 500)
    couleurs = ['R', 'B']  # Rouge et Bleu
    liste = []
    nb_couleurs = 0

    for i in range(taille):
        # choisir le prochain nombre de cette couleur
        numero = nb_couleurs + 1

        # ajouter le nombre à la liste
        liste.append(f"{numero}")

        # mettre à jour le nombre de nombres de cette couleur
        nb_couleurs += 1

    # choisir une couleur aléatoire
    chiffre = random.choice(liste)

    while chiffre == liste[0]:
        chiffre = random.choice(liste)
    list_numbers_color = []  # Utilisation d'un ensemble pour stocker les nombres de couleur

    a = True

    # Permet de récupérer les nombres et de les mettre dans leur ensemble respectif
    for c in range(len(liste)):
        if liste[c] == chiffre:
            list_numbers_color[c-1] = f"{liste[c-1]}{couleurs[1]}"
            a = False
        elif liste[c] != chiffre and a:
            list_numbers_color.append(f"{liste[c]}{couleurs[0]}")
        elif liste[c] != chiffre and a == False:
            list_numbers_color.append(f"{liste[c]}{couleurs[1]}")
        
    random.shuffle(list_numbers_color)  # mélanger la liste modifie la liste originale

    dict["numbers"] = list_numbers_color
    return dict


# Créer une matrice contenant à l'interieur plusieurs list de mots avec un mot qui apparaît en double
def list_doublon():
    dict = {}
    size_matrice = randint(1,100)
    size_list = randint(1,100)
    words = ["cow", "dog", "cat", "chicken", "firefox", "rabbit"]
    doublon = random.choice(words)
    words.remove(doublon)
    m = []
    for i in range(size_matrice):
        l = []
        for word in range(size_list):
            l.append(random.choice(words))
        m.append(l)

    # On place le doublon
    for i in range(2):
        ligne = randint(0,size_matrice-1); colonne = randint(0, size_list-1)
        m[ligne][colonne] = doublon

    dict["words"] = m
    return dict


# Créer les 3 pièces
def pieces(size_drawing, size_list):
    all_pieces = {}
    name_pieces = ['A', 'B', 'C']
    verification = []
    for name in name_pieces:
        p = []
        ligne = randint(2, size_drawing//2); colonne = randint(2, size_list//2)
        for _ in range(ligne):
            a = []
            for _ in range(colonne):
                a.append('X')
            p.append(a)
            
        all_pieces[name] = p
        verification.append(p)
    
    # Si l'une des pièces est égale à une autre
    """while (verification[0] == verification[1]) or (verification[0] == verification[2]) or (verification[1] == verification[2]):
        all_pieces = pieces(size_drawing, size_list)"""

    return all_pieces


# Mets la pièce choisie dans la map
def placer_piece(map, piece):
    map_rows = len(map)
    map_cols = len(map[0])
    piece_rows = len(piece)
    piece_cols = len(piece[0])

    # Générer des coordonnées aléatoires pour l'emplacement de la pièce
    max_row = map_rows - piece_rows
    max_col = map_cols - piece_cols
    row = random.randint(0, max_row)
    col = random.randint(0, max_col)

    # Placer la pièce dans la map en remplaçant les "X" par des espaces vides
    for r in range(piece_rows):
        for c in range(piece_cols):
            if piece[r][c] == "X":
                map[row + r][col + c] = ""

    return map


# Créer le dessin pour "raisonnement"
def dessins():
    dict = {}
    size_drawing = randint(7, 100)
    size_list = randint(7, 100)
    drawing = [[] for _ in range(size_drawing)]
    for d in range(size_drawing):
        for _ in range(size_list):
            drawing[d].append('X')

    diff_pieces = pieces(size_drawing, size_list)

    name_pieces = ['A', 'B', 'C']
    piece_choice = random.choice(name_pieces)
    
    for name, map in diff_pieces.items():
        if name == piece_choice:
            placer_piece(drawing, map)
            break

    dict["drawing"] = drawing
    dict["pieces"] = diff_pieces
    return dict