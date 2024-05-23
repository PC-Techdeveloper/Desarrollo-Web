/*
MÉTODOS DE CLASE:
Un método es el nombre que recibe una función que existe dentro de una clase. Se utilizan para englobar comportamientos o funcionalidades relacionadas en conjunto con la clase y mediante las cuales puede segmentar y separar en bloques de código.
*/

// .repeat(): Repite un string N cantidad de veces

const text = 'Manz ';
console.log(text.repeat(3));

/*
¿QUÉ ES UN MÉTODO?
Un método es cuando hace referencia a funciones que existen en el interior de una clase.
*/

// Ámbito global
function hablar() {
  return 'HOLA';
}

// En una clase -> Forma corta

class Animal {
  hablar() {
    return 'Primer cuak';
  }
}

const first = new Animal();
console.log(first.hablar());

// En una clase -> Forma larga
class OtroAnimal {
  hablar = function () {
    return 'Segundo cuak';
  };
}

const second = new OtroAnimal();
console.log(second.hablar());

/*
CONSTRUCTOR DE CLASE:
Se le llama constructor a un método de clase especial que se ejecutá automáticamente cuando se hace un 'new' de dicha clase al instanciar el objeto. Una clase SOLO PUEDE TENER UN CONSTRUCTOR, y en el caso de que no se específique un cosntructor a una clase, tendrá uno vacío de forma implícita.
*/

class MasAnimales {
  constructor() {
    console.log('Ha nacido un pato: 🦆');
  }

  hablar() {
    return 'Cuakk cuakk!';
  }
}

const pato = new MasAnimales();
console.log(pato.hablar());

/*
¿MÉTODOS ESTÁTICOS?
Crear métodos estáticos en una clase NO requieren crear una instancia, sino que se pueden ejecutar directamente sobre la clase.
*/

class TengoOtroAnimal {
  static {
    console.log('Adios ✌');
  }
  // Método público y privado (#)
  hablar() {
    console.log('Cuak otra vez!');
  }

  constructor() {
    console.log('Constructor ejecutado!');
  }
}
// Inicialización estática

const segundoPato = new TengoOtroAnimal();
