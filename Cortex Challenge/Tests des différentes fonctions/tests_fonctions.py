from Creation_cartes.creation_cartes import *
from fonctions1 import *
from fonctions2 import *
import timeit



def mesure_temps_execution_fonction1(fonction, *args, **kwargs):
    """
    Mesure le temps d'exécution d'une fonction avec des arguments donnés.
    :param fonction: La fonction à mesurer
    :param args: Les arguments positionnels de la fonction
    :param kwargs: Les arguments nommés de la fonction
    :return: Le temps d'exécution en secondes
    """
    
    nb_repetition = 10000
    temps_total = 0

    for _ in range(nb_repetition):
        donnees = None
        # Création d'un nouveau dictionnaire à chaque itération
        if fonction == couleur:
            donnees = create_color_dict()
        elif fonction == calcul:
            donnees = list_number()
        elif fonction == doublon:
            donnees = list_doublon()
        elif fonction == frequence:
            donnees = list_words()
        elif fonction == labyrinthe:
            donnees = map_labyrinthe()
        elif fonction == manquant:
            donnees = list_numbers_colors()
        elif fonction == raisonnement:
            donnees = dessins()
        elif fonction == reflexion:
            donnees = map_reflexion()

        temps_execution = timeit.timeit(lambda: fonction(donnees, **kwargs), number=1)
        temps_total += temps_execution

    temps_moyen = temps_total / nb_repetition

    print(f"Temps moyen d'exécution : {temps_moyen:.2e} secondes")

    return temps_moyen

def mesure_temps_execution_fonction2(fonction, *args, **kwargs):
    """
    Mesure le temps d'exécution d'une fonction avec des arguments donnés.
    :param fonction: La fonction à mesurer
    :param args: Les arguments positionnels de la fonction
    :param kwargs: Les arguments nommés de la fonction
    :return: Le temps d'exécution en secondes
    """
    
    nb_repetition = 10000
    temps_total = 0

    for _ in range(nb_repetition):
        donnees = None
        # Création d'un nouveau dictionnaire à chaque itération
        if fonction == couleur:
            donnees = create_color_dict()
        elif fonction == calcul:
            donnees = list_number()
        elif fonction == doublon:
            donnees = list_doublon()
        elif fonction == frequence:
            donnees = list_words()
        elif fonction == labyrinthe:
            donnees = map_labyrinthe()
        elif fonction == manquant:
            donnees = list_numbers_colors()
        elif fonction == raisonnement:
            donnees = dessins()
        elif fonction == reflexion:
            donnees = map_reflexion()

        temps_execution = timeit.timeit(lambda: fonction(donnees, **kwargs), number=1)
        temps_total += temps_execution

    temps_moyen = temps_total / nb_repetition

    print(f"Temps moyen d'exécution : {temps_moyen:.2e} secondes")

    return temps_moyen

def test(fonction):
    list_temps_executions = []
    list_temps_executions.append(fonction(couleur))
    list_temps_executions.append(fonction(calcul))
    list_temps_executions.append(fonction(doublon))
    list_temps_executions.append(fonction(frequence))
    list_temps_executions.append(fonction(manquant))
    list_temps_executions.append(fonction(raisonnement))
    list_temps_executions.append(fonction(reflexion))
    list_temps_executions.append(fonction(labyrinthe))

    return list_temps_executions

if __name__ == "__main__":
    f1 = test(mesure_temps_execution_fonction1)
    f2 = test(mesure_temps_execution_fonction2)


    for i in range(len(f1)):
        if f1[i] < f2[i]:
            print("Il faut utiliser la fonction1")
        else:
            print("Il faut utiliser la fonction2")

"""
Pour la fonction1 :
Temps moyen d'exécution pour couleur : 4.47e-05 secondes
Temps moyen d'exécution pour calcul : 1.48e-05 secondes
Temps moyen d'exécution pour doublon : 1.92e-04 secondes
Temps moyen d'exécution pour frequence : 1.89e-04 secondes
Temps moyen d'exécution pour manquant : 2.21e-03 secondes
Temps moyen d'exécution pour raisonnement : 2.10e-04 secondes
Temps moyen d'exécution pour reflexion : 8.29e-05 secondes
Temps moyen d'exécution pour labyrinthe : 4.22e-04 secondes

Pour la fonction2 :
Temps moyen d'exécution pour couleur : 2.25e-05 secondes
Temps moyen d'exécution pour calcul : 1.12e-05 secondes
Temps moyen d'exécution pour doublon : 1.90e-04 secondes
Temps moyen d'exécution pour frequence : 1.86e-04 secondes
Temps moyen d'exécution pour manquant : 2.58e-03 secondes
Temps moyen d'exécution pour raisonnement : 2.08e-04 secondes
Temps moyen d'exécution pour reflexion : 8.12e-05 secondes
Temps moyen d'exécution pour labyrinthe : 4.23e-04 secondes


Donc les fonctions à utiliser pour Cortex Challenge sont :

Il faut utiliser la fonction2 pour couleur
Il faut utiliser la fonction2 pour calcul
Il faut utiliser la fonction2 pour doublon
Il faut utiliser la fonction2 pour frequence
Il faut utiliser la fonction1 pour manquant
Il faut utiliser la fonction2 pour raisonnement
Il faut utiliser la fonction2 pour reflexion
Il faut utiliser la fonction1 pour labyrinthe
"""