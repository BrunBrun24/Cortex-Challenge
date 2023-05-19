from collections import Counter

def frequence(defis):
    """
    :return: Le mot le moins représenté (str)
    """
    word_count = Counter()
    for ligne in defis["words"]:
        word_count.update(ligne)
    
    return min(word_count, key=word_count.get)