/*
Recursividad -> La recursividad es una función que se llama a si misma. Esto se le llama recursividad.
*/
//Dos formas de pensar
//1 <-- Pensamiento iterativo: El bucle for
function pow(x, n) {
  let result = 1;
  //Multiplicar el resultado por x n cantidad de veces en el ciclo
  for (let i = 0; i < n; i++) {
    result *= x;
  }
  return result;
}

console.log(pow(2, 3));

//Pensamiento recursivo -> Simplifica la tarea y se llama a si mismo
function powTwo(x, n) {
  if (n === 1) {
    return x;
  } else {
    return x * powTwo(x, n - 1);
  }
}
console.log(powTwo(2, 3));
