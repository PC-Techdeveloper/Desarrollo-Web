/*
Las variables son una estructura de datos que asigna un nombre representativo a un valor. Pueden contener datos de cualquier tipo. El nombre de una variable se llama 'identificador'.

REGLAS: 
1. Pueden contener letras Unicode, signos de dólar, carácteres de subrayado, dígitos.
2. Los identificadores no pueden contener espacios en blanco.
3. Los identificadores deben comenzar con una letra, un guión bajo o un signo de dólar.
4. No pueden empezar con dígitos, para evitar confusiones entre números e identificadores.
5. No pueden contener carácteres especiales (! . , / \ + - + =)
*/

//Nomenclatura de variables

//camelCase
let camelCaseIdentifier = true;

//snake_case
let snake_case = false;

//SCREAMING_CASE -> Para crear variables constantes.
const SCREAMING_CASE = 3.14;

//Nombres para crear clases en JavaScript
// class MyClass {}

//Declaración de variables --> let (✅), const (✅) y var (❌)

//let --> Permite reasignar nuevos valores y no pueden tener el mismo nombre -> ❌ Error de sintaxis.
let myVariable = 5;
myVariable = 10;
console.log(myVariable + myVariable);

//Declarar una variable let sin inicializar.
let myVariable2;
myVariable2 = 30;
console.log(myVariable2);

//const --> Variables únicas que no pueden ser modificadas, son fijas.
const MY_CONSTANT = true;

//❌ No se puede declarar una constante sin asignarle un valor inmediatamente.
//const myConstant --> ❌

//Cuando una constante está asociada a un objeto, SI pueden modificarse, agregar o eliminar.
const CONSTANT_OBJECT = {
  firstValue: true,
  secondValue: false,
};

console.log(CONSTANT_OBJECT);

// ❌ CONSTANT_OBJECT = false;

/*
SCOPE: 
El alcance de una variable es la parte de una secuencia de comandos en la que esa variable está disponible. Fuera del alcance de una variable, no se definirá, no como un identificador que contenga un valor undefined, sino como si no se hubiera declarado.

Según la palabra clave que uses para declarar una variable y el contexto en el que la defines, puedes definir el alcance de las variables para sentencias de bloqueo (alcance de bloque), funciones individuales (alcance de función) o toda la aplicación de JavaScript (alcance global).
*/
