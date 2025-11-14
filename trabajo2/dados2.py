#dado 2 
import random
random.seed() #prepara random number generator 

print("¿cuantas veces quieres lanzar el dado?")
n= int (input())
suma = 0 
for i in range (1, n + 1, 1):
    dado = int (random.random()* 6) + 1
    print ("lanzamiento" + str(i) + ":" + str(dado))
    suma = suma + dado 
print("la suma de los dados es :" + str(suma)) 