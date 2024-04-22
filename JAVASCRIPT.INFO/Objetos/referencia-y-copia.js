/*
Los objetos son almacenados y copiados “por referencia”, en cambio los primitivos: strings, number, boolean, etc.; son asignados y copiados “como un valor completo”.
*/

//Primitivo como un string
//Una variable NO almacena el objeto mismo sino su 'dirección en memoria', una referencia.
let message = 'Hello!';
let phrase = message;

console.log(phrase);

//Así almacena en memoria
let user = {
  name: 'Miguel',
};
//Cuando una variable de objeto es copiada, se copia solo la referencia, el objeto NO ES DUPLICDO
let userTwo = { name: 'Ricardo' };
//Copia la referencia
let admin = userTwo;
//Acceder al objeto y modificar su contenido
//Cambiado por la referencia admin
admin.name = 'Pete';
//Cambios desde la referencia 'userTwo'
console.log(userTwo.name);

//COMPARACIÓN POR REFERENCIA
//Dos objetos son iguales solamente si son el mismo objeto
const a = {};
//Copia la referencia
const b = a;
console.log(a == b);
console.log(a === b);

//Objetos independientes que no son iguales
let one = {};
let two = {};
console.log(one === two);

//Objetos como referencias es que son declarado como const puede ser modificado
const myUser = {
  name: 'Pedro',
};
user.name = 'Adriana';
console.log(myUser.name);

//CLONACIÓN Y MEZCLA, Object.assign
let usuario = { name: 'Janer' };
let permissions1 = { canView: true };
let permissions2 = { canEdit: true };
//Copia todas las propiedades
Object.assign(usuario, permissions1, permissions2);
//Ahora user
console.log(usuario.name);
console.log(usuario.canView);
console.log(usuario.canEdit);
//Si la propiedad por copiar ya existe, se sobreescribe
let usuarioTwo = { name: 'Janer' };
Object.assign(usuarioTwo, { name: 'Pete' });
console.log(usuarioTwo.name);
//También podemos hacer una clonación simple
let info = {
  name: 'John',
  age: 30,
};
let clone = Object.assign({}, info);
console.log(clone.name);
console.log(clone.age);

//CLONACIÓN ANIDADA -> Las propiedades pueden ser referencias a otros objetos:
let secondInfo = {
  name: 'Pepito',
  age: 12,
  sizes: {
    altura: 1.82,
    anchura: 50,
  },
};
console.log(secondInfo.sizes.altura);

//STRUCTURECLONE -> Clona el object con todas sus propiedades anidadas
//Puede clonar la mayoría de los tipos de datos como objetos, arrays, valores primitivos...
//Las propiedades de function no están soportadas
let secondClone = structuredClone(secondInfo);
// No están relacionados
secondInfo.sizes.anchura = 60;
console.log(secondClone.sizes.anchura);

let thirdInfo = {};
//Referencia a si misma -> Referencia circular
thirdInfo.me = thirdInfo;
let thirdClone = structuredClone(thirdInfo);
console.log(thirdClone.me === thirdClone);
