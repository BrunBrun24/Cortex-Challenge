def frequence(donnee):
        """
        :return: Le mot le moins représenté (str)
        """
        word_count = {}
        for ligne in donnee["words"]:
            for word in ligne:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
            
        return min(word_count, key=word_count.get)


donnees = {"code": "FR-001", "type": "frequence", "words": [["cow", "dog", "dog", "cat", "chicken", "firefox"], ["dog", "cow", "cat", "chicken", "cat", "cat"], ["chicken", "dog", "cat", "chicken", "firefox", "chicken"], ["cat", "cow", "dog", "cat", "dog", "cow"], ["firefox", "cat", "dog", "cow", "dog", "chicken"], ["cow", "cow", "dog", "chicken", "cat", "dog"]]}

print(frequence(donnees))
# Moyenne des temps d'exécution : 3.07e-06 secondes