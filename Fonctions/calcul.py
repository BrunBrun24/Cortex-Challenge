def calcul(donnee):
    """
    Trouve les ensembles de nombres dans la liste 'numbers' qui s'additionnent pour obtenir le résultat 'result'.
    Returns:
        list: Une liste de listes contenant les ensembles de nombres qui s'additionnent pour obtenir le résultat cible.
    """
    result = donnee["result"]
    numbers = donnee["numbers"]
    res = []
    numbers.sort()  # Trie les nombres pour obtenir les combinaisons dans l'ordre croissant
    trouver_combinaisons_recursif(donnee, 0, result, [], numbers, res)  # Appel initial de la fonction auxiliaire avec un total cible de 'result'
    
    output = []
    for solution in res:
        solution.sort()
        output.append('+'.join([str(x) for x in solution]))
    
    return output

def trouver_combinaisons_recursif(donnee, start, target, path, numbers, res):
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
                trouver_combinaisons_recursif(donnee, i + 1, target - numbers[i], path, numbers, res)  # Appel récursif avec le nouveau total cible
                path.pop()  # Retour en arrière (trouver_combinaisons_recursif)


donnees = {"code": "CA-001", "type": "calcul", "result": 14, "numbers": [2, 5, 11, 7, 1, 4]}
output = calcul(donnees)
print(output)