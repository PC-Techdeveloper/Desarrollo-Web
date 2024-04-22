/*
Los operadores de comparación comparan los valores de dos operandos y evalúan si la declaración que forman es 'true' o 'false'.
*/

console.log(2 + 2 === 4);

/*
Coerción e igualdad de tipos --> Dos de los operadoes de comparación más usados son (==) para la igualdad baja y (===) para la igualdad estricta. Realizan una comparación general entre dos valores mediante la coerción de los operandos para que coincidan con los tipos de datos, si es posible.
*/

console.log(2 == 2);

console.log('2' == 2);

/*
Lo mismo sucede con (!=), que muestra 'true' solo si los operandos que se comparan no son iguales de manera general.
*/

console.log(2 != 3);

console.log(2 != '2');

/*
las comparaciones estrictas con (===) o (!==) no realizan coerción de tipos. Para que una comparación estricta evalúe como 'true', los valores que se comparan deben tener el mismo tipo de dato.
*/

console.log(2 === 3);

console.log(2 === '2');

/*
Operadores de comparación:

Estrictamente igual -> ===
Estrictamente diferente que -> !==
Igual -> ==
Mayor que -> > 
Mayor o igual que -> >=
Menor que ->  <
Menor o igual que -> <=
*/

/*
Truthy and Falsy: 
Todos los valores en JavaScript son 'true' o 'false' de manera implícita, y se pueden forzar el valor booleano correspondiente. Un conjunto limitado de valores se fuerza a false.

0, null, undefined, NaN, ''.

Todos los demás valores se convierten en 'true', incluida cualquier string que contenga uno o más carácteres y todos los números que no sean cero (0). A esto se le denomina valores 'de verdad' y 'falsidad'.
*/

console.log('My string' == true);

console.log(100 == true);

console.log(0 == true);

/*
Operadores Lógicos:
Los operadores lógicos AND (&&), OR (||) y NOT (!) controlan el flujo de secuencia de comandos en función de la evaluación de dos o más sentencias condicionales.
*/

console.log(2 === 3 || 5 === 5);

console.log(2 === 2 && 2 === '2');

console.log(2 === 2 && !'My string');

/*
Una expresión lógica NOT (!) niega el valor truthy o falsy de un operando y evalúa a 'true' si el operando se evalúa como 'false' y 'false' si el operando se evalúa como 'true'.
*/

console.log(true);

console.log(!true);

console.log(!false);

//Dos operadoes NOT es una práctica común forzar los datos a su valor booleano coincidente.
console.log(!!'string');
console.log(!!0);

//Lógica del operador AND -> && -> Si uno es false, retorna false

console.log(false && true);
console.log(true && false);
console.log(true && true);
console.log(false && false);

//Lógica del operador OR -> || -> Si uno es true, retorna true
console.log(false || true);
console.log(true || false);
console.log(true || true);
console.log(false || false);

//Operador coalescente nulo o opcional

/*
Muestra el primer operando solo si ese operando tiene algún valor distinto de null o undefined. De lo contrario, muestra el segundo operando.
*/

console.log(null ?? 'My string');
console.log(undefined ?? 'My string');
console.log(true ?? 'My string');
console.log(0 ?? 'My string');
console.log(false ?? 'My string');

//Operadores lógicos de asignación:

/*
Los operadores de asignación permiten asignar el valor de un segundo operador a un primer operador. El signo (=) se usa para asignar un valor a una variable declarada.

Usar operadores de asignación lógica para asignar condicionalmente un valor a una variable según el valor truthy o falsy de esa variable. 

El operador de asignación && lógico evalúa el segundo operando y lo asigna al primer operando si el primer operando se evaluaría como 'true'. Si el primer operando es verdadeo, se asigna el valor del segundo operando.

El operador de asignación || lógico evalúa el segundo operando y lo asigna al primer operando si el primero se evalúa como 'false'. Si el primer operando es falso, se asigna el valor del segundo operando. 
*/

// &&
let myVariable = false;

console.log((myVariable &&= 2 + 2));

let myVariable2 = true;

console.log((myVariable2 &&= 2 + 2));

// ||
let myVariable3 = false;
console.log((myVariable3 ||= 2 + 2));

let myVariable4 = true;
console.log((myVariable4 ||= 2 + 2));
