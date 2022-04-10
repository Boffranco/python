palabra= input('ingrese una palabra: ')
metodo1=False
if(metodo1):
    valor=0
    x=["a","e","i","o","u","l","n","r","s","t"]
    f=["d","g"]
    a=["b","c","m","p"]
    h=["f","h","v","w","y"]
    k=["k"]
    j=["j","x"]
    q=["q","z"]

    for c in palabra:
        if(c in x):
            valor+=1
        elif(c in f):
            valor+=2
        elif(c in a):
            valor+= 3
        elif(c in h):
            valor+=4    
        elif(c in k):
            valor+=5
        elif(c in j):
            valor+=8
        elif(c in q):
            valor+=10
    print(valor)        
else:
    #version 2
    dicc={ "a": 1, "e": 1,"i" : 1,"o" : 1,"u": 1,"l": 1,"n": 1,"r": 1,"s": 1,"t": 1,
            "d": 2,"g": 2, 
            "b": 3,"c": 3,"m": 3,"p": 3,
    "f": 4,"h": 4,"v": 4,"w": 4,"y": 4,
    "k":5,
    "j": 8,"x": 8,
    "q": 10,"z": 10 }
    total=0
    for c in palabra:
        total+=dicc[c]
    print(total)

    l=""
    for v in range(1,10):
        for k in list(dicc.keys()):
            if(dicc[k] == v):
                l+=" "+k
        print(l+"   " + str(v))
        l=""