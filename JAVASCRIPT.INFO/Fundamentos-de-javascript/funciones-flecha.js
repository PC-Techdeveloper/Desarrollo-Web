//Versión más corta para crear funciones:
const SUM = (a, b) => a + b;

console.log(SUM(1, 4));

//Único argumento se puede omitir paréntesis alrededor de los parámetros
const DOUBLE = (n) => n * 2;
console.log(DOUBLE(3));
//Usando operador ternario -> condición ? expresión : expresión
let age = prompt('Cuál es tu edad?', 18);
let welcome =
  age < 18 ? () => console.log('Hola') : () => console.log('¡Saludos!');

welcome();

//Funciones de flecha multilínea:
let mult = (a, b) => {
  let resultado = a * b;
  return resultado;
};

console.log(mult(3, 3));
