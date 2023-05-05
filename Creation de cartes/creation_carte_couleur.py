import random


# Crée un dictionnaire de couleurs aléatoires
def create_color_dict(size):
    # Liste des couleurs disponibles
    colors = ["argent", "beige", "blanc", "bleu", "corail", "indigo", "jaune", "lavande", "magenta", "marron", "mauve", "noir", "olive", "or", "orange", "orchidée", "rose", "rouge", "saumon", "vert",
          "silver", "beige", "white", "blue", "coral", "indigo", "yellow", "lavender", "magenta", "brown", "mauve", "black", "olive", "gold", "orange", "orchid", "pink", "red", "salmon", "green"]
    color_dict = {}
    for i in range(size):
        color = random.choice(colors)
        color_dict[color] = random.choice(colors)
    return color_dict

# Crée une map pour le jeu réflection
def create_map(size):
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