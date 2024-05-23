function saludar() {
  console.log('Hola, Miguel!');
}

// Llamada de la función
saludar();
saludar();
saludar();

// Devolviendo un resultado
function sumar() {
  return 1 + 1;
}

// Guardar el resultado en una variable
const resultado = sumar();
console.log(resultado);

// O ver el resultado en consola directamente
console.log(sumar());

// Objeto math -> Operaciones matemáticas:
// Math.random -> Devuelve un número aleatorio entre 0 y 1, con decimales
// Math.floor -> Redondea un número hacia abajo
function getRandomNumber() {
  // Recupera un número aleatorio entre 0 y 1
  const random = Math.random();

  // Lo multiplicamos para que este entre 0 y 10
  const multiplied = random * 10;

  // Redondeamos hacia abajo para que este entre 0 y 9
  const rounded = Math.floor(multiplied);

  // Le sumamos uno para que este entre 1 y 10
  const result = rounded + 1;

  // Devolvemos el resultado
  return result;
}

console.log(getRandomNumber());
