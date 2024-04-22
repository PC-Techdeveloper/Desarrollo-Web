//Numbers -> infinity y NaN (No es un número, realizar cálculos matemáticos).
console.log(Number(10));
console.log(Number(null));
console.log(Number(false));
console.log(Number(true));
console.log('six' * 3);

let edad = 25;
const PI = 3.14;

//Cadena que contiene carácteres no numéricos, la función Number() muestra NaN.
console.log(Number(undefined));
console.log(Number('The number 3'));

//Ningún motivo para usar el objeto Number() como constructor
let numObject = new Number(15);
console.log(numObject);

//Números de punto flotante (float) y números enteros (int) -> Int para evitar errores de precisión
console.log(0.1 + 0.7);

/*
Operadores númericos: 
+,-,*,/,++,--,**,% --> Adición, resta, multiplicación, división, incremento, decremento, exponente y resto.
*/

/*
Operadores de Asignación: 
+= ,-= ,*= , /=, **=, %= --> Asignación de adición, asignación de resta, asignación de multiplicación, asignación de división, asignación de exponencial y asignación del resto.
*/

//Valores símbolicos --> Infinity (Positivo) y -Infinity (Negativo)
console.log(10 / 0);
//NaN --> Literal de cadena que contenga solo un número en una operación matemática.
console.log('2' * 2);
//Si no, retorna un error NaN ❌
console.log('two' * 2);
