/*
Los objetos son usados para almacenar colecciones de varios datos y entidades más complejas asociadas con un nombre clave.
*/

//Sintaxis de 'constructor de objetos'
const userOne = new Object();
//Sintaxis de 'objeto literal'
const userTwo = {};

//Literales y propiedades
//Nombrar propiedades entre comillas
let user = {
  name: 'John',
  age: 30,
  //Las claves con más de una palabra deben ir entre comillas
  'likes birds': true,
};

//Podemos agregar, eliminar y leer archivos
//Acceder a los valores de las propiedades con la notación de puntos:
console.log(user.name);
console.log(user.age);
//Se puede agregar un nuevo valor:
user.isAdmin = true;
console.log(user.isAdmin);
console.log(user);
//Para eliminar una propiedad usar el operador delete:
delete user.age;
console.log(user);

//Notación de corchetes -> Permite acceder a propiedades con claves de más de una palabra:
let myUserTwo = {};
//Asignando
myUserTwo['likes birds'] = true;
//Obteniendo
console.log(myUserTwo['likes birds']);
//Eliminando
delete myUserTwo['likes birds'];
console.log(myUserTwo);

//También brindan una forma de obtener el nombre de la propiedad desde el resultado de una expresión
let key = 'likes birds';
user[key] = true;
console.log(key);

//Ejemplo
let myUserThree = {
  name: 'Maria',
  age: 35,
};

//Propiedades calculadas -> Usar corchetes en un objeto literal al crear un objeto
// let fruit = prompt('Qué fruta comprar?', 'Manzana');

// let bag = {};
// bag[fruit] = 5;

//Atajo para valores de propiedad -> Variables existentes como valores de los nombres de propiedades:
function makerUser(name, age) {
  return {
    name,
    age,
  };
}

//La prueba de propiedad existente, Operador IN
//La lectura de una propiedad no existente solo devuleve 'undefined':
let secondUser = {};
console.log(secondUser.noSuchProperty === undefined);

//Operador especial 'IN'
let thirdUser = { name: 'Roberto', age: 35 };
console.log('name' in thirdUser);
console.log('country' in thirdUser);

//Bucle 'for..in'

//Para recorrer todas las claves de un objeto.

const myUser = {
  name: 'John',
  age: 30,
  isAdmin: true,
};

for (let key in myUser) {
  //Claves
  console.log(key);
  //Valores de las claves
  console.log(myUser[key]);
}

//Ordenando un objeto
let codes = {
  '+49': 'Germany',
  '+41': 'Switzerland',
  '+44': 'Great Britain',
  '+1': 'USA',
};

for (let code in codes) {
  console.log(code);
}
