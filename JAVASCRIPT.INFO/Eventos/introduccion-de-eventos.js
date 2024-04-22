/*
Un evento es una señal que algo ocurrió. Todos los nodos del DOM generan dichas señales (pero los eventos no están limitados sólo al DOM)

EVENTOS DEL DOM MÁS UTILIZADOS:
EVENTOS DEL MOUSE:
- click -> Cuando el mouse hacer click sobre un elemento.
- contextmenu -> Cuando el mouse hace click derecho sobre un elemento.
- mouseover/mouseout -> Cuando el cursor del mouse ingresa/abandona un elemento.
- mousedown/mouseup -> Cuando el botón del mouse es presionado/soltado sobre un elemento.
- mousemove -> Cuando el mouse se mueve.

EVENTOS DEL TECLADO:
keydown/keyup -> Cuando se presiona/suelta una tecla.

EVENTOS DEL ELEMENTO FORM:
submit -> Cuando el visitante envía un <form>.
focus -> Cuando el visitante hace foco en un elemento, por ejemplo un <input>.

EVENTOS DEL DOCUMENTO:
DOMContentLoaded -> Cuando el HTML es cargado y procesado, el DOM está completamente construido.

EVENTOS DEL CSS:
transitionend -> Cuando una animación CSS concluye.
*/

//CONROLADORES DE EVENTOS:
/*
Para reaccionar a los eventos se asigna un handler (controlador) el cual es una función que se ejecuta en caso de un evento. Los handlers son una forma de ejecutar código JavaScript en caso de acciones por parte del usuario.
*/

//ATRIBUTO HTML
//Un handler puede ser con un atributo llamado on<event>.
//Crear una función a un evento click
function countRabbits() {
  for (let i = 1; i <= 3; i++) {
    alert('Conejo número: ' + i);
  }
}

//PROPIEDAD DEL DOM
//Podemos asignar un handler usando una propiedad del DOM on<event>
//Para eliminar un handler, se asigna elem.onclick = null
elem.onclick = function () {
  alert('!Gracias¡');
};

//ACCEDIENDO AL ELEMENTO 'THIS'
//El valor de 'this' dentro de un handler es el elemento, el cual tiene el handler dentro.

//ADDEVENTLISTENER <- PENDIENTE