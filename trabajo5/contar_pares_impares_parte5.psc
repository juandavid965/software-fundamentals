Algoritmo contar_pares_impares_parte5
	Definir n,i, dado Como Entero
	Definir pares, impares Como Entero
	
	pares <- 0
	impares <-0
	
	Escribir "¿cuantos lanzamientos quieres realizar ?"
	Leer n 
	
	Para i <- 1 hasta n Con Paso 1 Hacer
		dado <- Aleatorio(1,6)
		Escribir  "lanzamiento", i, ": ", dado
		
		si dado % 2 = 0 Entonces
			pares <- pares + 1 
		SiNo
			impares <- impares + 1 
		FinSi
	FinPara
	
Escribir  "" 
Escribir  "total de los tiros pares:", pares
Escribir  "total de los tiros impares:", impares 
	
FinAlgoritmo
