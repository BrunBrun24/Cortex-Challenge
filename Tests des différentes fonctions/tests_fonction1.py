from fonctions1 import *
from Creation_cartes import *
import timeit



def mesure_temps_execution(fonction, *args, **kwargs):
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
        temps_execution = timeit.timeit(lambda: fonction(*args, **kwargs), number=1)
        temps_total += temps_execution

    temps_moyen = temps_total / nb_repetition

    print(f"Temps moyen d'exécution : {temps_moyen:.2e} secondes")



donnees = {"code": "CA-001", "type": "calcul", "result": 14, "numbers": [2, 5, 11, 7, 1, 4]}
temps_execution = mesure_temps_execution(calcul, donnees)


donnees = {"code": "CO-001", "type": "couleur", "colors": {"black": "red", "blue": "green", "mauve": "black", "green": "purple", "white": "blue", "orange": "yellow", "pink": "pink", "yellow": "white", "red": "orange"}}
temps_execution = mesure_temps_execution(couleur, donnees)


donnees = {"code": "DO-001", "type": "doublon", "words": [["cow", "dog", "dog", "cat", "chicken", "firefox"], ["dog", "cow", "cat", "chicken", "cat", "cat"], ["chicken", "dog", "rabbit", "chicken", "firefox", "chicken"], ["cat", "cow", "dog", "cat", "dog", "cow"], ["firefox", "cat", "dog", "cow", "dog", "chicken"], ["cow", "cow", "dog", "rabbit", "cat", "dog"]]}
temps_execution = mesure_temps_execution(doublon, donnees)


donnees = {"code": "FR-001", "type": "frequence", "words": [["cow", "dog", "dog", "cat", "chicken", "firefox"], ["dog", "cow", "cat", "chicken", "cat", "cat"], ["chicken", "dog", "cat", "chicken", "firefox", "chicken"], ["cat", "cow", "dog", "cat", "dog", "cow"], ["firefox", "cat", "dog", "cow", "dog", "chicken"], ["cow", "cow", "dog", "chicken", "cat", "dog"]]}
temps_execution = mesure_temps_execution(frequence, donnees)


donnees = {"code": "LA-001", "type": "labyrinthe", "map": [["1", "X", "X", "X", "X", "X", "X", "", "", "2"], ["", "", "", "", "", "", "X", "", "X", ""], ["X", "X", "X", "X", "X", "", "X", "", "X", ""], ["X", "X", "X", "X", "X", "D", "X", "X", "X", ""], ["X", "X", "X", "", "", "X", "X", "", "", ""], ["X", "X", "X", "", "X", "X", "X", "", "X", "X"], ["4", "", "", "", "X", "X", "X", "", "", "3"]]}
temps_execution = mesure_temps_execution(labyrinthe, donnees)


donnees = {"code": "MA-001", "type": "manquant", "numbers": ["1R", "4R", "5R", "4B", "7B", "8B", "2R", "3R", "5B"]}
temps_execution = mesure_temps_execution(manquant, donnees)


donnees = {"code": "RA-001","type": "raisonnement","drawing" : [["X","X","X","","","X","X","X"],["X","X","X","","","X","X","X"],["X","X","X","X","X","X","X","X"]],"pieces" : {"A" : [["X", "X"],["X", "X"]],"B" : [["", "X", ""],["X", "X", "X"]],"C" : [["X", "X", ""],["", "X", "X"]]}}
temps_execution = mesure_temps_execution(raisonnement, donnees)


donnees = {"code": "RE-001", "type": "reflexion", "map": [[" ", 1, 2, 3, 4, ""], [15, "", "", "", "", 5], [14, "", "/", "", "/", 6], [13, "", "", "", "", 7], [12, "", "", "", "", 8], ["", 11, "L", 10, 9, ""]]}
temps_execution = mesure_temps_execution(reflexion, donnees)
