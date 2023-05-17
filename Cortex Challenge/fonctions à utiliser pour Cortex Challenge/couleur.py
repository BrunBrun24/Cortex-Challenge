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