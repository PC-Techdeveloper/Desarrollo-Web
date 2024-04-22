/*
El flujo de control es el orden en el que el intérprete de JavaScript ejecuta las declaraciones. Si una secuencia de comandos no incluye declaraciones que alteren su flujo, se ejecuta de principio a fin, una línea a la vez. Las estructuras de control se usan para determinar si un conjunto de declaraciones se ejecuta según un conjunto definido de criterios. Si se ejecuta un conjunto de declaraciones repetidamente o si se interrumpe una secuencia de declaraciones.
*/

/*
Instrucciones condicionales: Determinan si el código se debe ejecutar en función de una o más condicionales. Una sentencia condicionl ejecuta el código que contiene si la condición asociada (o el conjunto de condiciones) se evalúa como 'true'. De lo contrario, se omite el código.
*/

//IF

number1 = 5;

if (number1 === 5) {
  console.log('El número es correcto!');
}

//IF...ELSE
const myString = 'True';

if (myString === 'True') {
  console.log(myString);
} else {
  console.log('False');
}

//IF...ELSE -> ELSE...IF...ELSE --> Mejor legibilidad de código

let myCondition = 14;

if (myCondition === 5) {
  console.log('Five');
} else if (myCondition === 3) {
  console.log('Three');
} else {
  console.log('Wrong Number!');
}

/*
Operador condicional ternario: Es la abreviatura para ejecutar una expresión de forma condicional. Es el único operador de JavaScript que usa tres operandos:

1. ? -> Una condición que se evaluará.
2. : -> La expresión que se ejecutará si la condición se evalúa como 'true'.
3. La expresión que se ejecutará si la condición se evalúa como 'false'.
*/

const myFirstResult = true ? 'First Value' : 'Second Value';
const mySecondResult = false ? 'First Value' : 'Second Value';

console.log(myFirstResult);

console.log(mySecondResult);

/*
Switch...case -> Se utiliza para comprobar el valor de una expresión con una lista de valores potenciales definidos con una o más palabras clave 'case'.

Cuando el intérprete alcanza un case con un valor que coincide con la expresión que se está evaluando entre paréntesis después de la palabra clave 'switch', ejecuta cualquier declaración que siga a esa cláusula 'case'.
*/

switch (true) {
  case false:
    console.log('False');
    break;
  case true:
    console.log('True');
    break;
  default:
    console.log('Caso Incorrecto!');
    break;
}

/*
Iteración y bucles: Los bucles permiten repetir un conjunto de declaraciones mientras se cumpla una condición o hasta que se cumpla una condición. Usar bucles ejecuta un conjunto de instrucciones una cantidad fija de veces, hasta que se logre un resultado específico o hasta que el intérprete llegue al final de una estructura de datos iterable.
*/

/*
While --> Si la condición específicada se evalúa en un principio como 'true', se ejecuta la instrucción . De lo contrario, el bucle nunca se ejecuta. Después de cada iteración, la condición se vuelve a evalúar y, si aún es 'true', se repite el bucle. 
*/

//WHILE
console.log('Bucle While');
let contador = 1;

while (contador < 11) {
  console.log(contador);
  contador++;
}

/*
Do...while --> La evaluación condicional ocurre al final de cada iteración del bucle. Esto significa que el cuerpo del bucle siempre se ejecuta al menos 1 vez.
*/

//DO...WHILE
console.log('Bucle DO...WHILE');
let i = 0;

do {
  i = i + 1;
  console.log(i);
} while (i < 5);

/*
For --> La sentencia for en JavaScript consiste de tres expresiones y una declaración:

1. Inicialización -> Crear contadores
2. Condición -> Expresión que es evaluada antes de la ejecución de cada iteración.
3. Expresión final -> Expresión que se ejecuta luego de cada iteración.
4. Sentencia o declaración -> Código que será ejecutado repetidamente por el bucle (break--continue).

*/
//FOR
console.log('Bucle For');

let arr = [1, 2, 3];

for (let i = 0; i <= arr.length - 1; i++) {
  console.log(arr[i]);
}

/*
For...Of --> Para iterar sobre los valores almacenados en una estructura de datos iterables, como un array, un conjunto o un mapa.
*/

//For...Of
console.log('Bucle For...OF');

const myIterable = [true, false, true];

for (const myElement of myIterable) {
  console.log(myElement);
}

/*
For...in --> Para iterar sobre las propiedades que se pueden enumerar de un objeto, incluidas las propiedades heredadas que se pueden enumerar.
*/

//For...In
console.log('Bucle For...In');

const myObject = { miProperty: true, mySecondProperty: false };

for (const myKey in myObject) {
  const myValue = myObject[myKey];
  console.log(`${myKey} : ${myValue}`);
}

/*
ForEach() --> Los métodos que proporcionan los constructores Array, Map, Set y NodeList proporcionan una abreviatura útil para iterar sobre una estructra de datos en el contexto de una función de devolución de llamada. Un bucle creado con cualquier método forEach() NO se puede interrumpir usando break o continue.
*/

//ForEach

console.log('Bucle ForEach');

const myArray = [true, false];

myArray.forEach((myElement, i, originalArray) => {
  console.log(i, myElement, originalArray);
});

/*
La función de devolución de llamada que se usa con Map.forEach proporciona parámetros que contienen el valor asociado con el elemento actual, la clave asociada con este y el mapa en el que se invocó el método forEach
*/

const myMap = new Map([
  ['myKye', true],
  ['mySecondKey', false],
]);

myMap.forEach((myValue, myKey, originalMap) => {
  console.log(myValue, myKey, originalMap);
});

/*
Una devolución de llamada Set.forEach incluye parámetros similares. Debido a que Set no tiene índices ni claves distintos de los valores, el segundo argumento proporciona un valor redundante que se puede ignorar estrictamente para mantener la coherencia de la sintaxis con los otros métodos forEach.
*/

const mySet = new Set([true, false]);
mySet.forEach((myValue, myKey, originalSet) => {
  console.log(myValue, myKey, originalSet);
});

//Iteradores

/*
Un iterable es cualquier estructura de datos compuesta por elementos individuales que se pueden iterar con los enfoques detallados. Un iterador es un objeto iterable que sigue el protocolo iterador, lo que significa que debe implementar un método next() que avance por los elementos que contiene, uno a la vez, cada vez que se llama a ese método y muestre un objeto para cada elemento secuencial en un formato específico.
*/

const MY_ITERABLE = [1, 2, 3];
const MY_ITERADOR = MY_ITERABLE[Symbol.iterator]();

console.log(MY_ITERABLE);

console.log(MY_ITERADOR);

/*
Llamar al método next() en un iterador recorre los elementos que contiene, uno a la vez, y cada llamada muestra un objeto que contiene dos propiedades: value, que contiene el valor del elemento actual, y done, un valor booleano que indica si el iterador pasó el último elemento de la estructura de datos. El valor de done es true solo cuando una llamada a next() da como resultado un intento de acceso a un elemento más allá del último elemento del iterador.
*/

//JavaScript Asíncrono

/*
Promesas --> Una promesa es un marcador de posición para un valor que se desconoce cuando se crea la promesa. Es un contenedor que dicta una operación asíncrona, los términos por los cuales la operación se considera un éxito o un fracaso, las acciones se deben realizar en cualquier caso y el valor que se genera.
*/

console.log('Promesas');

const myPromise = new Promise(() => {
  const myResult = true;

  setTimeout(() => {
    if (myResult === true) {
      console.log('This promise was successful!');
    } else {
      reject(new Error('This promise has been rejected'));
    }
  }, 10000);
});

console.log(myPromise);

//ASYNC / AWAIT

/*
Async --> Cualquier valor que muestre esa función se muestra como una promesa cumplida que contiene ese valor. Esto permite ejecutar y administrar operaciones asíncronas con los mismos flujos de trabajo que el desarrollo síncrono.
*/

async function myFunction() {
  return 'This is my returned value';
}

myFunction()
  .then((myReturnValue) => {
    console.log(myReturnValue);
  })
  .catch((err) => {
    console.log(err);
  });

/*
Await --> Pausa la ejecución de una función asíncrona mientras se estable la promesa asociada. Una vez que se establece la promesa, el valor de la expresión 'await' es el valor cumplido o rechazado de la promesa.
*/

async function myFunction() {
  const myPromise = new Promise((fulfill, reject) => {
    setTimeout(() => fulfill('Successful. '), 5000);
  });
  const myPromisedResult = await myPromise;
  return myPromisedResult;
}

myFunction()
  .then((myResult) => console.log(myResult))
  .catch((myFailedResult) => console.error(myFailedResult));
