/*
Accediendo a elementos HTML
JavaScript permite interactuar, crear o eliminar elementos de un documento Web. Existen varias funciones en JavaScript que permite acceder a elementos de HTML, dependiendo de si quieres obtener uno o varios elementos, a partir de su tipo, su clase o su ID.
*/

/*
DOM:
Significa Document Object Model, esto es la estructura del documento HTML, sus elementos, atributos, etc. Todo navegador crea un DOM al acceder a una página web, y JavaScript utiliza este modelo para poder acceder, agregar, borrar, modificar elementos del documento.
*/

function changeText() {
  let element = document.getElementById('rect');
  element.innerHTML = 'Este es el nuevo texto!';
}

function OtherText() {
  let element = document.getElementById('rect');
  element.innerHTML = `<a href="https://www.google.com" target="_blank">Ir a Google</a>`;
}

/*
Para hacer las modificaciones, se utiliza la propiedad innerHTML, a la cual se le asigna el HTML Interno del elemento como tipo string.

*/

/*Acceder a los elementos por clase: A diferencia de los IDs, podemos tener múltiples elementos con la misma clase, podemos obtener elementos de acuerdo a su clase, utilizando la función document.getElementsByClassName o querySelctor.*/

function cambiaTexto() {
  let elem = document.getElementsByClassName('rect');

  elem[0].innerHTML = 'Nuevo texto 1';
  elem[1].innerHTML = 'Nuevo texto 2';
}

/*Acceder a elementos por su tipo
Obtener elementos por su tipo de etiqueta también puede ser de utilidad cuando queremos modificar múltiples elementos. La función que se utiliza para seleccionar a los elementos de un tipo específico es document.getElementsByTagName.
*/
function cambiaTexto2() {
  let elem = document.getElementsByTagName('div');

  elem[0].innerHTML = 'Nuevo texto 1';
  elem[1].innerHTML = 'Nuevo texto 2';
  elem[2].innerHTML = 'Nuevo texto 3';
}

/*
MODIFICAR ATRIBUTOS:
*/

const cambiarImagen = () => {
  let link1 =
    'https://images.unsplash.com/photo-1610024552791-c92de4e0394b?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1300&q=80';

  let link2 =
    'https://images.unsplash.com/photo-1609894836394-512d7c1a375b?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=634&q=80';

  let imagen = document.getElementById('imagen1');

  if (imagen.src === link1) {
    imagen.src = link2;
  } else {
    imagen.src = link1;
  }
};
