numero = int(input("ingresa un numero entero o postivo: "))

if numero % 2 == 0:
    if numero >= 0:
        print (f"el numero {numero} es par positivo ")
    else:
        print (f"el numero {numero} es par negativo ") 
else: 
    if numero >= 0:
        print (f"el numero{numero} es impar positivo ")
    else:
        print (f"el numero{numero} es impar negativo ")
