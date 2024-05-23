const saludar = nombre => {
  return `Hola ${nombre}, Esto es un Arrow Function!`;
};

const result = saludar('Miguel');
console.log(result);

// RETURN IMPLÍCITO

/*
Cuando una función flecha tiene una sola expresión, se puede omitir las {} y la palabra clave return para hacerla más corta. Esto se conoce como return implícito
*/

// Declaración de función regular
function sumar(a, b) {
  return a + b;
}

// Función flecha
const sumarFlecha = (a, b) => {
  return a + b;
};

// Función flecha con return implícito
const sumandoFlecha = (a, b) => a + b;

console.log(sumar(4, 4));
console.log(sumarFlecha(3, 2));
console.log(sumandoFlecha(5, 2));
