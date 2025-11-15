import random
random.seed ()  #prepare random number generator 

pares = 0 
impares = 0 
print ("¿cuantos lanzamientos quieres realizar?")
n = int (input())
for i in range(1, n + 1, 1):
    dado = int (random.random() * 6) + 1 
    print ("lanzamiento " + str(i) + ":" + str (dado))
    if dado % 2 == 0 : 
        pares = pares + 1
    else: 
        impares = impares + 1 
    i = i + 1 
print("total de lso tiros pares:" + str(pares))
print("total de los tiros impares :" + str (impares))
