import json

class Defis_1:
    def __init__(self, fichier_defis) -> None:

        with open(fichier_defis, 'r') as f:
            self.defis = json.load(f)

    def couleur(self):
        """
        Vérifie si les couleurs dans les défis sont valides en comparant avec des listes de couleurs en français et en anglais.
        :return: la clef du dictionnaire colors correspondant à la même couleur que sa clef, sinon False
        """
        couleur_fr = ("argent", "beige", "blanc", "bleu", "corail", "indigo", "jaune", "lavande", "magenta", "marron", "mauve", "noir", "olive", "or", "orange", "orchidée", "rose", "rouge", "saumon", "vert")
        couleur_en = ("silver", "beige", "white", "blue", "coral", "indigo", "yellow", "lavender", "magenta", "brown", "mauve", "black", "olive", "gold", "orange", "orchid", "pink", "red", "salmon", "green")
        
        # On parcourt la liste des couleurs
        for cle,valeur in self.defis["colors"].items():
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

    def reflexion(self):
        """
        Cherche où se trouve la lampe dans la map
        :return: la fonction "parcours_lampe_torche"
        """
        direction_lampe_torche = None
        ligne_lampe = None
        colonne_lampe = None

        # On récupère la direction de la lampe torche et ses coordonnées
        for i, ligne in enumerate(self.defis["map"]):
            # Si la lampe se trouve sur la première ligne
            if "L" in ligne and i == 0:
                direction_lampe_torche = "bas"
                ligne_lampe = i
                colonne_lampe = ligne.index("L")
            # Si la lampe se trouve sur la dernière ligne
            elif "L" in ligne and i == len(self.defis["map"])-1:
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

        return self.parcours_lampe_torche(direction_lampe_torche, ligne_lampe, colonne_lampe)               

    def parcours_lampe_torche(self, direction, ligne, colonne):
        """
        Parcours la map en suivant le faisceau lumineux
        :param:
            direction : "string"
            ligne : "int"
            colonne : "int"
        :return: un entier (int)
        """
        if type(self.defis["map"][ligne][colonne]) == int:
            return self.defis["map"][ligne][colonne]

        direction = self.si_miroir(direction, ligne, colonne)
        
        if direction == "bas":
            return self.parcours_lampe_torche(direction, ligne+1, colonne)
        elif direction == "haut":
            return self.parcours_lampe_torche(direction, ligne-1, colonne)
        elif direction == "droite":
            return self.parcours_lampe_torche(direction, ligne, colonne+1)
        else:
            return self.parcours_lampe_torche(direction, ligne, colonne-1)

    def si_miroir(self, direction, ligne, colonne):
        """
        Indique si sur les coordonnées pris en paramètres, il y a un miroir
        :param:
            direction : "string"
            ligne : "int"
            colonne : "int"
        :return: la direction (string)
        """
        if self.defis["map"][ligne][colonne] == "/":
            if direction == "haut":
                return "droite"
            elif direction == "bas":
                return "gauche"
            elif direction == "droite":
                return "haut"
            elif direction == "gauche":
                return "bas"
        elif self.defis["map"][ligne][colonne] == "\\":
            if direction == "haut":
                return "gauche"
            elif direction == "bas":
                return "droite"
            elif direction == "droite":
                return "bas"
            elif direction == "gauche":
                return "haut"
            
        return direction

    def calcul(self):
        """
        Fonction qui trouve toutes les combinaisons de nombres dans la liste qui, additionnées ensemble, donnent le nombre cible.

        Args:
            nombre_cible (int): Le nombre cible à atteindre.
            nombres (list): Une liste de nombres.

        Returns:
            list: Une liste de toutes les combinaisons trouvées. Si aucune combinaison n'est trouvée, retourne une liste vide.
        """
        nombre_cible = self.defis["result"]
        nombres =self.defis["numbers"]
        combinaisons = []
        self.trouver_combinaisons_recursif(nombre_cible, nombres, 0, [], combinaisons)

        # Convertir les listes de nombres en chaînes de caractères avec des "+" comme séparateurs
        combinaisons = ['+'.join(map(str, combinaison)) for combinaison in combinaisons]

        return combinaisons

    def trouver_combinaisons_recursif(self, nombre_cible, nombres, index, combinaison_actuelle, combinaisons):
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
        self.trouver_combinaisons_recursif(nombre_cible, nombres, index + 1, combinaison_actuelle, combinaisons)

        # Inclure le nombre actuel dans la combinaison
        if nombre_cible >= nombres[index]:
            # Ajouter le nombre actuel à la combinaison
            combinaison_actuelle.append(nombres[index])
            self.trouver_combinaisons_recursif(nombre_cible - nombres[index], nombres, index + 1, combinaison_actuelle, combinaisons)
            # Retirer le nombre actuel de la combinaison pour explorer d'autres possibilités
            combinaison_actuelle.pop()

    def frequence(self):
        """
        :return: Le mot le moins représenté (str)
        """
        occurence_words = {}  # Dictionnaire pour stocker les occurrences de chaque mot
        for ligne in self.defis["words"]:
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

    def manquant(self):
        """
        Fonction permettant de trouver le premier nombre manquant dans une liste de nombres.
        :return: int: Le premier nombre manquant dans la liste de nombres.
        """
        list_color = [] # List des couleurs disponible
        list_numbers_color1 = []
        list_numbers_color2 = []
        # Permet de récupérer les couleurs disponible et de les mettre dans "list_color"
        for color in self.defis["numbers"]:
            # On sait que l'initiale de la couleur est au dernier caractère
            if color[-1] not in list_color:
                list_color.append(color[-1])
        # Permet de récupérer les nombres et de les mettres dans leur list respective
        for color in self.defis["numbers"]:
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

    def labyrinthe(self):
        """
        Cherche les coordonnées de la case départ
        :return: la fonction "parcours_labyrinthe"
        """
        ligne_start = None
        colonne_start = None
        position = 0
        # On récupère la ligne de la position de départ 
        for ligne in self.defis["map"]:
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

        return self.parcours_labyrinthe(ligne_start, colonne_start, derniere_direction = "")

    def parcours_labyrinthe(self, ligne, colonne, derniere_direction):
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
        case = self.defis["map"][ligne][colonne]

        if case == "1":
            return 1
        elif case == "2":
            return 2
        elif case == "3":
            return 3
        elif case == "4":
            return 4

        max_ligne = len(self.defis["map"])  # Nombre de lignes
        max_colonne = len(self.defis["map"][0])  # Nombre de colonnes (en supposant que toutes les lignes ont la même longueur)
        arrivees = ["1", "2", "3", "4"]
        # Si la ligne se trouve sur la map et que les coordonnées (avec ligne+1) sont dans "arrivees"
        if (ligne < max_ligne-1) and (self.defis["map"][ligne+1][colonne] == "" or self.defis["map"][ligne+1][colonne] in arrivees) and ((derniere_direction != "bas") or (derniere_direction == "")):
            derniere_direction = "haut"
            return self.parcours_labyrinthe((ligne+1), colonne, derniere_direction)
        # Si la ligne se trouve sur la map et que les coordonnées (avec ligne-1) sont dans "arrivees"
        elif (ligne > 0) and (self.defis["map"][ligne-1][colonne] == "" or self.defis["map"][ligne-1][colonne] in arrivees) and ((derniere_direction != "haut") or (derniere_direction == "")):
            derniere_direction = "bas"
            return self.parcours_labyrinthe((ligne-1), colonne, derniere_direction)
        # Si la colonne se trouve sur la map et que les coordonnées (avec colonne+1) sont dans "arrivees"
        elif (colonne < max_colonne-1) and (self.defis["map"][ligne][colonne+1] == "" or self.defis["map"][ligne][colonne+1] in arrivees) and ((derniere_direction != "droite") or (derniere_direction == "")):
            derniere_direction = "gauche"
            return self.parcours_labyrinthe(ligne, (colonne+1), derniere_direction)
        # Si la colonne se trouve sur la map et que les coordonnées (avec colonne-1) sont dans "arrivees"
        elif (colonne > 0) and (self.defis["map"][ligne][colonne-1] == "" or self.defis["map"][ligne][colonne-1] in arrivees) and ((derniere_direction != "gauche") or (derniere_direction == "")):
            derniere_direction = "droite"
            return self.parcours_labyrinthe(ligne, (colonne-1), derniere_direction)

    def doublon(self):
        """
        Recherche un mot en double dans la liste de mots fournie.
        :return: (str) Le mot en double s'il existe, sinon un message indiquant qu'il n'y a pas de mot en double.
        """
        all_words = []
        list_words = []
        dict_words = {}
        # Met tous les mots dans une seul liste
        for ligne in self.defis["words"]:
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

    def raisonnement(self):
        """
        Applique un raisonnement sur le dessin en utilisant différentes méthodes pour vérifier s'il y a une solution possible.
        :return: Le nom de la solution trouvée, sinon (str) "Aucune de ces solutions n'est la bonne".
        """
        drawing = self.defis["drawing"]
        # On regarde si il y a possibilité d'enlever des colonnes à droite du dessin
        decalage = self.decalage_raisonnement(drawing)

        # On décale chaque ligne du dessin par "decalage"
        new_drawing = []
        for ligne in drawing:
            if "" in ligne:
                new_drawing.append(ligne[decalage:])

        # On regarde si il y a possibilité d'enlever des colonnes à gauche du dessin mais pour cela on va inverser chaque ligne du dessin
        new_drawing = self.retourne_raisonnement(new_drawing)
        # On regarde si il y a possibilité d'enlever des colonnes à droite du dessin
        decalage_new_drawing = self.decalage_raisonnement(new_drawing)

        # On décale chaque ligne du dessin par "decalage_new_drawing"
        finish_drawing = []
        for ligne in new_drawing:
            if "" in ligne:
                finish_drawing.append(ligne[decalage_new_drawing:])

        # On remet le dessin à l'endroit
        finish_drawing = self.retourne_raisonnement(finish_drawing)
        # On inverse le vide ("") avec les murs ("X")
        finish_drawing = self.inversion_raisonnement(finish_drawing)
        # On regarde si une solution est possible
        for nom, map in self.defis["pieces"].items():
            if finish_drawing == map:
                return nom

        return "Aucune de ces solutions n'est la bonne"
    
    def decalage_raisonnement(self, drawing):
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

    def retourne_raisonnement(self, drawing):
        """
        Retourne horizontalement chaque ligne du dessin.
        :param drawing: (list) Le dessin représenté sous forme de liste de listes.
        :return: (list) Le dessin modifié avec chaque ligne retournée horizontalement.
        """
        new_drawing = []
        for ligne in drawing:
            new_drawing.append(ligne[::-1])

        return new_drawing

    def inversion_raisonnement(self, drawing):
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

    def main(self):
        if self.defis["type"] == "couleur":
            print(self.couleur())
        elif self.defis["type"] == "reflexion":
            print(self.reflection())
        elif self.defis["type"] == "calcul":
            print(self.calcul())
        elif self.defis["type"] == "frequence":
            print(self.frequence())
        elif self.defis["type"] == "manquant":
            print(self.manquant())
        elif self.defis["type"] == "labyrinthe":
            print(self.labyrinthe())
        elif self.defis["type"] == "doublon":
            print(self.doublon())
        elif self.defis["type"] == "raisonnement":
            print(self.raisonnement())


if __name__ == "__main__":
    read_json_couleur = "C:/Users/aubru/Documents/Professionnel/MI/P5/Projets/Cortex Challenge/cortex-challenge-test/cards/card-1.json"
    read_json_reflection = "C:/Users/aubru/Documents/Professionnel/MI/P5/Projets/Cortex Challenge/cortex-challenge-test/cards/card-2.json"
    read_json_calcul = "C:/Users/aubru/Documents/Professionnel/MI/P5/Projets/Cortex Challenge/cortex-challenge-test/cards/card-3.json"
    read_json_frequence = "C:/Users/aubru/Documents/Professionnel/MI/P5/Projets/Cortex Challenge/cortex-challenge-test/cards/card-4.json"
    read_json_manquant = "C:/Users/aubru/Documents/Professionnel/MI/P5/Projets/Cortex Challenge/cortex-challenge-test/cards/card-5.json"
    read_json_labyrinthe = "C:/Users/aubru/Documents/Professionnel/MI/P5/Projets/Cortex Challenge/cortex-challenge-test/cards/card-6.json"
    read_json_doublon = "C:/Users/aubru/Documents/Professionnel/MI/P5/Projets/Cortex Challenge/cortex-challenge-test/cards/card-7.json"
    read_json_raisonnement = "C:/Users/aubru/Documents/Professionnel/MI/P5/Projets/Cortex Challenge/cortex-challenge-test/cards/card-8.json"

    Cortex_challenge = Defis_1(read_json_couleur)
    Cortex_challenge.main()
    Cortex_challenge = Defis_1(read_json_reflection)
    Cortex_challenge.main()
    Cortex_challenge = Defis_1(read_json_calcul)
    Cortex_challenge.main()
    Cortex_challenge = Defis_1(read_json_frequence)
    Cortex_challenge.main()
    Cortex_challenge = Defis_1(read_json_manquant)
    Cortex_challenge.main()
    Cortex_challenge = Defis_1(read_json_labyrinthe)
    Cortex_challenge.main()
    Cortex_challenge = Defis_1(read_json_doublon)
    Cortex_challenge.main()
    Cortex_challenge = Defis_1(read_json_raisonnement)
    Cortex_challenge.main()