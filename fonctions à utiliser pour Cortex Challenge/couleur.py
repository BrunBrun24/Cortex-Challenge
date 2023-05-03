def couleur(donnee):
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

    for cle, valeur in donnee["colors"].items():
        for c, v in dict.items():
            if cle == valeur:
                return cle
            elif (cle == c) and (valeur == v):
                return cle
            elif (cle == v) and (valeur == c):
                return cle
    return False

donnees = {"code": "CO-001", "type": "couleur", "colors": {"black": "red", "blue": "green", "mauve": "black", "green": "purple", "white": "blue", "orange": "yellow", "pink": "pink", "yellow": "white", "red": "orange"}}

output = couleur(donnees)
print(output)
# Moyenne des temps d'exécution : 8.40e-06 secondes