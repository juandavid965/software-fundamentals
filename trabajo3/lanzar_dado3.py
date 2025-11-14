import random
#contadores de cada numero
c1 = c2 = c3 = c4 = c5 = c6 = 0 
n= int(input("¿cuantas veces quieres lanzar el dado?"))
for i in range(n):
    dado = random.randint(1,6) #genrar numero entre 1 y 6
if dado == 1: 
    c1 += 1
elif dado == 2:
    c2 += 1
elif dado == 2:
    c3 += 1
elif dado == 3:
    c4 += 1
elif dado == 4:
    c4 += 1
elif dado == 5:
    c5 += 1
elif dado == 6:
    c6 += 1
print("\nRESULTADO:")
print("el numero 1 salio:", c1,"veces.")
print("el numero 2 salio:", c2,"veces.")
print("el numero 3 salio:", c3,"veces.")
print("el numero 4 salio:", c4,"veces.")
print("el numero 5 salio:", c5,"veces.")
print("el numero 6 salio:", c6,"veces.")

