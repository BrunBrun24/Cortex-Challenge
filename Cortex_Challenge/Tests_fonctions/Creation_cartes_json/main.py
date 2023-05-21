"""
ATTENTION IL FAUT EXECUTER CE FICHIER EN OUVRANT LE DOSSIER "Cortex Challenge" qui se trouve 4 dossier au dessus de ce fichier
"""

import shutil
import os
import json
from creation_cards_json import *
from fonctions_finish import *


def nom_id(fonction):
    global liste_id_couleur
    global liste_id_reflection
    global liste_id_calcul
    global liste_id_frequence
    global liste_id_manquant
    global liste_id_labyrinthe
    global liste_id_doublon
    global liste_id_raisonnement

    if fonction == "couleur":
        nombre = int(liste_id_couleur[-1][-1]) + 1
        id_suivant = liste_id_couleur[0][:3] + str(nombre)
        liste_id_couleur.append(id_suivant)
        return id_suivant, id_suivant
    elif fonction == "reflexion":
        nombre = int(liste_id_reflection[-1][-1]) + 1
        id_suivant = liste_id_reflection[0][:3] + str(nombre)
        liste_id_reflection.append(id_suivant)
        return id_suivant, id_suivant
    elif fonction == "calcul":
        nombre = int(liste_id_calcul[-1][-1]) + 1
        id_suivant = liste_id_calcul[0][:3] + str(nombre)
        liste_id_calcul.append(id_suivant)
        return id_suivant, id_suivant
    elif fonction == "frequence":
        nombre = int(liste_id_frequence[-1][-1]) + 1
        id_suivant = liste_id_frequence[0][:3] + str(nombre)
        liste_id_frequence.append(id_suivant)
        return id_suivant, id_suivant
    elif fonction == "manquant":
        nombre = int(liste_id_manquant[-1][-1]) + 1
        id_suivant = liste_id_manquant[0][:3] + str(nombre)
        liste_id_manquant.append(id_suivant)
        return id_suivant, id_suivant
    elif fonction == "labyrinthe":
        nombre = int(liste_id_labyrinthe[-1][-1]) + 1
        id_suivant = liste_id_labyrinthe[0][:3] + str(nombre)
        liste_id_labyrinthe.append(id_suivant)
        return id_suivant, id_suivant
    elif fonction == "doublon":
        nombre = int(liste_id_doublon[-1][-1]) + 1
        id_suivant = liste_id_doublon[0][:3] + str(nombre)
        liste_id_doublon.append(id_suivant)
        return id_suivant, id_suivant
    elif fonction == "raisonnement":
        nombre = int(liste_id_raisonnement[-1][-1]) + 1
        id_suivant = liste_id_raisonnement[0][:3] + str(nombre)
        liste_id_raisonnement.append(id_suivant)
        return id_suivant, id_suivant

    return None

def id_actuelle(fonction):
    global liste_id_couleur
    global liste_id_reflection
    global liste_id_calcul
    global liste_id_frequence
    global liste_id_manquant
    global liste_id_labyrinthe
    global liste_id_doublon
    global liste_id_raisonnement

    if fonction == "couleur":
        id = liste_id_couleur[-1]
    elif fonction == "calcul":
        id = liste_id_calcul[-1]
    elif fonction == "doublon":
        id = liste_id_doublon[-1]
    elif fonction == "frequence":
        id = liste_id_frequence[-1]
    elif fonction == "labyrinthe":
        id = liste_id_labyrinthe[-1]
    elif fonction == "manquant":
        id = liste_id_manquant[-1]
    elif fonction == "raisonnement":
        id = liste_id_raisonnement[-1]
    elif fonction == "reflexion":
        id = liste_id_reflection[-1]

    return id

def creation_donnees(fonction):
    donnees = None
    if fonction == "couleur":
        id = nom_id(fonction)
        id = id[0]
        donnees = create_color_dict(id)
    elif fonction == "calcul":
        id = nom_id(fonction)
        id = id[0]
        donnees = list_number(id)
    elif fonction == "doublon":
        id = nom_id(fonction)
        id = id[0]
        donnees = list_doublon(id)
    elif fonction == "frequence":
        id = nom_id(fonction)
        id = id[0]
        donnees = list_words(id)
    elif fonction == "labyrinthe":
        id = nom_id(fonction)
        id = id[0]
        donnees = map_labyrinthe(id)
    elif fonction == "manquant":
        id = nom_id(fonction)
        id = id[0]
        donnees = list_numbers_colors(id)
    elif fonction == "raisonnement":
        id = nom_id(fonction)
        id = id[0]
        donnees = dessins(id)
    elif fonction == "reflexion":
        id = nom_id(fonction)
        id = id[0]
        donnees = map_reflexion(id)

    return donnees

def creation_result():
    # Création du chemin complet du fichier
    file_path = os.path.join("Cortex_Challenge/cortex-challenge-test/", "results.json")

    open(file_path, 'w').close()

    # Écriture des données JSON dans le fichier
    with open(file_path, 'w') as file:
        file.write("{" + "\n")

def filename_json():
    global liste_filename_card_json

    last_filename = liste_filename_card_json[-1]
    current_number = int(last_filename.split("-")[1].split(".")[0])
    new_number = current_number + 1
    filename = liste_filename_card_json[0][:5] + str(new_number) + ".json"
    liste_filename_card_json.append(filename)
    return filename

def result(fonction, data):
    resultat = None
    if fonction == "couleur":
        resultat = couleur(data)
    elif fonction == "calcul":
        resultat = calcul(data)
    elif fonction == "doublon":
        resultat = doublon(data)
    elif fonction == "frequence":
        resultat = frequence(data)
    elif fonction == "labyrinthe":
        resultat = labyrinthe(data)
    elif fonction == "manquant":
        resultat = manquant(data)
    elif fonction == "raisonnement":
        resultat = raisonnement(data)
    elif fonction == "reflexion":
        resultat = reflexion(data)

    return resultat

def resultat_data_in_result(fonction, resultat):

    id = id_actuelle(fonction)

    if result is not int():
        resultat = f'"{resultat}"'

    # Création du chemin complet du fichier
    file_path = os.path.join("Cortex_Challenge/cortex-challenge-test/", "results.json")

    # Écriture des données JSON dans le fichier
    with open(file_path) as file:
        # Lit le fichier
        texte = file.read()

    # Écriture des données JSON dans le fichier
    with open(file_path, 'w') as file:
        file.write(texte + '    "' + id + '"' + " : [" + str(resultat) + "]" + "," + "\n")

def creation_cards_json(fonction):
    if not os.path.exists("Cortex_Challenge/cortex-challenge-test/cards"):
        os.makedirs("Cortex_Challenge/cortex-challenge-test/cards")

    # Création des données et du nom du fichier
    filename = filename_json()
    data = creation_donnees(fonction)
    # On récupère le résultat en fonction des données fournies
    resultat_data = result(fonction, data)
    # Mets le résultat dans le fichier result
    resultat_data_in_result(fonction, resultat_data)

    filepath = os.path.join("Cortex_Challenge/cortex-challenge-test/cards", filename)

    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False)

def creation_automatique(fonction, size):
    for _ in range(size):
        creation_cards_json(fonction)

def corrige_et_ferme_le_dict():
    # Création du chemin complet du fichier
    file_path = os.path.join("Cortex_Challenge/cortex-challenge-test/", "results.json")

    # Écriture des données JSON dans le fichier
    with open(file_path) as file:
        # Lit le fichier
        texte = file.read()

    texte = texte[:-2]

    # Écriture des données JSON dans le fichier
    with open(file_path, 'w') as file:
        file.write(texte + "\n" + "}")

    # Lecture du contenu du fichier JSON
    with open(file_path, 'r') as file:
        json_data = json.load(file)

    # Parcours des clés et valeurs du dictionnaire JSON
    for key, value in json_data.items():
        # Vérification si la clé ne commence pas par "CA" et si la valeur est un chiffre (représenté par une chaîne de caractères)
        if not key.startswith("CA") and isinstance(value[0], str) and value[0].isdigit():
            # Conversion de la valeur en entier
            json_data[key] = [int(value[0])]

    # Écriture du dictionnaire JSON mis à jour dans le fichier
    with open(file_path, 'w') as file:
        json.dump(json_data, file, ensure_ascii=False, indent=4)

def main():

    file_path = "result.json"
    if os.path.exists(file_path):
        os.remove(file_path)

    folder_path = "Cortex_Challenge/cortex-challenge-test/cards"
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)

    creation_result()

    size = 2

    creation_automatique("couleur", size)
    creation_automatique("reflexion", size)
    creation_automatique("calcul", size)
    creation_automatique("frequence", size)
    creation_automatique("manquant", size)
    creation_automatique("labyrinthe", size)
    creation_automatique("doublon", size)
    creation_automatique("raisonnement", size)

    corrige_et_ferme_le_dict()
    



if __name__ == '__main__':
    liste_id_couleur = ["CO-0"]
    liste_id_reflection = ["RE-0"]
    liste_id_calcul = ["CA-0"]
    liste_id_frequence = ["FR-0"]
    liste_id_manquant = ["MA-0"]
    liste_id_labyrinthe = ["LA-0"]
    liste_id_doublon = ["DO-0"]
    liste_id_raisonnement = ["RA-0"]
    liste_filename_card_json = ["card-0"]
    main()
