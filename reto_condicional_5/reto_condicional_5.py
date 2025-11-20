
tipoID = input("Ingresa el tipo de identificación (CC, PS, CE, CI): ")
nombre = input("Ingresa tus nombres: ")
apellido = input("Ingresa tus apellidos: ")
genero = input("Ingresa tu género (M/F): ").upper()
anioNacimiento = int(input("Ingresa tu año de nacimiento: "))
direccion = input("Ingresa tu dirección: ")
telefono = input("Ingresa tu teléfono: ")
salario = float(input("Ingresa tu salario: "))


if salario <= 1200000:
    if genero == "F":
        aumento = salario * 0.10     
    else:
        aumento = salario * 0.08     
elif salario < 2000000:
    aumento = salario * 0.05         
else:
    if genero == "F":
        aumento = salario * 0.03     
    else:
        aumento = salario * 0.025    


salarioFinal = salario + aumento



print(f"Empleado: {nombre} {apellido}")
print(f"Salario inicial: {salario}")
print(f"Aumento aplicado: {aumento}")
print(f"SALARIO FINAL: {salarioFinal}")

