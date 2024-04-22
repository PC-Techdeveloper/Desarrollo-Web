//Spread operator -> Expandir los arrays y los objetos

let firstArray = [1, 2, 3];
let secondArray = [4, 5, 6];

//Copiar arrays
const firstArrayCopy = [...firstArray];

const thirdArray = [...firstArray, ...secondArray];

console.log(thirdArray);
console.log(firstArrayCopy);

const firstObject = { name: 'Pedro' };
const secondObject = { lastName: 'Plasencia' };

//Copiar objetos
const firstObjectCopy = { ...firstObject };

console.log(firstObjectCopy);

const thirdObject = { ...firstObject, ...secondObject };

console.log(thirdObject);

//Rest Operator -> In parameters of function -> transform to array
const myFunction = (data1, ...data) => {
  console.log(data);
  console.log(data1);
};

myFunction(1, 2, 3);

//Destructuring: arrays & objects

const myArray = [1, 2, 3];
//Saltarse un valor con ,
//Definir valores por defecto, si uno no existe retorna undefined
const [a, b, c, d] = myArray;

console.log(a, b, c, d);

//Destructuring: Object
const myObject = { firstName: 'Pedro', lastName: 'Plasencia' };
//Modificar
//Propiedades por defecto
const {
  firstName: nombre,
  lastName: apellido,
  direccion = 'Prueba',
} = myObject;

console.log(nombre, apellido, direccion);
