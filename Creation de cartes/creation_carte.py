import random
from random import randint


# Créer un dictionnaire de couleurs aléatoires
def create_color_dict():
    size = randint(1,250)
    # Liste des couleurs disponibles
    colors = ["argent", "beige", "blanc", "bleu", "corail", "indigo", "jaune", "lavande", "magenta", "marron", "mauve", "noir", "olive", "or", "orange", "orchidée", "rose", "rouge", "saumon", "vert",
          "silver", "beige", "white", "blue", "coral", "indigo", "yellow", "lavender", "magenta", "brown", "mauve", "black", "olive", "gold", "orange", "orchid", "pink", "red", "salmon", "green"]
    color_dict = {}
    for i in range(size):
        color = random.choice(colors)
        color_dict[color] = random.choice(colors)
    return color_dict

# Créer une map pour le jeu réflection
def map_reflection():
    size = randint(1,250)
    map_list = []
    # Première ligne
    first_row = [" "] + list(range(1, size+1)) + [""]
    map_list.append(first_row)
    # Lignes du milieu
    for i in range(1, size+1):
        row = [size*4-i+1] + [""]*(size-1) + [size+i]
        for j in range(1, size//2+1):
            if i == j or i == size-j+1:
                row[j] = "/"
                row[size-j] = "/"
        map_list.append(row)

    # Dernière ligne
    last_row = []
    n = size*3+1
    for j in range(size):
        n -= 1
        last_row.append(n)
    last_row = [""] + last_row + [""]
    map_list.append(last_row)

    # Placement de la lampe (L)
    list_number = [i for i in range(1, size*4+1)]
    numero_a_change = random.choice(list_number)
    for ligne in map_list:
        if numero_a_change in ligne:
            for numero in ligne:
                for i, numero in enumerate(ligne):
                    if numero == numero_a_change:
                        ligne[i] = "L"

    return map_list

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
    size_matrice = randint(1,1000)
    size_list = randint(1,1000)
    words = ["cow", "dog", "cat", "chicken", "firefox", "rabbit"]
    m = []
    for i in range(size_matrice):
        l = []
        for word in range(size_list):
            l.append(random.choice(words))
        m.append(l)

    return m


# Créer une matrice contenant à l'interieur un labyrinthe avec 4 sorties
def map_labyrinthe():
    # On définie la taille de la map
    size_matrice = randint(4,100)
    size_list = randint(4,100)

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

    return map



l = map_labyrinthe()
for ligne in l:
    print(ligne)