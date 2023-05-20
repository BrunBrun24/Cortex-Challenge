from Creation_cartes.creation_cartes import *
from fonctions1 import *
from fonctions2 import *
import timeit


def generation_carte(fonction):
    donnees = None
    if fonction == "couleur":
        donnees = create_color_dict()
    elif fonction == "calcul":
        donnees = list_number()
    elif fonction == "doublon":
        donnees = list_doublon()
    elif fonction == "frequence":
        donnees = list_words()
    elif fonction == "labyrinthe":
        donnees = map_labyrinthe()
    elif fonction == "manquant":
        donnees = list_numbers_colors()
    elif fonction == "raisonnement":
        donnees = dessins()
    elif fonction == "reflexion":
        donnees = map_reflexion()

    return donnees

def mesure_temps_execution_fonction(fonction):
    """
    Mesure le temps d'exécution d'une fonction avec des arguments donnés.
    :param fonction: La fonction à mesurer
    :param args: Les arguments positionnels de la fonction
    :param kwargs: Les arguments nommés de la fonction
    :return: Le temps d'exécution en secondes
    """
    
    nb_repetition = 5000
    temps_total = 0
    temps_total_f2 = 0

    for _ in range(nb_repetition):
        donnees =  generation_carte(fonction)
        # Création d'un nouveau dictionnaire à chaque itération
        if fonction == "couleur":
            temps_execution = timeit.timeit(lambda: couleur1(donnees), number=1)
            temps_total += temps_execution
            temps_execution = timeit.timeit(lambda: couleur2(donnees), number=1)
            temps_total_f2 += temps_execution
        elif fonction == "calcul":
            temps_execution = timeit.timeit(lambda: calcul1(donnees), number=1)
            temps_total += temps_execution
            temps_execution = timeit.timeit(lambda: calcul2(donnees), number=1)
            temps_total_f2 += temps_execution
        elif fonction == "doublon":
            temps_execution = timeit.timeit(lambda: doublon1(donnees), number=1)
            temps_total += temps_execution
            temps_execution = timeit.timeit(lambda: doublon2(donnees), number=1)
            temps_total_f2 += temps_execution
        elif fonction == "frequence":
            temps_execution = timeit.timeit(lambda: frequence1(donnees), number=1)
            temps_total += temps_execution
            temps_execution = timeit.timeit(lambda: frequence2(donnees), number=1)
            temps_total_f2 += temps_execution
        elif fonction == "labyrinthe":
            temps_execution = timeit.timeit(lambda: labyrinthe1(donnees), number=1)
            temps_total += temps_execution
            temps_execution = timeit.timeit(lambda: labyrinthe2(donnees), number=1)
            temps_total_f2 += temps_execution
        elif fonction == "manquant":
            temps_execution = timeit.timeit(lambda: manquant1(donnees), number=1)
            temps_total += temps_execution
            temps_execution = timeit.timeit(lambda: manquant2(donnees), number=1)
            temps_total_f2 += temps_execution
        elif fonction == "raisonnement":
            temps_execution = timeit.timeit(lambda: raisonnement1(donnees), number=1)
            temps_total += temps_execution
            temps_execution = timeit.timeit(lambda: raisonnement2(donnees), number=1)
            temps_total_f2 += temps_execution
        elif fonction == "reflexion":
            temps_execution = timeit.timeit(lambda: reflexion1(donnees), number=1)
            temps_total += temps_execution
            temps_execution = timeit.timeit(lambda: reflexion2(donnees), number=1)
            temps_total_f2 += temps_execution


    temps_moyen_f1 = temps_total / nb_repetition
    temps_moyen_f2 = temps_total_f2 / nb_repetition

    print(f"Temps moyen d'exécution pour la fonction {fonction} de fonction1 est de : {temps_moyen_f1:.2e} secondes")
    print(f"Temps moyen d'exécution pour la fonction {fonction} de fonction2 est de : {temps_moyen_f2:.2e} secondes")
    print("-----------------------------------------------------------------------------------------")

    if temps_moyen_f1 < temps_moyen_f2:
        utiliser = "fonction1"
    else:
        utiliser = "fonction2"

    return f"Donc pour la fonction {fonction} il faut utiliser : {utiliser}"

if __name__ == "__main__":
    list_temps_executions = []
    list_temps_executions.append(mesure_temps_execution_fonction("couleur"))
    list_temps_executions.append(mesure_temps_execution_fonction("calcul"))
    list_temps_executions.append(mesure_temps_execution_fonction("doublon"))
    list_temps_executions.append(mesure_temps_execution_fonction("frequence"))
    list_temps_executions.append(mesure_temps_execution_fonction("manquant"))
    list_temps_executions.append(mesure_temps_execution_fonction("raisonnement"))
    list_temps_executions.append(mesure_temps_execution_fonction("reflexion"))
    list_temps_executions.append(mesure_temps_execution_fonction("labyrinthe"))
    print()
    for l in list_temps_executions:
        print(l)


"""
Temps moyen d'exécution pour la fonction couleur de fonction1 est de : 1.78e-05 secondes
Temps moyen d'exécution pour la fonction couleur de fonction2 est de : 4.27e-05 secondes
-----------------------------------------------------------------------------------------
Temps moyen d'exécution pour la fonction calcul de fonction1 est de : 1.64e-05 secondes
Temps moyen d'exécution pour la fonction calcul de fonction2 est de : 2.46e-05 secondes
-----------------------------------------------------------------------------------------
Temps moyen d'exécution pour la fonction doublon de fonction1 est de : 5.04e-04 secondes
Temps moyen d'exécution pour la fonction doublon de fonction2 est de : 2.09e-04 secondes
-----------------------------------------------------------------------------------------
Temps moyen d'exécution pour la fonction frequence de fonction1 est de : 1.93e-04 secondes
Temps moyen d'exécution pour la fonction frequence de fonction2 est de : 1.01e-04 secondes
-----------------------------------------------------------------------------------------
Temps moyen d'exécution pour la fonction manquant de fonction1 est de : 3.11e-03 secondes
Temps moyen d'exécution pour la fonction manquant de fonction2 est de : 1.12e-04 secondes
-----------------------------------------------------------------------------------------
Temps moyen d'exécution pour la fonction raisonnement de fonction1 est de : 2.13e-04 secondes
Temps moyen d'exécution pour la fonction raisonnement de fonction2 est de : 2.10e-04 secondes
-----------------------------------------------------------------------------------------
Temps moyen d'exécution pour la fonction reflexion de fonction1 est de : 3.00e-06 secondes
Temps moyen d'exécution pour la fonction reflexion de fonction2 est de : 4.30e-06 secondes
-----------------------------------------------------------------------------------------
Temps moyen d'exécution pour la fonction labyrinthe de fonction1 est de : 4.52e-04 secondes
Temps moyen d'exécution pour la fonction labyrinthe de fonction2 est de : 4.50e-04 secondes
-----------------------------------------------------------------------------------------

Donc pour la fonction couleur il faut utiliser : fonction1
Donc pour la fonction calcul il faut utiliser : fonction1
Donc pour la fonction doublon il faut utiliser : fonction2
Donc pour la fonction frequence il faut utiliser : fonction2
Donc pour la fonction manquant il faut utiliser : fonction2
Donc pour la fonction raisonnement il faut utiliser : fonction2
Donc pour la fonction reflexion il faut utiliser : fonction1
Donc pour la fonction labyrinthe il faut utiliser : fonction2
"""