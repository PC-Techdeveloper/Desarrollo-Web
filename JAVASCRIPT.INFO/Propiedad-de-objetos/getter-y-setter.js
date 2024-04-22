//PROPIEDADES DE ACCESO:
//getter -> Obtener valores
//setter -> Asignar o modificar valores

let user = {
  name: 'John',
  surname: 'Smith',
  //Obtener el valor
  get fullName() {
    return `${this.name} ${this.surname}`;
  },
  //Asignar el valor o modificarlo
  set fullName(value) {
    [this.name, this.surname] = value.split(' ');
  },
};

console.log(user.fullName);
//Set se ejecuta con valor dado -> Set se comporta como una propiedad
user.fullName = 'Alice Cooper';

console.log(user.name);
console.log(user.surname);

//Getter y setter más inteligentes -> Más control sobre ellos.
let userTwo = {
  get name() {
    return this._name;
  },

  set name(value) {
    if (value.length < 4) {
      console.log(
        'El nombre es demasiado corto, necesita al menos 4 caracteres'
      );
      return;
    }
    this._name = value;
  },
};

user.name = 'jeff';
console.log(user.name);
