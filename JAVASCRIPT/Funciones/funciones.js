/*
Una función es un bloque modular y reutilizable de sentencias que se usa para realizar un conjunto de tareas relacionadas, como calcular y mostrar un valor según los argumentos proporcionados a la función. Las funciones son objetos. Son objetos únicos porque se les puede llamar para ejecutar código, pasar datos en forma de argumentos y retornar un valor.

Una función puede asignarse a una variable, pasarse como argumento a otras funciones y ser devuelta por otras funciones. Las declaraciones usan el comportamiento de alcance heredado de JavaScript, lo que significa que tiene alcance en función de la función contenedora más cercana.
*/

//Declaración de función
function myFunction() {
  console.log('This is my function!');
}

myFunction(); //LLamada a la función

//Función por parámetros por defecto
function myFunction(myParameter = 'omitted') {
  console.log(`The value is: ${myParameter}`);
}

//Función por parámetro y argumentos
function myFunction(a, b) {
  return `La suma es: ${a + b}`;
}

//Argumentos
console.log(myFunction(4, 4));

//Expresiones de función

/*
Usar expresiones de función para crear funciones anónimas omitiendo el identificador y siguiendo la palabra clave 'function' con un par de paréntesis que contengan parámetros opcionales.
*/

const myVariable = function () {
  console.log('Soy una expresión de función!');
};

myVariable();

/*
También se puede usar expresiones de funciones con nombre mediante una sintaxis similar a las declaraciones de funciones.
*/

const mySecondVariable = function myFunction() {
  console.log('This is my second function');
};

mySecondVariable();

console.log(typeof mySecondVariable);

//Expresiones de funciones tipo flecha

const myArrowFunction = () => 2 + 2;

console.log(myArrowFunction());

//La palabra clave 'new' --> Permite la creación de objetos.

function myFunction() {
  //Encapsulamiento
  this.myProperty = 10;
}

const myObject = new myFunction();

console.log(myObject.myProperty);

//La palabra clave 'return' --> Específica el valor que la función debe producir como resultado final.

const myFunction3 = function () {
  return 2 + 2;
};

console.log(myFunction3());

function myFunction4(myString) {
  if (typeof myString !== 'string') {
    return false;
  }
  if (myString.length >= 5) {
    return true;
  } else {
    return false;
  }
}

console.log(myFunction4('string'));

//La palabra clave 'this'

/*
Hace referencia al contexto de ejecución actual de una función, lo que significa que su valor es diferente según si se llama a la función como método, como función independiente o como constructor. Al igual que una constante, this no se puede quitar y su valor no se puede reasignar, pero los métodos y las propiedades del objeto que contiene la palabra clave this se pueden modificar.

Cuando se usa el modo estricto, this tiene un valor de undefined dentro de una función independiente
*/

//Vinculación global
(function () {
  'use strict';
  console.log(this);
})();

//Vinculación implícita

/*
Cuando se llama a una función como método de un objeto, una instancia de this dentro de ese método hace referencia al objeto que lo contiene, lo que otorga acceso a los métodos y las propiedades que se encuentran a su lado
*/
let myObject2 = {
  myValue: 'This is my string.',
  myMethod() {
    console.log(this.myValue);
  },
};

console.log(myObject2);

//this en funciones flecha

/*
En las funciones de flecha, this se resuelve en una vinculación en un entorno que lo encierra léxicamente. Esto significa que this en una función de flecha hace referencia al valor de this en el contexto envolvente más cercano de esa función:
*/

let myObject3 = {
  myMethod() {
    console.log(this);
  },
  myArrowFunction: () => console.log(this),
  myEnclosingMethod: function () {
    this.myArrowFunction = () => {
      console.log(this);
    };
  },
};

console.log(myObject3);
