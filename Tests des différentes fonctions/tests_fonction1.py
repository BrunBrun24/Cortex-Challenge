from Creation_cartes.creation_cartes import *
from fonctions1 import *
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



mesure_temps_execution(couleur)
mesure_temps_execution(calcul)
mesure_temps_execution(doublon)
mesure_temps_execution(frequence)
mesure_temps_execution(manquant)
mesure_temps_execution(raisonnement)
mesure_temps_execution(reflexion)

#mesure_temps_execution(labyrinthe)