/* Las clases son funciones especiales que sirven como plantillas para crear objetos que ya contienen datos, propiedades asociadas con esos datos y métodos relacionados con la manipulación de esos datos.
 */

//Para definir una clase, se usa la palabra clave 'class'
class MyClass {}

console.log(typeof MyClass);

//Instanciar una clase para convertilo en un objeto se usa la palabra clave 'new'

const myClassInstance = new MyClass();

console.log(myClassInstance);

/* Las funciones definidas dentro del cuerpo de una clase se expone como métodos de cada instancia de esa clase.
 */

class MyClass2 {
  classMethod() {
    console.log('My class method');
  }
}

const myClassInstance2 = new MyClass2();

myClassInstance2.classMethod();

/* Cuando se crea una instancia de una clase, se llama a un método constructor() especial que realiza cualquier "configuración" necesaria para la instancia recién creada y, luego, inicializa las propiedades asociadas a ella. Cualquier argumento que se pase a la clase cuando se crea la instancia estará disponible para el método constructor():
 */

class MyClass3 {
  constructor(myPassedValue) {
    console.log(myPassedValue);
  }
}

const myClassInstance3 = new MyClass3('A string');

console.log(myClassInstance3);

/* Dentro del cuerpo de una clase, el valor de 'this' hace referencia a la instancia en sí, con cualquier propiedad definida en this expuesta como propiedades de cada instancia de esa clase:
 */

class MyClass4 {
  constructor(myPassedValue) {
    this.instanceProperty = myPassedValue;
  }
}

const myClassInstance4 = new MyClass4('A string!');

console.log(myClassInstance4);

/* Estas propiedades también están disponibles para todos los métodos dentro del cuerpo de la clase:
 */

class MyClass5 {
  constructor(myPassedValue) {
    this.instanceProp = myPassedValue;
  }
  myMethod() {
    console.log(this.instanceProp);
  }
}

const myClassInstance5 = new MyClass5('Second string!.');

console.log(myClassInstance5);

/* Las expresiones de clase se pueden asignar o dejar sin nombre para crear una clase “anónima”.
 */

//Clase Anónima

let classExpression = class {
  constructor() {
    console.log('Hello!');
  }
};

console.log(classExpression);

/* Usar expresiones de clase anónimas para las funciones que crean clases 'sobre la marcha'.
 */

function classMaker() {
  return class {
    constructor() {}
  };
}

let myVariable = classMaker;

console.log(myVariable);

/* Las expresiones de clase permiten redefinir una clase
 */

let ClassExpression2 = class MyClass {};

ClassExpression2 = class MyOtherClass {
  constructor(myString) {
    this.myProp = myString;
  }
};

new ClassExpression2('String.');

console.log(ClassExpression2);

//Heredar clases -> Extends

/* La palabra clave 'extends'se usa en declaraciones o expresiones de clase para crear una clase que actúe como una subclase de otra, y la clase superior (A veces llamada clase 'base') funciona como el prototipo de clase secundaria (A veces llamada 'subclase' o 'clase derivada')
 */

// class ParentClass {}

// class ChildClass extends ParentClass {}

// console.log(ChildClass);

/* Estas subclases heredan las propiedades y los métodos de la clase superior. Esto permite extender la funcionalidad principal de una clase para que cumpla con fines más específicos sin sobrecargar la clase superior a fin de que se adapte a todos los casos de uso posibles o volver a implementar código que tenga un proposito similar.

Las clases secundarias pueden proporcionar sus propias implementaciones de los métodos heredados de una clase superior.
 */

class MyClass6 {
  constructor(myPassedValue) {
    this.instanceProp = myPassedValue;
  }
  classMethod() {
    console.log(`The value was '${this.instanceProp}.'`);
  }
}
//Herencia de clase

class ChildClass extends MyClass6 {
  classMethod() {
    console.log(
      `The value was '${this.instanceProp},' and its type was '${typeof this
        .instanceProp}.'`
    );
  }
}

const myParentClassInstance = new MyClass6('My string.');
const mySubclassInstance = new ChildClass(100);

myParentClassInstance.classMethod();

mySubclassInstance.classMethod();

//También puedes llamar a los métodos definidos en la clase superior en el contexto de la clase secundaria con 'super'

class MyClass7 {
  constructor(myPassedValue) {
    this.instanceProp = myPassedValue;
  }
  classMethod() {
    console.log(`The value was '${this.instanceProp}.'`);
  }
}

class ChildClass2 extends MyClass7 {
  subclassMethod() {
    super.classMethod();
    console.log(`The value type was '${typeof this.instanceProp}.'`);
  }
}
const mySubclassInstance2 = new ChildClass2(100);

mySubclassInstance2.subclassMethod();

/* Si hay un constructor en la subclase, primero se debe llamar a super() junto con los argumentos necesarios antes de hacer referencia a this.
 */

class MyClass8 {
  constructor(myPassedValue) {
    this.instanceProp = myPassedValue;
  }
  classMethod() {
    console.log(`The value was '${this.instanceProp}.'`);
  }
}

class ChildClass3 extends MyClass8 {
  constructor(myPassedValue) {
    super(myPassedValue);
    this.modifiedProp = myPassedValue + 50;
  }
  subclassMethod() {
    super.classMethod();
    console.log(`The value type was '${typeof this.instanceProp}.'`);
  }
}
const mySubclassInstance3 = new ChildClass3(100);

console.log(mySubclassInstance3);

/* Los métodos get y set son métodos especiales que se usan exclusivamente para recuperar y definir valores, respectivamente. Los métodos definidos con las palabras clave get y set permite crear métodos con los que se puede interactuar como si fueran propiedades estáticas.
 */

class MyClass9 {
  constructor(originalValue) {
    this.totalValue = 0;
  }

  set doubleThisValue(newValue) {
    this.totalValue = newValue * 2;
  }

  get currentValue() {
    console.log(`The current value is: ${this.totalValue}`);
  }
}

const myClassInstance6 = new MyClass9();

console.log(myClassInstance6);

myClassInstance6.doubleThisValue = 20;

myClassInstance6.currentValue;

/* Las propiedades get y set se definen en la propiedad del prototipo de clase y, por lo tanto, están disponibles para todas las instancias de la clase.
 */

//Campos y métodos de clase

//Campos

/* Los campos de clae se declaran directamente dentro del cuerpo de una clase, no se agregan de forma explícita como una propiedad del valor this. Sin embargo, el resultado es el mismo, una propieaad definida en instancias de esa clase.
 */

//Inicializar un campo con un valor.
class MyClass10 {
  myResult = false;
  set setValue(myValue) {
    this.setValue = myValue;
  }
}

const myClassInstance7 = new MyClass10();

console.log(myClassInstance7);

// myClassInstance7.setValue = true;

console.log(myClassInstance7);

/* Los campos de clase son funcionalmente idénticos a las propiedades adjuntas a la clase con this. Esto significa que se puede acceder a ellas y modificarlas desde fuera de clase como cualquier propiedad.
 */

class MyClass11 {
  myField = true;
}

const myInstance = new MyClass11();

console.log(myInstance.myField);

//Modificado

myClassInstance.myField = false;

console.log(myClassInstance.myField);

/* Los campos proporcionan una base para algunas de las funciones más avanzadas de las clases.
 */

//Métodos y campos privados

/* Los campos y métodos Private no son accesibles fuera de una clase. Una propiedad privada se asocia con una instancia de una clase, lo que significa que cada instancia contiene su propio conjunto de campos y métodos, según se definen en la clase. Para convertir una propiedad en privada, se agrega un elemento '#' al comienzo del identificador cuando se declare.
 */

class MyClass12 {
  #myPrivateField = true;
  #myPrivateMethod() {}
}

const myInstance2 = new MyClass12();

console.log(myInstance2);

/* Los campos privados se deben declarar en el cuerpo de la clase que los contiene. Puedes modificar su valor más adelante como una propiedad de this, pero no puedes crear el campo con this.

No se puede acceder a los campos privados desde otras partes de una secuencia de comandos. Esto evita que las propiedades de datos se modifiquen fuera de los métodos get y set que se proporcionan para interactuar con los valores que contienen, y evita el acceso directo a los métodos diseñados solo para su uso dentro de la propia clase.
*/

class MyClass13 {
  #myResult = false;
  set setValue(myValue) {
    this.#myResult = myValue;
  }
}
const myInstance3 = new MyClass13();

myInstance3.setValue = true;

console.log(myInstance3);

/* Los campos privados tienen un alcance estricto para el cuerpo de la clase que los contiene, lo que significa que incluso las clases secundarias no pueden acceder a los campos privados asociados con una clase superior:
 */

//Campos y métodos estáticos

/* Los campos y métodos estáticos son miembros de una clase en sí, no miembros de las instancias de esa clase. Debido a esto, los campos estáticos proporcionan un punto central para los datos que no serán únicos de cada instancia de una clase, pero al que esas instancias podrían necesitar hacer referencia, por ejemplo, información de configuración compartida. Los métodos estáticos suelen ser funciones de utilidad para trabajar con instancias de una clase, como comparar u ordenar instancias con un campo que contienen.

Para definir campos y métodos estáticos en el cuerpo de una clase, se usa la palabra clave static:
*/

class MyOtherClass {
  static myStaticField;
  static myStaticMethod() {}
}

const myInstace = new MyOtherClass();

/* 
Se puede usar la notación de puntos para crear un método estático.
*/

class MySecondClass {
  constructor() {}
}

MySecondClass.myStaticMethod = function () {};

/* No se puede acceder a propiedades estáticas desde una instancia de su clase, pero están disponibles en el constructor de la clase.
 */

class MyThirdClass {
  static myStaticField = true;
  static myStaticMethod() {
    console.log('A static method.');
  }
}
const myFirstInstance = new MyThirdClass();

//Método estático desde el constructor
MyThirdClass.myStaticMethod();

/* No son técnicamente necesarias, pero el uso de métodos estáticos es una práctica recomendada para crear utilidades que funcionen con instancias de una clase.
 */
