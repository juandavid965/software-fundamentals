import random

def lanzar_dado():
    """Retorna un número aleatorio entre 1 y 6."""
    return random.randint(1, 6)

def paridad(valor):
    """Retorna si un número es PAR o IMPAR."""
    return "PAR" if valor % 2 == 0 else "IMPAR"

# Lanzar los dos dados
dado1 = lanzar_dado()
dado2 = lanzar_dado()

print(f"Dado 1: {dado1} → {paridad(dado1)}")
print(f"Dado 2: {dado2} → {paridad(dado2)}")

# Verificar si ganaste
if dado1 == dado2:
    print(" YOU WIN! ")
else:
    print(" GAME OVER ")
