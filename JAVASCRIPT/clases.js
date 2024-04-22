//Declaración de clase -> Anoníma

class Rectangulo {
  constructor(alto, ancho) {
    (this.alto = alto), (this.ancho = ancho);
  }
  //Getter
  get area() {
    return this.calcularArea();
  }
  //Método
  calcularArea() {
    return this.alto * this.ancho;
  }
}

const cuadrado = new Rectangulo(10, 10);

console.log(cuadrado.area);

// Métodos estáticos son llamados sin instanciar su clase y no pueden ser llamados
// Mediante una instancia de clase. Son útiles para crear funciones de utilidad para una aplicación.

class Punto {
  constructor(x, y) {
    this.x = x;
    this.y = y;
  }

  static distancia(a, b) {
    const dx = a.x - b.x;
    const dy = a.y - b.y;

    return Math.sqrt(dx * dx + dy * dy);
  }
}

const punto1 = new Punto(5, 6);

const punto2 = new Punto(10, 45);

console.log(Punto.distancia(punto1, punto2));

//Subclases con herencia -< extend

class Animal {
  constructor(name) {
    this.name = name;
  }

  hablar() {
    console.log(`${this.name} hacer un ruido`);
  }
}

class Perro extends Animal {
  hablar() {
    console.log(`${this.name} ladra`);
  }
}

const perro = new Perro('Luna');

perro.hablar();
