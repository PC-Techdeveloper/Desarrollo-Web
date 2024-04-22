/*
Las primitivas BigInt son una adición relativamente nueva a JavaScript, que permite operaciones matemáticas con números fuera del rango permitido por Number. Para crear un BigInt, se añade 'n' al final de un literal númerico o pasar de un valor de cadena númerico o entero a la función BigInt().
*/

/*
No se pueden mezclar primitivas BigInt y Number en operaciones aritméticas estándar.
*/
const myNumber = 9999999999999999;
const myBigInt = 9999999999999999n;

console.log(myNumber);

console.log(myBigInt);

/*
Para crear operaciones aritméticas, definir ambos operandos como valores BigInt.
*/
console.log(9999999999999999 + 10); //Fuera de 1
console.log(9999999999999999n + 10n);

console.log(BigInt(123));
console.log(BigInt('0b10101'));
console.log(BigInt('0O123'));
