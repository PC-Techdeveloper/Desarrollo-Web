//DECLARACIÓN DE FUNCIONES -> Palabra clave function
function showMessage() {
  console.log('¡Hola Mundo!');
}
//Llamada a la función ejecuta el código:
showMessage();

//Variables Locales -> Una variable declarada dentro de una función
function secondShowMessage() {
  //Variable local
  let message = 'Hola, ¡Soy JavaScript!';
  console.log(message);
}

secondShowMessage();

//Variables Externas -> Acceder a una variable externa desde una función:
let userName = 'Juan';
function thirdShowMessage() {
  //Modificando la variable externa
  userName = 'Bob';
  let message = 'Hola,' + userName;
  console.log(message);
}

thirdShowMessage();

//Variables Globales -> Variables declaradas fuera de cualquier función

// Parámetros -> Pasar datos arbitrarios a funciones usando parámetros:
// Parámetros -> from,text
function myFunction(from, text) {
  console.log(from + ':' + text);
}
//Argumentos pasados a la función cuando se llama:
myFunction('Anna', '¡Hola!');

//Valores Predeterminados -> Valor que se usa si el argumento fue omitido:
function mySecondFunction(from, text = 'Sin texto') {
  console.log(from + ' : ' + text);
}

mySecondFunction('Jose');

//Parámetros predeterminados alternativos -> Asignar valores predeterminados a los parámetros:
// O usar el operador lógico OR (||)
function myThirdFunction(text) {
  if (text === undefined) {
    text = 'Mensaje vacío';
  }
  console.log(text);
}

myThirdFunction();

//Operador Nulling Coalescing -> ??
function showCount(count) {
  console.log(count ?? 'Desconocido!');
}

showCount(0);
showCount(null);
showCount();

//Devolviendo un valor -> Return (Cuando la ejecución lo alcanza, la función se detiene)
//También se puede retornar guardando desde una variable
function sum(a, b) {
  return a + b;
}
console.log(sum(1, 2));

//Puede habler múltiples return sin ningún valor, y la función se detiene inmediatamente:
function checkAge(age) {
  return age;
}

function showMovie(age) {
  if (!checkAge(age)) {
    return;
  }
  console.log('Mostrandote la pelicula!');
}

showMovie(25);

//Una función con un return vacío, sin return, devuelve undefined:
function doNothing() {}
console.log(doNothing() === undefined);

function secondDoNothing() {
  return;
}

console.log(secondDoNothing() === undefined);

/*
Nomenclatura de funciones:
Funciones que comienzan con...
'get' -> Devuelve un valor.
'calc' -> Calculan algo.
'create' -> Crean algo.
'check' -> Revisan algo y devuelven un valor booleano, etc.

Ejemplos de este tipo de nombres:
showMessage(..) -> Muestra un mensaje.
getAge(..) -> Devuelve la edad (La obtiene de alguna manera).
calcSum(..) -> Calcula una suma y devuelve el resultado.
createForm(..) -> Crea un formulario (Y usualmente lo devuelve).
checkPermission(..) -> Revisa permísos, y devuelve true/false.
*/

