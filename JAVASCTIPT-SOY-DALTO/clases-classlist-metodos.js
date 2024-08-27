const titulo = document.querySelector('.titulo');

/*
MÉTODOS DE CLASSLIST:

* add -> Añade una clase.
? remove -> Elimina la clase.
! item -> Devuelve la clase del índice específicado, devuelve un valor.
? contains -> Verifica si ese elemento posee o no, la clase específicada y devuleve un valor booleano.
? replace -> Reemplaza una clase por otra.
* toggel -> Si no tiene la clase específicada, la agrega, si YA la tiene, la elimina, parámetro opcional (true/false)
*/
let nombreDeClase = 'grande';

let valor = titulo.classList.replace('grande','pequeño');
document.write(valor);
