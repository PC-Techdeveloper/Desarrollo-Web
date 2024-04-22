//Export antes de las sentencias:

//Exportar un array:
export let month = [
  'Jan',
  'Feb',
  'Mar',
  'Apr',
  'Aug',
  'Sep',
  'Oct',
  'Nov',
  'Dec',
];

//Exportar una constante:
export const MODULES_BECAME_STANDARD_YEAR = 2024;

//Exportar una clase:
export class User {
  constructor(name) {
    this.name = name;
  }
}

//Variables exportadas
export { sayHi, sayBye };

//Exportar separado de la declaración o arriba de las funciones:
function sayHi(user) {
  alert(`Hello, ${user}`);
}

function sayBye(user) {
  alert(`Bye, ${user}`);
}

//Import
//Primera versión -> Importar con una lista
import { sayHi, sayBye } from './say.js';
sayHi('John');
sayBye('John');

//Segunda versión -> Importar todo
import * as say from './say.js';

say.sayHi('Maria');
say.sayBye('Maria');

//Import 'as' -> Importar bajo nombres diferentes
import { sayHi as hi, sayBye as bye } from './say.js';
hi('Ricardo');
bye('Ricardo');

//Export 'as' -> Exportando funciones
export { sayHi as hi, sayBye as bye };
