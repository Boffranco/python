#Indique la palabra que aparece mayor cantidad de veces en el texto del README.md de numpy.
from collections import Counter
with open("readme.txt", "rt") as text:
    words = text.read().lower().split()
    # without counter
    mostCommon = max(words, key=words.count)
    print(mostCommon)

    # with counter
    print(Counter(words).most_common()[0])