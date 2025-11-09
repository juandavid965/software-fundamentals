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
	Escribir "enter number 1: " //show messege from pc to user
	Leer num1 //user enter a number
	
	Escribir "enter number2: " //show messege from pc to user
	leer num2 //user enter a number and program reads it
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
