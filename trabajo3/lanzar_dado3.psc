Algoritmo lanzar_dado3
	Definir n, i, dado Como Entero 
	Definir c1,c2,c3,c4,c5,c6 Como Entero
	//inicializar contadores
	c1 <- 0
	c2 <- 0
	c3 <- 0
	c4 <- 0
	c5 <- 0
	c6 <- 0
	Escribir "¿cuantas veces deseas lanzar el dado?"
	Leer n 
	
	Para i <- 1 Hasta n Con Paso 1 Hacer
		dado <- Aleatorio(1,6) // genera numero entre 1 y 6
		
		segun dado hacer 
			1:
				c1 <- c1 + 1
			2:
				c2 <- c2 + 1
			3:
				c3 <- c3 + 1
			4:
				c4 <- c4 + 1
			5: 
				c5 <- c5 + 1
			6:
				c6 <- c6 + 1
				
		FinSegun
	FinPara
	Escribir "resultado:"
	Escribir "el numero 1 salio: ", c1, "veces."
	Escribir "el numero 2 salio: ", c2, "veces."
	Escribir "el numero 3 salio: ", c3, "veces."
	Escribir "el numero 4 salio: ", c4, "veces."
	Escribir "el numero 5 salio: ", c5, "veces."
    Escribir "el numero 6 salio: ", c6, "veces."	
FinAlgoritmo
