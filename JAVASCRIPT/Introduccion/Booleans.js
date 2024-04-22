/*
El tipo de dato primitivo booleano es un tipo de datos lógicos con solo dos valores --> true y false
*/

//Función Boolean() --> Se puede usar para convertir un valor a un valor booleano
console.log(Boolean('A string literal'));

/*
Los valores false --> 0, null, undefined, Nan, "", '', false. Los demás valores dan como resultado true
*/
let esMayorDeEdad = true;
let llueve = false;

console.log(Boolean(NaN));
console.log(Boolean(-0));
console.log(Boolean(5));
console.log(Boolean('false'));
