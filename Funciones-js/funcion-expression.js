/*
Una función expression es una función que se asigna a una variable.
*/

// Esto es una function expression
const sum = function (a, b) {
  return a + b;
};

// Esto es una declaración de función
function mult(a, b) {
  return a * b;
}

console.log(sum(1, 2));

// HOISTING

/*
Mueve las declaraciones y funciones al principio del código, de forma que se pueda usar incluso antes de declararlas
*/

// Con las function expression da un ERROR ❌

// console.log(resta(4, 2));

const resta = function (a, b) {
  return a - b;
};

// Con la declaración de función FUNCIONA! ✅

console.log(division(4, 2));

function division(a, b) {
  return a / b;
}
