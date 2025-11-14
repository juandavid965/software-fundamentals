Algoritmo lanzar_dado2
	Definir n,i, dado, suma Como Entero 
	
	Escribir "¿cuantas veces quiere lanzar el dado?"
	Leer n 
	suma <- 0
	Para i <- 1 hasta n Con Paso 1 Hacer
		dado <- Aleatorio(1,6)
		Escribir "lanzamiento", i, ":", dado
		suma <- suma + dado 
	FinPara
	Escribir "la suma total de los valores son : ", suma 
FinAlgoritmo
