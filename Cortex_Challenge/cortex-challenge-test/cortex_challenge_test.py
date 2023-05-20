"""
L1 - MI-I : Concrétisation disciplinaire -- Cortex Challenge

Fichier pour tester une partie sans interface graphique

"""

__author__ = "Antoine JAMIN"
__date__ = "2022-2023"
__email__ = "antoine.jamin@univ-angers.fr"

import os
import random
import time
import json
from typing import Union

import joueurs.binome2 as j2

joueurs = [
    {"classe": j2, "time": 0.0, "good": False, "playing": True,
     "win": {"couleur": 0, "réflexion": 0, "calcul": 0, "fréquence": 0, "manquant": 0, "labyrinthe": 0, "doublon": 0,
             "raisonnement": 0}, "puzzle": 0}
]


def get_time(player: dict) -> int:
    """
    Accesseur au temps de réponse d'un joueur
    :param player: le joueur
    :return: le temps de réponse
    """
    return player["time"]


def get_team(player: dict) -> str:
    """
    Accesseur au nom d'équipe
    :param player: le joueur
    :return: le nom de l'équipe
    """
    return player["classe"].__team__


def get_puzzle(player: dict) -> int:
    """
    Accesseur au nombre de cerveau puzzle
    :param player: le joueur
    :return: son nombre de cerveau puzzle
    """
    return player["puzzle"]


def get_sum_win(player: dict) -> int:
    """
    Accesseur à la somme du nombre de cartes gagnées
    :param player: le joueur
    :return: le nombre de cartes gagnées
    """
    return sum(player["win"].values())


def str_joueur(player: dict) -> str:
    """
    Joueur (dictionnaire) en chaîne de caractères
    :param player: le joueurs
    :return: informations du joueur en chaîne de caractères (nom équipe, ...)
    """
    return player["classe"].__team__ + " [" + str(player["win"]) + ", " + str(player["puzzle"]) + "]"


def str_joueurs(players: list, infos: str = "all", sep: str = " -- ") -> str:
    """
    Transforme une liste de joueurs en chaîne de caractères
    :param infos: type d'informations à afficher (si team on affiche que le nom de l'équipe sinon on utilise str_joueur)
    :param players: liste de joueurs
    :param sep: séparateur des joueurs
    :return: les joueurs séparés par " -- "
    """
    msg = ""
    for p in players:
        if infos == "team":
            msg += p["classe"].__team__ + sep
        else:
            msg += str_joueur(p) + sep
    return msg[:-len(sep)]


def stop_loosers(players: list) -> None:
    """
    Faire passe son tour aux joueurs
    :param players: liste des joueurs
    :return: liste de joueurs avec "playing" passé à False
    """
    for p in players:
        p["playing"] = False


def reward(players: list, card: dict) -> None:
    """
    récompenser le gagnant d'un manche
    :param players: liste des joueurs à récompenser
    :param card: carte joué
    :return: liste des joueurs mise à joueur avec un point en plus pour le gagnant
    """
    players.sort(key=get_time)
    if len(players) > 0:
        players[0]["win"][card["type"]] += 1


def puzzle(players: list) -> None:
    """
    Ajouter un morceau de cerveau puzzle dès que 2 cartes d'une même catégorie
    :param players: les joueurs
    :return: None
    """
    for p in players:
        for t, score in p["win"].items():
            if score == 2:
                p["win"][t] = 0
                p["puzzle"] += 1


def who_win(players: list) -> Union[None, dict]:
    """
    Il y a t'il un vainqueur ?
    :param players: les joueurs
    :return: un joueur (dictionnaire) si gagnant, None si pas de gagnant
    """
    for p in players:
        if p["puzzle"] == 4:
            return p
    return None


def str_victory(player: dict) -> str:
    """
    Chaîne de caractère pour afficher la fin de la partie
    :param player: le joueur gagnant
    :return: chaine de caractère d'affichage de fin de partie
    """
    joueurs.sort(key=get_team)
    joueurs.sort(key=get_sum_win, reverse=True)
    joueurs.sort(key=get_puzzle, reverse=True)
    if player is not None:
        msg = "Gagnant : " + player["classe"].__team__
        msg += "\nClassement :\n" + str_joueurs(joueurs, sep="\n")
    else:
        msg = "Aucun gagnant !\nClassement :\n" + str_joueurs(joueurs, sep="\n")
    return msg


if __name__ == '__main__':
    # Récupération et mélange des cartes
    cartes = os.listdir("Cortex_Challenge/cortex-challenge-test/cards")
    random.shuffle(cartes)
    results = json.load(open("Cortex_Challenge/cortex-challenge-test/results.json"))
    winner = dict()
    # Jeux
    for c in cartes:
        carte = json.load(open("Cortex_Challenge/cortex-challenge-test/cards/" + c, encoding='utf_8'))
        # Chaque joueur joue la carte son résultat et son temps d'execution sont sauvegardés
        for j in joueurs:
            if j["playing"]:
                start_time = time.time()
                try:
                    result = j["classe"].jouer(carte)
                except Exception as e:
                    result = e
                if result is not None:
                    j["time"] = time.time() - start_time
                    j["good"] = result in results[carte["code"]]
                else:
                    j["time"] = -1
            else:
                j["time"] = -1
                j["playing"] = True

        # Qui a non répondu, perdu et gagné classé du plus rapide au plus lent
        joueurs.sort(key=get_time)
        not_answered = list(filter(lambda joueur: joueur["time"] == -1, joueurs))
        loosers = list(filter(lambda joueur: joueur["time"] != -1 and not joueur["good"], joueurs))
        winners = list(filter(lambda joueur: joueur["time"] != -1 and joueur["good"], joueurs))

        # Qui doit passer son tour ?
        stop_loosers(loosers)

        # Qui a gagné ? (lui donner la carte)
        reward(winners, carte)

        # Y-a-t-il un nouveau morceau de cerveau puzzle à ajouter ?
        puzzle(winners)

        # Y-a-t-il un gagnant ? (4 morceaux de puzzle)
        winner = who_win(winners)
        if winner is not None:
            break

        print()
        print(carte["code"])
        print("Joueur n'ayant pas répondu", str_joueurs(not_answered))
        print("Joueurs n'ayant pas bien répondu", str_joueurs(loosers))
        print("Joueurs ayant bien répondu", str_joueurs(winners))
        print()
    print("\n--FIN--\n")
    print(str_victory(winner))
