def frequence(defis):
    """
    :return: Le mot le moins représenté (str)
    """
    word_count = {}
    for ligne in defis["words"]:
        for word in ligne:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        
    return min(word_count, key=word_count.get)