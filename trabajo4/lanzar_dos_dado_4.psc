Algoritmo lanzar_dos_dado_4
	Definir dado1, dado2 Como Entero
	definir contador Como Entero
	contador <- 0 
	Repetir
		// generar valores de 1 a 6 
		dado1 <- Aleatorio(1,6)
		dado2 <- Aleatorio(1,6)
		contador <- contador +1 
		Escribir "lanzamiento ", contador, ": ^[", dado1,",", dado2, "]"
	Hasta Que dado1 = 6 Y dado2 = 6 
	
	Escribir ""
	Escribir "salio par de 6 hurra. El programa termino."
	Escribir "el total de los lanzamientos : ", contador
	
FinAlgoritmo
