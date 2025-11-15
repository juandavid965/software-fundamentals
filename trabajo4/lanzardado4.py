import random 

# inicializar contador 
contador = 0 

while True:
    #generar valores entre 1 y 6 
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    contador += 1 

    print(f"lanzamiento {contador}: [{dado1}, {dado2}]")

    #verificar si salio par de 6 
    if dado1 == 6 and dado2 == 6:
        break

print()
print("salio par de 6, hurra el programa termino ")
print("total de lanzamientos:", contador)