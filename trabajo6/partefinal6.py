import random

total_tiros = 0
suma_tiros = 0
pares = 0
impares = 0

respuesta = ""

while True:
    dado = random.randint(1, 6)

    total_tiros += 1
    suma_tiros += dado

    print(f"Tiro {total_tiros}: {dado}")

    if dado % 2 == 0:
        pares += 1
    else:
        impares += 1

    respuesta = input("¿Quieres volver a lanzar? (s/n o si/no): ").lower()

    if respuesta == "n" or respuesta == "no":
        break

print("\n--- EL REPORTE ---")
print("Total de tiros efectuados:", total_tiros)
print("Suma total de los tiros:", suma_tiros)
print("Total de pares generados:", pares)
print("Total de impares generados:", impares)
