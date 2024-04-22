//Operador nullish coalescing -> ??
// El operador nullish devuelve el primer argumento cuando esto no es null ni undefined, en caso contrario, devuelve el segundo:

let user;
console.log(user ?? 'Anonymous');

//Con un nombre asignado:
let secondUser = 'John';
console.log(secondUser ?? 'Anonymous');

//Seleccionar el primer valor que no sea null/undefined de una lista
let firstName = null;
let lastName = null;
let nickName = 'Supercoder';
//Devuelve el primer valor definido
console.log(firstName ?? lastName ?? nickName);

//Comparación con || <-- PENDIENTE
let myName = null;
let myLastName = null;
let myNickName = 'Superman';
//Devuelve el primer valor verdadero
console.log(myName || myLastName || myNickName);

//Cuando el valor realmente es desconocido o no fue establecido:
let height = 0;
console.log(height || 100);
console.log(height ?? 0);

//Uso de ?? con && y ||
let x = (1 && 2) ?? 3;
console.log(x);