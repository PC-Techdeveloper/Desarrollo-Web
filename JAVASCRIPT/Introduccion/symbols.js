/*
Es un tipo de dato primitivo introducida en ES6. Una primitiva de symbol representa un valor único que nunca choca con ningún otro valor. Dos primitivas de strings formadas por carácteres idénticos se evalúan como estrictamente iguales.
*/

console.log(String() === String());

//Creados con la función symbol() nunca pueden ser estrictamente iguales.
console.log(Symbol() === Symbol());

/*
Este rango permite usar símbolos como claves de propiedad únicas en un objeto, evitando colisiones con claves que cualquier otro código podría agregar a ese obj
*/

const mySymbol = Symbol('Dese');

console.log(mySymbol);

/*
Hay 3 tipos de symbols:
1. Creados con symbol().
2. Symbols compartidos que se configuran y recuperan de un registro de símbolos globales usando symbol.for().
3. Symbols conocidos definidos como propiedades estáticas en el objeto symbol(). Estos symbols contienen métodos internos que no se pueden sobreescribir accidentalmente.

Symbol() acepta una descripción (o 'nombre de símbolo') como argumento opciona. Cualquier llamada a symbol devuelve un símbolo primitivo completamente único, incluso si varias llamadas tienen descripciones idénticas.
*/

console.log(Symbol('My symbol.') === Symbol('My symbol.'));
const ID = Symbol('id');

/*Se puede acceder a una descripción como propiedad heredada del símbolo creado*/

let mySymbol2 = Symbol('My symbol.');

console.log(mySymbol2.description);

//❌ No se puede crear un symbol usando la palabra clave 'new'

/*El getOwnPropertySymbols() método da acceso a las propiedades del símbolo de un objeto.*/

// let mySymbol3 = new Symbol() --> ❌

//Symbols compartidos
/*
El symbol.for() es un método que intenta buscar cualquer simbolo existente en un registro de símbolos globales en tiempo de ejecución con una cadena determinada como clave y devuelve el símbolo coincidente si se encuentra uno. Si no encuentra ninguno, crea un símbolo con la clave específicada y lo agrega al registro global.
*/

//Acceder a un símbolo en el registro de símbolos, primero crearlo usando for().

//Para recuperar la clave de cualquier símbolo del registro de símbolos, se utiliza Symbol.keyFor():

//Símbolos conocidos

/*
Los símbolos conocidos son propiedades estáticas del Symbol objeto, cada una de las cuales es un símbolo en sí mismo. Los símbolos conocidos proporcionan claves de propiedad únicas para acceder y modificar los métodos integrados de JavaScript, al tiempo que evitan que el comportamiento principal se sobrescriba involuntariamente.
*/
