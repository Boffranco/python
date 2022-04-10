#Tomando el texto del README.md de numpy, imprima todas las líneas que contienen ‘http’ o ‘https’.
with open("readme.txt", "rt") as f:
    query = [line for line in f.readlines()
    if ("http" or "https")
          in line]
    print(query)