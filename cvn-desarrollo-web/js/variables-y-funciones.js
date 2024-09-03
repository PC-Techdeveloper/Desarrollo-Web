/*
Las variables se utilizan para almacenar datos y las funciones son segmentos de código que realizan una función específica.

A estas instrucciones se les denomina sentencias que pueden incluir valores, operadores, expresiones y comentarios.

Existen dos tipos de valores: Literals y variables

- Las literales son valoress fijos.
- Las variables pueden cambiar de valor.
*/

/*

Literales:

15.57 -> Número decimal
12 -> Número entero
'Hola Mundo' -> Cadena de caracteres
true -> Booleano
false -> Booleano
null -> Null
undefined -> Undefined
NaN -> Not a Number
Infinity -> Infinito

Variables:

let nombre = 15.57;
let nombre = 12;
let nombre = 'Hola Mundo';
let nombre = true;
let nombre = false;
let nombre = null;
let nombre = undefined;
let nombre = NaN;
let nombre = Infinity;

*/

let nombre1 = 15.57;
let nombre2 = 12;
let nombre3 = 'Hola Mundo';
let nombre4 = true;
let nombre5 = false;
let nombre6 = null;
let nombre7 = undefined;
let nombre8 = NaN;
let nombre9 = Infinity;

const PI = 3.14;

/*Funciones*/

//Función declarativa con parámetros
function myFunc(a, b) {
  let result = a * b;
  return result;
}

//Función con argumentos
console.log(myFunc(2, 3));
