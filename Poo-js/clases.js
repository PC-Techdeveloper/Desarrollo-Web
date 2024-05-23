/*
¿QUÉ ES UNA CLASE?
La clase es el concepto abstracto de un objeto, mientras que el objeto es el elemento final que se basa en la clase.

INSTANCIAR UNA CLASe:
Se le llama instanciar una clase, crear un objeto o crear una instancia a la acción de crear un nuevo objeto basado en una clase particular. 
Esta acción se realiza a través de la plabra clave 'new', seguida del nombre de la clase, la cuál puede tener párametrosm en cuyo caso se controlarían desde un 'constructor'.
*/

// Declaración de una clase
class Animal {
  //Propiedades
  name = 'Garfield';
  type = 'Cat';

  // Métodos
  hablar() {
    return 'Odio los lunes!';
  }
}

class SegundoAnimal {}
// Instanciando la clase -> Objeto
const pato = new SegundoAnimal();

/*
MIEMBROS DE UNA CLASE:
Las propiedades: A grandes rasgos, variables dentro de clases.
Los métodos: A grandes rasgos, funciones dentro de clases.
*/

class Coche {
  // Propiedades
  marca = 'Chevrolet';
  año = 2020;
  // Método
  moverse() {
    return 'El coche se esta moviendo!';
  }
}

/*
LA PALABRA CLAVE THIS:
Se utiliza mucho dentro de las clases para hacer referencia al OBJETO INSTANCIADO, y no a la clase.
*/

class TercerAnimal {
  // Propiedad sin valor
  name;

  // Hace referencia a la propiedad de la clase
  constructor(name) {
    this.name = name;
  }
}

/*
CLASES EN FICHEROS EXTERNOS:

Fichero -> Animal.js:
export class Animal {
  // Contenido de la clase
}

CREAR OBJETOS BASADOS EN LA CLASE IMPORTANDO EL FICHERO DE LA CLASE:

Fichero -> index.js
import { Animal } from './Animal.js'

const pato = new Animal();
*/
