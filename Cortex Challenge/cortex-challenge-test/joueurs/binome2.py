"""
L1 - MI-I : Concrétisation disciplinaire -- Cortex Challenge
"""

__team__ = "Binôme 2"
__authors__ = ["Paul AUBRUN", "Kevin PLECIS"]
__date__ = "16/02/2023"
__version__ = "0.0"

from typing import Union
from fonctions_all import *

def jouer(card: dict) -> Union[None, str, int]:
    '''
    Fonction commune à tous les groupes permettant de jouer tous ensemble
    :param card: la carte au format JSON
    :return: le résultat trouvé par son joueur. Si type non implémenté return None.
    '''
    
    if card["type"] == "couleur":
        return couleur(card)
    elif card["type"] == "réflexion":
        return reflexion(card)
    elif card["type"] == "calcul":
        return calcul(card)
    elif card["type"] == "fréquence":
        return frequence(card)
    elif card["type"] == "manquant":
        return manquant(card)
    elif card["type"] == "labyrinthe":
        return labyrinthe(card)
    elif card["type"] == "doublon":
        return doublon(card)
    elif card["type"] == "raisonnement":
        return raisonnement(card)
    return None