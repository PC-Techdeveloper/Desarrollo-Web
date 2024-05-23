// La función sumar tiene dos parámetros: a y b
function sumar(a, b) {
  return a + b
}

function restar(a, b) {
  return a - b
}
// Cuando llamamos a la función, le pasamos dos argumentos 5 y 2
const resultadoSuma = sumar(5, 2)
const resultadoResta = restar(10, 4)

console.log(resultadoSuma)
console.log(resultadoResta)

// El orden de los parámetros IMPORTA!
function cocinarMicroondas(plato, tiempo, potencia) {
  if (plato === '🐥' && tiempo === 1 && potencia === 5) {
    return '🍗'
  } else if (plato === '🥚' && tiempo === 2 && potencia === 3) {
    return '🍳'
  }

  return '❌ Plato no soportado!'
}

const resultadoCocina = cocinarMicroondas('🐥', 1, 5)
console.log(resultadoCocina)
