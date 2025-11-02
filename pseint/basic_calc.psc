//algoritm description:
//basic calc v1
//get two numbers
// add, subs, mult, div
//print results

Algoritmo basic_calc
	//1. Define vars and/or const
 	Definir num1, num2 Como Entero
	Definir add, subs, mult, div Como Real
	//2. intialize vars and/or const 
	//inputs
	num1 <- 20;
	num2 <- 45;
	//3. processes
	add <- num1 + num2;
	subs <- num1 - num2;
	mult <- num1 * num2;
	div <- num1 / num2; 
	//4. outputs
	Mostrar "addition: ", add;
	Mostrar "subtraction: ", subs;
	Mostrar "multiplicacion: ", mult;
	Mostrar "divison: ", div;
FinAlgoritmo
