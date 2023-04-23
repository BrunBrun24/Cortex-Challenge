def doublon(donnee):
    """
    Recherche un mot en double dans la liste de mots fournie.
    :return: (str) Le mot en double s'il existe, sinon un message indiquant qu'il n'y a pas de mot en double.
    """
    word_count = {}
    for ligne in donnee["words"]:
        for word in ligne:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    # Retourne le mot en double
    for cle, valeur in word_count.items():
        if valeur == 2:
            return cle
        
    return "Il n'y a pas de mot en double"


donnees = {"code": "DO-001", "type": "doublon", "words": [["cow", "dog", "dog", "cat", "chicken", "firefox"], ["dog", "cow", "cat", "chicken", "cat", "cat"], ["chicken", "dog", "rabbit", "chicken", "firefox", "chicken"], ["cat", "cow", "dog", "cat", "dog", "cow"], ["firefox", "cat", "dog", "cow", "dog", "chicken"], ["cow", "cow", "dog", "rabbit", "cat", "dog"]]}

output = doublon(donnees)
print(output)
