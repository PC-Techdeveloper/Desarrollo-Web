//FUNCIÓN CONSTRUCTORA
//Nombradas con la primer letra en mayúscula
//Solo se ejecutan con el operador 'new'
function User(name) {
  this.name = name;
  this.isAdmin = false;
}

let user = new User('Jackson');
console.log(user.name);
console.log(user.isAdmin);

//MÉTODOS EN CONSTRUCTOR
function UserTwo(name) {
  this.name = name;

  this.sayHi = function () {
    console.log('Mi nombre es: ' + this.name);
  };
}

let john = new UserTwo('John');
john.sayHi();
