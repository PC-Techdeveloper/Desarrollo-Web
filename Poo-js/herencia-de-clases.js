/*
¿QUÉ ES UNA HERENCIA DE CLASES?
Una herencia de clases se denomina a la característica donde una clase hija obtiene las propiedades y métodos de una clase porque se ha establecido una relación entre ambas. Esta relación se establece a través de la plabra clave 'extends'.
*/

class Figura {
  constructor() {
    console.log('Soy una figura geométrica! 🟩');
  }
}

class Cuadrado extends Figura {
  constructor() {
    super();
    console.log('Soy un cuadrado! 🟩');
  }
}

const primerFigura = new Cuadrado();

/*

EL MÉTODO SUPER: El método especial super() se encarga de llamar al constructor de la clase padre, también denominada superclase, de hay su nombre. Por lo que funcionará en cascada e irá ejecutando primero el consructor del padre, y luego el texto del constructor hijo.
*/

class MiFigura {
  type = 'geométrica';
  color = 'naranja';

  constructor() {
    console.log('Constructor padre finalizado');
  }

  show() {
    console.log(`Soy una forma ${this.type} de color ${this.color}`);
  }

  setColor(color) {
    this.color = color;
  }
}

class MiCuadrado extends MiFigura {
  // Sobreescribiendo la propiedad type
  type = 'cuadrada';

  constructor() {
    super();
    console.log('Constructor hija finalizado.');
  }
}

const c1 = new MiCuadrado();
c1.show();

const c2 = new MiCuadrado();
c2.setColor('verde');
c2.show();

/*
ACCEDER A MÉTODOS DEL PADRE:
También permite utilizar la plabra clave 'super()'en métodos para llamar a métodos del padre según interese heredar o no
*/

class Padre {
  soloPadre() {
    console.log('Tarea en el padre...');
  }
  padreHijo() {
    console.log('Tarea en el padre...');
  }
  sobreHijo() {
    console.log('Tarea en el padre...');
  }
}

class Hijo extends Padre {
  padreHijo() {
    // Accedemos con la función super()
    super.padreHijo();
    console.log('Tarea en el hijo...');
  }

  soloHijo() {
    console.log('Tarea en el hijo...');
  }

  sobrePadre() {
    console.log('Tarea en el hijo...');
  }
}

const hijo1 = new Hijo();

hijo1.padreHijo();
