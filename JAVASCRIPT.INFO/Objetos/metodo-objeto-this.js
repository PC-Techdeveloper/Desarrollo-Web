//Para acceder al objeto, un método puede usar la palabra clave 'THIS'
//Es usado para llamar al método
let user = {
  name: 'John',
  age: 30,
  //Método del objeto user
  sayHi() {
    console.log(this.name);
  },
};

user.sayHi();

//EL 'THIS' NO ES VINCULADO -> Puede ser usado en cualquier función
let secondUser = { name: 'Pedro' };
let thirdUser = { name: 'Admin' };

function sayHi() {
  console.log(this.name);
}

secondUser.f = sayHi;
thirdUser.f = sayHi;
//Estos llamados tienen diferentes 'this'
secondUser.f();
thirdUser.f();
thirdUser['f'];

//LAS FUNCIONES DE FLECHA NO TIENEN 'THIS'
//Será tomada desde afuera de la declaración de una función
let myUser = {
  firstName: 'Nina',
  sayHi() {
    let arrow = () => {
      console.log(this.firstName);
    };
    arrow();
  },
};

myUser.sayHi();
