/*
OBTENCIÓN Y MODIFICACIÓN DE ELEMENTOS:
* textContent -> Devuelve el texto de cualquier nodo.
* innerHTML -> Devuelve el contenido HTML de un elemento.
¿ outerHTML -> Devuelve el código HTML completo del elemento.

*/

const titulo = document.querySelector('.titulo');

let resultado = titulo.textContent;
let resultado1 = titulo.innerHTML;
let resultado2 = titulo.outerHTML;

alert(resultado);
alert(resultado1);
alert(resultado2);
