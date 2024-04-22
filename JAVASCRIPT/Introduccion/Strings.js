/*
Cualquier conjunto de carácteres (letras, números, símbolos, etc.) entre un conjunto de comillas dobles ("") o comillas simples ('') es una primitiva de cadena.
*/

console.log('Hello, World!');
console.log('Hello, World!');

//Literal de cadena
console.log('"A string:" I said.');

//Función string() -> Convierte un valor específico en un literal de cadena
let myString = String(10);

console.log(myString);

console.log(typeof myString);

/*
Concatenación --> Un solo signo más (+) actúa como un operador de concatenación y combina varios valores en una sola cadena
*/

console.log('My' + ' string');

/*
Literales de cadena y literales de plantilla --> Usar cadenas simples para específicar literales de plantillas, los literales de cadena se crean con comillas simples o dobles, los literales de plantilla peermiten la interpolación de cadenas y las cadenas de varias líneas.
*/

const MY_STRING = 'This is a string';
console.log(MY_STRING);

/*
Los literales de plantilla pueden contener expresiones de marcador de posición marcadas por un signo de dolar y llaves (${}), lo que significa que el resultado de la expresión reemplaza al marcador de posición en la cadena final.
*/

console.log(`The result is ${2 + 4}`);

//Escapar carácteres -> \
console.log('"I\'m a string," I said.');

let nombre = 'Pedro';
let mensaje = 'Hola Mundo!';
