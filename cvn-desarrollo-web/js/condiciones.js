/*Una condición es una declaración que da como resultado un valor booleano (True o False), que significa cierto o falso respectivamente.*/

//Sentencia if-else
if (2 > 3) {
  console.log('2 es mayor que 3');
} else {
  console.log('2 es menor que 3');
}

//Operadores de comparación
// ==, ===, ==, !=, !==, <, >, <=, >=
console.log(1 === 1);
console.log(2 !== '2');
console.log(2 <= 2);

//else if
if (2 > 3) {
  console.log('2 es mayor que 3');
} else if (2 < 3) {
  console.log('2 es menor que 3');
} else {
  console.log('2 es igual a 3');
}

//switch
let myVariable = 10;
switch (myVariable) {
  case 1:
    console.log('1 es menor que 2');
    break;
  case 2:
    console.log('2 es igual a 2');
    break;
  case 3:
    console.log('3 es mayor que 2');
    break;
  default:
    console.log('Valor desconocido');
}
