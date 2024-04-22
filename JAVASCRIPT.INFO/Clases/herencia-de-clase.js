//La herencia de clases es el modo para que una clase herede de otra o se extienda
//De esta manera podemos añadir nuevas funcionalidades a la que ya existe
class Animal {
  constructor(name) {
    this.speed = 0;
    this.name = name;
  }
  run(speed) {
    this.speed = speed;
    console.log(`${this.name} corre a una velocidad de ${this.speed}Km/h`);
  }
  stop() {
    this.speed = 0;
    console.log(`${this.name} se queda quieto!`);
  }
}

let animal = new Animal('Mi animal');
animal.stop();

//Clase (Rabbit) que hereda de la clase padre (Animal) ->
class Rabbit extends Animal {
  hide() {
    console.log(`${this.name} se esonconde!`);
  }
}
let rabbit = new Rabbit('Conejo Blanco');
rabbit.run(5);
rabbit.hide();
