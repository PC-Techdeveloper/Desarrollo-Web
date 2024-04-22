/*
null --> Representa una ausencia de valor intencionalmente, null es una primitiva, aunque el typeof operador devuelve que null es un objeto.
*/

let resultado = null;
console.log(typeof null);

/*
Definir una variable con null refleja el valor asignado a ella en algún momento de un script o un valor explícitamente ausente. También permite asignar el valor null a una referencia existene para borrar un valor anterior.
*/

/*
undefined --> Es un valor primitivo asignado a variables que acaban de ser declaradas, o al valor resultante de una operación que no devuelve un valor significativo.

Una función regresa explícitamente 'undefined' cuando su 'return' declaración no devuelve ningún valor.
*/

let noDefinido;

//En funciones -> Undefined
function myFunction() {
  return;
}

console.log(myFunction());

//Comparación de null y undefined
/*
El operador de igualdad estricta considera que los operandos de diferentes tipos de datos son desiguales.
*/

//Evalúa el valor.
console.log(null == undefined);

//Evalúa el valor y el tipo.
console.log(null === undefined);
