Algoritmo parte_final_dados_6
	
	Definir dado, total_tiros, suma_tiros, pares, impares Como Entero
	Definir respuesta Como Caracter
	
	total_tiros <- 0
	suma_tiros <- 0
	pares <- 0
	impares <- 0 
	
	Repetir
		dado <- Aleatorio(1,6)
		
		total_tiros <- total_tiros + 1
		suma_tiros <- suma_tiros + dado
		
		Escribir "tiro", total_tiros, ": ", dado 
		
		si dado % 2 = 0 entonces 
			pares <- pares + 1 
		SiNo
			impares <- impares + 1 
		FinSi
		
		Escribir "¿quieres volver a lanzar ? (s/n o si/no) "
		leer respuesta
		
	Hasta Que respuesta = "n" O respuesta = "no"
	Escribir ""
	Escribir  "--- el reporte---"
	Escribir "total de los tiros efectuados fueron: ", total_tiros
	Escribir "suma total de los tiros fueron: ", suma_tiros
	Escribir "total de los pares generados fueron: ", pares
	Escribir "total de los impares generados fueron: ", impares
	
FinAlgoritmo
