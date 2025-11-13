Algoritmo Lanzar_Dado
	Definir dado Como Entero
	// genera un numero aleatorio entre 1 y 6
	dado <- Aleatorio(1,6)
	// Mostrar el numero obtenido
	Escribir 'el dado cayo en el numero:', dado
	// verifica si es es par o impar
	Si dado MOD 2=0 Entonces
		Escribir 'el numero es par'
	SiNo
		Escribir 'el numero es impar'
	FinSi
FinAlgoritmo
