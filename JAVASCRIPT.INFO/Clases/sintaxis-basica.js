//Programación orientada a objetos -> POO
//Sintaxis básica 'class'
class MyClass {
  //Métodos de clase
  constructor() {}
  method1() {}
  method2() {}
  method3() {}
}

//El método constructor() es llamado por 'new' para inicializar el objeto
class User {
  constructor(name) {
    this.name = name;
  }
  sayHi() {
    console.log(this.name);
  }
}

let user = new User('John');
user.sayHi();
//Una clase es una función
console.log(typeof User);

//EXPRESIÓN DE CLASES -> Con nombres
let UserTwo = class MyClassTwo {
  sayHi() {
    console.log(MyClassTwo);
  }
};

//Muestra la definición de MyClassTwo
new UserTwo().sayHi();

//Getters/Setters en las clases
class UserThree {
  constructor(name) {
    // invoca el setter
    this.name = name;
  }

  get name() {
    return this._name;
  }

  set name(value) {
    if (value.length < 4) {
      console.log('Nombre demasiado corto.');
      return;
    }
    this._name = value;
  }
}

let userTwo = new UserThree('John');
console.log(user.name);

user = new User('');
