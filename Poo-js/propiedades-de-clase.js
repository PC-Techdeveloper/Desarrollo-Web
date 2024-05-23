/*
¿QUÉ ES UNA PROPIEDAD DE CLASE?
Las clases, siendo estructuras para guardar y almacenar información, tienen unas variables que viven dentro de la clase. Se denomina propiedad o propiedad de clase.
*/

class Personaje {
  name; // Sin definir
  type = 'Player'; // Definida
  lifes = 5; // Definida
  energy = 10; // Definida

  constructor(name) {
    this.name = name;
    console.log(`!Bienvenido/a, ${this.name}!`);
  }
}

const mario = new Personaje('Mario');

/*
PROPIEDADES PÚBLICAS:
Siempre permite acceder y modificar a las propiedades desde el constructor u otros métodos dentro de la clase, ya sean propiedades públicas o privadas.
*/

class SegundoPersonaje {
  name;
  energy = 10;

  constructor(name) {
    this.name = name;
  }
}

const personaje1 = new SegundoPersonaje('Luigi');
console.log(personaje1.name);
console.log((personaje1.name = 'Evil Mario'));
console.log(personaje1.name);

/*
CLASES PRIVADAS:
Existe la posibilidad de crear propieades de clase privadas. Si se añade el carácter # justo antes del nombre de la propiedad, se tratará de una 'propiedad privada'
*/

class TercerPersonaje {
  #name;
  energy = 15;

  constructor(name) {
    this.#name = name;
  }
}
const personaje2 = new TercerPersonaje('Mario Bros');
// Muestra 'undefined'
// Se puede acceder desde métodos en las propiedades privadas
console.log(personaje2.name);
// ERROR ❌
// console.log(personaje2.#name);

/*
ÁMBITOS DE PROPIEDADES DE CLASe: Si se declara propiedades dentro de un método con let o const, estos elementos existirán sólo en el método en cuestión. Además, no serán accesibles desde fuera del método.
*/

// ÁMBITO DENTRO DE UN MÉTODO
class cuartoPersonaje {
  constructor() {
    const name = 'Manz Dev';
    console.log('Constructor:' + name);
  }

  // Método
  method(name) {
    console.log('Método: ' + name);
  }
}

const c = new cuartoPersonaje();
// Undefined
c.name;
// Método
c.method('Maria');

/*
ÁMBITO DE CLASEs: Las propiedades tendrán alcance en toda la clase, por lo que podemos acceder a ellas tanto desde el constructor, como desde otros métodos de la clase.
*/

// ÁMBITO DE CLASES
class quintoPersonaje {
  // ES2020+
  name = 'Manz';

  constructor() {
    // ES2015+
    this.name = 'Manz';
    console.log('Constructor: ' + this.name);
  }

  metodo() {
    console.log('Método: ' + this.name);
  }
}

const nombre = new quintoPersonaje();
nombre.name;
nombre.metodo();

// PROPIEDADES COMPUTADAS: Los getters y setters

/*
PROPIEDADES GET (GETTERS):
Añadde la palabra clave 'get' antes del nombre de la función. De resto, se define exactamente igual que una función
*/

class MyPersonaje {
  constructor(name, energy = 10) {
    this.name = name;
    this.energy = energy;
  }

  get status() {
    return '⭐'.repeat(this.energy);
  }
}

const personaje3 = new MyPersonaje('Mario');
console.log(personaje3.energy);
console.log(personaje3.status);

/*
PROPIEDADES SET (SETTERS):
La propiedad set permite modificar el valor.
*/

class My_Personaje {
  name;
  energy;

  constructor(name, energy = 10) {
    this.name = name;
    this.energy = energy;
  }

  get status() {
    return '⭐'.repeat(this.energy);
  }

  set status(stars) {
    this.energy = stars.length;
  }
}

const personaje4 = new My_Personaje('Luigi');
console.log(personaje4.energy);
console.log((personaje4.status = '⭐⭐⭐'));
console.log(personaje4.energy);
console.log(personaje4.status);
