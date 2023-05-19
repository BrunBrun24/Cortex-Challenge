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