/*
Los objetos en JavaScript son una colección de propiedades y métodos que definen un elemento a través de una clave y un valor
*/

//Declaración y asignación de objetos
const persona = {
  firstName: 'Dani',
  age: 36,
  isWorking: true,
};

/*
Las propiedades y métodos de un objeto puede ser de cualquier tipo de dato de JavaScript, incluso otros objetos o Arrays.
*/

const myPerson = {
  firstName: 'Miguel',
  age: 25,
  isWorking: false,
  family: ['Andrea', 'Felipe'],
  address: {
    street: 'Calle de la piruleta',
    number: 13,
    city: 'Barcelona',
  },
  //Method
  walk: function () {
    console.log('Estoy caminando...');
  },
};

// Acceder a las propiedades y métodos de un objeto con punto (.) o corchetes ([])
// Si una propiedad o método no existe, devolvera 'undefined'
const otraPersona = { 'full firstName': 'Johana Valencia' };
console.log(otraPersona['full firstName']);

console.log(myPerson.isWorking);
console.log(myPerson['address']['street']);

myPerson.walk();
myPerson['walk']();

// Añadir y modificar propiedades de un objeto
const user = { firstName: 'Roberto' };

// Moficando el objeto user
user.firstName = 'Alejandro';
console.log(user.firstName);

// Añadiendo la propiedad age
user.age = 25;
console.log(user);

// Eliminar propiedades de un objeto -> Usar la palabra reservada delete
delete user.age;
console.log(user);

let firstName = 'Jefferson';
let userName = 'Chavez Diaz';

const myUser = {
  firstName: firstName,
  userName: userName,
};

console.log(myUser);
