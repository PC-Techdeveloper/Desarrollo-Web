/*
Una colección indexada es una estructura de datos en la que los elementos se almacenan y se accede a ellos mediante indices numerados. A los valores almacenados en una colección indexada se les asignan índices numerados a partir de 0.
*/

//Array

/*
Un array es un contenedor que puede contener cero o más valores de cualquier tipo de datos, incluidos otro arrays o objetos complejos.
*/

const myArray = [];

const myArray2 = new Array(10);

const myArray3 = [true, null, 'String', false];

console.log(myArray2);

console.log(myArray3);

//Longitud total del arreglo

console.log(myArray3.length);

//Acceso a los valores del array

console.log(myArray3[2]);

//Modificar valores del array

myArray3[0] = 20;
console.log(myArray3);

//Desestructuración de una asignación en arrays

/*
La desestructuración de la asignación es una manera concisa de extraer un rango de valores de arreglos u objetos y asignarlos a un conjunto de identificadores, un proceso que a veces se denomina “desempaquetar” la estructura de datos original, aunque no modifica el objeto ni el arreglo original.

La asignación de desestructuración usa una lista de identificadores similar a un objeto o arreglo para realizar un seguimiento de los valores. En su forma más simple, llamada desestructuración de patrón de vinculación, cada valor se descomprime del arreglo o el objeto y se asigna a una variable correspondiente, que se inicializa mediante let o const (o var):
*/

//Desempaquetado de arrays

const myArray4 = ['A string', 'A second string'];

const [myFirstElement, mySecondElement] = myArray4;

console.log(myFirstElement);
console.log(mySecondElement);

//Para omitir elementos, se puede omitir un identificaor.

const myArray5 = [1, 2, 3];
const [firstValue1, , secondValue2] = myArray5;

console.log(secondValue2);

//Desempaquetado de objetos

const myObject = { firstValue: 1, secondValue: 2, thirdValue: 3 };

const { secondValue, thirdValue, firstValue } = myObject;

console.log(firstValue);
console.log(secondValue);
console.log(thirdValue);

//Spread operator -> Se usa principalmente para copiar y combinar arrays

const miColeccion = [4, 5, 6];
const miColeccion2 = [1, 2, 3, ...miColeccion];

console.log(...miColeccion2);

/*
En el caso de los arrays y strings, la sintaxis de distribución solo se aplica cuando se esperan cero o más argumentos en una llamada a función o cuando se esperan elementos de un array. 
*/

//Copiar un array si extiende el array original en un literal de array

const miColeccion3 = [1, 2, 3];
const spreadArray = [...miColeccion3];

console.log(spreadArray);

/*
Combinar los elementos que conforman dos o más arrays en uno solo.
*/

const myArray6 = [1, 2, 3];
const mySecondArray = [4, 5, 6];
const myNewArray = [...myArray6, ...mySecondArray];

console.log(myNewArray);

/*
Pasar elementos de un array como argumentos individuales en un allamada a función.
*/

const myArray7 = [true, false];
const myFunction = (myArgument, mySecondArgument) => {
  console.log(myArgument, mySecondArgument);
};

myFunction(...myArray7);

/*
El operador spread permite duplicar o combinar objetos.
*/

const myObj = { myProperty: true };
const mySecondObj = { ...myObj };

console.log(mySecondObj);

const myFirstObject = { myProperty: true };
const mySecondObject = { additionalProperty: true };
const myMergedObject = { ...myFirstObject, ...mySecondObject };

console.log(myMergedObject);

//Rest operator

/*
El operador de resto combina elementos en una estructura de datos iterable. El nombre proviene del hecho de que se usa para recopilar "el resto" de un conjunto de valores de datos. 

Cuando se usa con la asignación de destructuración, la sintaxis se denomina sintaxis 'propiedad rest'.
*/

const array = ['first', 'second', 'third', 'fourth', 'fifth'];

[primerElemento, segundoElemento, ...remainingElements] = array;

console.log(remainingElements);

//Colecciones con clave

/*
Permite almacenar pares clave - valor y arreglos para almacenar colecciones de valores iterables, asignación para pares clave - valor y configuración para valores individuales.
*/

//Map

/*
Un mapa es una estructura de datos iterable que almacena información como pares clave- valor, similar a un literal de objeto. A diferencia de los literalees de objetos, un mapa permite que los valores y las claves tengan cualquier tipo de datos, y los elementos de orden que se agregan a un mapa se conservan cuando se itera sobre el.

Para crear un mapa, se usa el constructor Map().
*/

const myMap = new Map([
  ['myKey', 'A string value'],
  ['mySecondKey', 500],
  ['myThirdKey', true],
]);

console.log(myMap);

/*
Un objeto Map difiere de un literal de objeto en que tanto los valores y las claves pueden tomar cualquier tipo de datos y valor.
*/

const notAFunction = () => {
  console.log('function');
};

const myMap2 = new Map([
  [null, 0],
  [false, 'this is false'],
  [undefined, 'No defined value'],
  [NaN, 'Not a number'],
]);

console.log(myMap2);

/*
Para obtener, configurar o borrar elementos de Map, se usa los métodos heredados del constructor Map().
*/

/*
const myMap3 = new Map();

myMap3.set('miKey', 'My value');

myMap3.has('miKey');

myMap3.get('miKey');

myMap3.delete('miKey');

console.log(myMap3);
*/

/*
Las claves de un mapa son únicas, lo que significa que, cuando se configura una clave idéntica, se reemplaza el par clave - valor almacenado con anterioridad.
*/

const myMap4 = new Map([['myKey', 'A string value']]);

myMap4.set('myKey', 500);

console.log(myMap4);

/*
Al igual que con los objetos, permiten asignar un mapa a una variable declarada con const y, luego, modificar ese mapa. Sin embargo, al igual que con otros casos de uso de const, no permite modificar ni borrar la variable en sí.
*/

const myMap5 = new Map();

myMap5.set('myKey', 'A string value');

console.log(myMap5);

/* WeakMap -> Un WeakMap es un mapa que contiene references 'debiles' que deben ser referencias a objetos o símbolos que no se hayan agregado al registro global de símbolos. Para crear un WeakMap se usa el constructor WeakMap().
 */

const myWeakMap = new WeakMap();

console.log(myWeakMap);

// Set

/*
Un set es una colección iterable de valores únicos similar a un array, aunque un conjunto solo puede contener valores únicos. Al igual que con un mapa, la iteración sobre un conjunto conserva los elementos de orden que se le agregaron, para crear un conjunto se usa el constructor Set().
*/

const mySet = new Set();

/* Puede construir un conjunto a partir de un literal de arreglo:
 */

const mySet2 = new Set([1, 2, 3]);

mySet2.add(5);

console.log(mySet2);

/* Para agregar o quitar elementos de un conjunto, se usa los métodos heredados del constructor Set(). Estos métodos actúan sobre un elemento según el valor de este, en lugar de hacer referencia a un índice.
 */

const mySet3 = new Set();

mySet3.add('My value');

console.log(mySet3);

mySet3.delete('My value');

console.log(mySet3);

/*Para crear un array a partir de un conjunto,  se usa el método Array.from() o la sintaxis de distribución*/

const mySet4 = new Set([1, 2, 3]);
const MY_ARRAY = Array.from(mySet4);

console.log(MY_ARRAY);

console.log([...mySet4]);

//WeakSet

/* WeakSet es un conjunto que contiene solo valores recolectables de elementos no utilizados, como referencias a objetos o símbolos que no se agregaron al registro de símbolo global. Para crear un WeakSet se usa el constructor WeakSeat().
 */

const myWeakSet = new WeakSet();

console.log(myWeakSet);

/* Esto permite casos de uso, como la agregación de una sola colección iterable de objetos relacionados. Si no existen otras referencias a un objeto al que hace referencia el WeakSet, el elemento asociado también se quita del WeakSet.
 */
