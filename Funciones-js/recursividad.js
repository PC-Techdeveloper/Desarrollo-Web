/*
La recursividad es una técnica de programación que consiste en que una función se llame a si misma. Para evitar que se invoque una infinidad de veces, se evita con una condición base.
*/

function countBack(number) {
  //condición base
  if (number < 0) {
    //Si el número es menor de 0, sale de la función
    return;
  }
  console.log(number);

  countBack(number - 1);
}

countBack(4);

// Usando recursividad devolviendo un valor

function factorial(n) {
  //Condición base
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

console.log(factorial(5));
console.log(factorial(3));
