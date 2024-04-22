//Programación orientado a objetos

/*
Clase -> Un modelo o plantilla para crear objetos que define sus propiedades y comportamientos.

Herencia -> El proceso mediante el cual una clase puede heredar propiedades y métodos de otra clase.

Encapsulamiento -> El concepto de ocultar los detalles internos de un objeto y exponer solo las operaciones públicas.

Polimorfismo -> La capacidad de diferentes objetos de una misma jerarquía de clases para responder al mismo mensaje de manera diferente.

Abstracción -> La simplificación de un objeto o concepto para enfocarse en sus caracteríticas esenciales.

Modularidad -> La división de un programa en módulos independientes que pueden ser desarrollados, probados y mantenidos por separado.

Objeto -> Una instancia de una clase que tiene propiedades y métodos específicos.
*/

//Creando una clase
class Animal {
  constructor(especie, edad, color) {
    this.especie = especie;
    this.edad = edad;
    this.color = color;
    //Atributo
    this.info = `${this.especie}, tengo ${this.edad} años y soy de color ${this.color}`;
  }
  //Métodos -> Acciones
  ladrar() {
    if (this.especie === 'perro') {
      document.write('WAW!');
    } else {
      document.write(`No puede ladrar ya que es un ${this.especie}`);
    }
  }
  verInfo() {
    document.write(`${this.info} </br>`);
  }
}

//Herencia -> Hereda con funcionalidades nuevas
class Perro extends Animal {
  constructor(especie, edad, color, raza) {
    //Heredando de la clase Padre
    super(especie, edad, color);
    this.raza = null;
  }
  //Método estático -> SIN PROPIEDADES Y OBJETO
  static ladrar() {
    // document.write("!Waw!");
  }
  //Setter -> Modificar o definir valor, recibe como parámetro el valor a modficar
  set modificarRaza(newName) {
    this.raza = newName;
  }
  //Getter -> Obtener valor -> PENDIENTE ⚠
}

//Instanciando una clase -> Se convierte en un objeto
const perro = new Animal('perro', '5', 'doberman');
const gato = new Animal('gato', '2', 'negro');
const pajaro = new Animal('pajaro', '1', 'verde');

//Mostrando las instancias
perro.verInfo();
gato.verInfo();
pajaro.verInfo();

//Instanciando el método setter -> ⚠ Colocar como propiedad
perro.modificarRaza = 'frespuder';
document.write(perro.modificarRaza);

//Instanciando el método getter

//Método estático
Perro.ladrar();
