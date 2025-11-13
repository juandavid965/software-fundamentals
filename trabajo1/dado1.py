#dado alazar 
import random
random.seed()  #prepare random number generator 

dado = int(random.random()* 6) + 1
print ("el dado cayo en el numero: " +str(dado))
if dado %  2 == 0:
    print("el numero es PAR")
else:
    print("el numero es IMPAR")
    