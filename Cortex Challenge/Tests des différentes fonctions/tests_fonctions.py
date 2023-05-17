from Creation_cartes.creation_cartes import *
from fonctions1 import *
from fonctions2 import *
import timeit



def mesure_temps_execution_fonction(fonction, chiffre):
    """
    Mesure le temps d'exécution d'une fonction avec des arguments donnés.
    :param fonction: La fonction à mesurer
    :param args: Les arguments positionnels de la fonction
    :param kwargs: Les arguments nommés de la fonction
    :return: Le temps d'exécution en secondes
    """
    
    nb_repetition = 5000
    temps_total = 0

    for _ in range(nb_repetition):
        donnees = None
        # Création d'un nouveau dictionnaire à chaque itération
        if fonction == "couleur":
            donnees = create_color_dict()
            if chiffre == 1:
                temps_execution = timeit.timeit(lambda: couleur1(donnees), number=1)
                temps_total += temps_execution
            else :
                temps_execution = timeit.timeit(lambda: couleur2(donnees), number=1)
                temps_total += temps_execution
        elif fonction == "calcul":
            donnees = list_number()
            if chiffre == 1:
                temps_execution = timeit.timeit(lambda: calcul1(donnees), number=1)
                temps_total += temps_execution
            else :
                temps_execution = timeit.timeit(lambda: calcul2(donnees), number=1)
                temps_total += temps_execution
        elif fonction == "doublon":
            donnees = list_doublon()
            if chiffre == 1:
                temps_execution = timeit.timeit(lambda: doublon1(donnees), number=1)
                temps_total += temps_execution
            else :
                temps_execution = timeit.timeit(lambda: doublon2(donnees), number=1)
                temps_total += temps_execution
        elif fonction == "frequence":
            donnees = list_words()
            if chiffre == 1:
                temps_execution = timeit.timeit(lambda: frequence1(donnees), number=1)
                temps_total += temps_execution
            else :
                temps_execution = timeit.timeit(lambda: frequence2(donnees), number=1)
                temps_total += temps_execution
        elif fonction == "labyrinthe":
            donnees = map_labyrinthe()
            if chiffre == 1:
                temps_execution = timeit.timeit(lambda: labyrinthe1(donnees), number=1)
                temps_total += temps_execution
            else :
                temps_execution = timeit.timeit(lambda: labyrinthe2(donnees), number=1)
                temps_total += temps_execution
        elif fonction == "manquant":
            donnees = list_numbers_colors()
            if chiffre == 1:
                temps_execution = timeit.timeit(lambda: manquant1(donnees), number=1)
                temps_total += temps_execution
            else :
                temps_execution = timeit.timeit(lambda: manquant2(donnees), number=1)
                temps_total += temps_execution
        elif fonction == "raisonnement":
            donnees = dessins()
            if chiffre == 1:
                temps_execution = timeit.timeit(lambda: raisonnement1(donnees), number=1)
                temps_total += temps_execution
            else :
                temps_execution = timeit.timeit(lambda: raisonnement2(donnees), number=1)
                temps_total += temps_execution
        elif fonction == "reflexion":
            donnees = map_reflexion()
            if chiffre == 1:
                temps_execution = timeit.timeit(lambda: reflexion1(donnees), number=1)
                temps_total += temps_execution
            else :
                temps_execution = timeit.timeit(lambda: reflexion2(donnees), number=1)
                temps_total += temps_execution


    temps_moyen = temps_total / nb_repetition

    print(f"Temps moyen d'exécution pour la fonction {fonction} est de : {temps_moyen:.2e} secondes")

    return temps_moyen

def test(chiffre):
    list_temps_executions = []
    list_temps_executions.append(mesure_temps_execution_fonction("couleur", chiffre))
    list_temps_executions.append(mesure_temps_execution_fonction("calcul", chiffre))
    list_temps_executions.append(mesure_temps_execution_fonction("doublon", chiffre))
    list_temps_executions.append(mesure_temps_execution_fonction("frequence", chiffre))
    list_temps_executions.append(mesure_temps_execution_fonction("manquant", chiffre))
    list_temps_executions.append(mesure_temps_execution_fonction("raisonnement", chiffre))
    list_temps_executions.append(mesure_temps_execution_fonction("reflexion", chiffre))
    list_temps_executions.append(mesure_temps_execution_fonction("labyrinthe", chiffre))

    return list_temps_executions

if __name__ == "__main__":
    print("Pour la fonction1 :")
    f1 = test(1)
    print()
    print("Pour la fonction2 :")
    f2 = test(2)
    print()

    print("Donc les fonctions à utiliser pour Cortex Challenge sont :")

    for i in range(len(f1)):
        if f1[i] < f2[i]:
            print("Il faut utiliser la fonction1")
        else:
            print("Il faut utiliser la fonction2")

"""
Pour la fonction1 :
Temps moyen d'exécution pour la fonction couleur est de : 1.73e-05 secondes
Temps moyen d'exécution pour la fonction calcul est de : 1.31e-05 secondes
Temps moyen d'exécution pour la fonction doublon est de : 5.72e-04 secondes
Temps moyen d'exécution pour la fonction frequence est de : 1.90e-04 secondes
Temps moyen d'exécution pour la fonction manquant est de : 2.10e-04 secondes
Temps moyen d'exécution pour la fonction raisonnement est de : 2.19e-04 secondes
Temps moyen d'exécution pour la fonction reflexion est de : 2.80e-06 secondes
Temps moyen d'exécution pour la fonction labyrinthe est de : 4.56e-04 secondes

Pour la fonction2 :
Temps moyen d'exécution pour la fonction couleur est de : 2.24e-05 secondes
Temps moyen d'exécution pour la fonction calcul est de : 1.15e-05 secondes
Temps moyen d'exécution pour la fonction doublon est de : 1.91e-04 secondes
Temps moyen d'exécution pour la fonction frequence est de : 1.86e-04 secondes
Temps moyen d'exécution pour la fonction manquant est de : 1.88e-03 secondes
Temps moyen d'exécution pour la fonction raisonnement est de : 2.15e-04 secondes
Temps moyen d'exécution pour la fonction reflexion est de : 4.16e-06 secondes
Temps moyen d'exécution pour la fonction labyrinthe est de : 4.52e-04 secondes

Donc les fonctions à utiliser pour Cortex Challenge sont :
Il faut utiliser la fonction1
Il faut utiliser la fonction2
Il faut utiliser la fonction2
Il faut utiliser la fonction2
Il faut utiliser la fonction1
Il faut utiliser la fonction2
Il faut utiliser la fonction1
Il faut utiliser la fonction2
"""