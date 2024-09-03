/*Los ciclos son estructuras de control que permiten ejecutar una secuencia de instrucciones repetidamente.*/

/* let elementos = ['Programar', 'en', 'JavaScript', 'es', 'divertido'];
let parrafo = document.getElementById('parrafo1');

function mostrarElementos() {
  let texto = ' ';
  for (let i = 0; i < elementos.length; i++) {
    texto += 'Elemento ' + i + ': ' + elementos[i] + '<br>';
  }
  parrafo.innerHTML = texto;
} */

/*
Los ciclos 'for' y 'while' se pueden utilizar con el mismo proposito; recorrer los elementos de un array.
*/

let elements = ['Programar', 'en', 'JavaScript', 'es', 'divertido'];
let phrase = document.getElementById('parrafo1');

function showElements() {
  let text = '';
  let i = 0;
  while (i < elements.length) {
    text += 'Elemento ' + i + ': ' + elements[i] + '<br>';
    i++;
  }
  phrase.innerHTML = text;
}

/*
¿Qué diferencia hay entre ambos ciclos?
- Declarar y asignar variables antes del while, dentro de este sólo debe estar la expresión condicional. Dentro del ciclo también se actualiza el contador al final con i++. Aumentar el valor de la variable es muy importante para evitar que el ciclo se ejecuta indefinidamente.

- Los ciclos while se utilizan para verificar alguna otra condición que utilice tipos de datos no-númericos.
*/
