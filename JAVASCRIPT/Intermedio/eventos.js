/* 
Los eventos se lanzan dentro de la ventana del navegador y usualmente están asociados a un elemento en específico dentro de dicha ventana. Esto puede ser un solo elemento, un grupo de elementos, el documento HTML cargado de la pestaña actual, o la ventana del navegador en su totalidad. 
*/

//TEMPORIZADORES -> Permite funciones
/*
setTimeout -> Establece un temporizador que ejecuta una función o una pieza de código específica una vez que expire el temporizador.

setInterval -> Llama a una función o ejecuta un fragmento de código, con un retardo de tiempo fijo entre cada llamada
*/
// const temporizador = setTimeout(() => {
//   document.write("Hola!");
// }, 2000);

// //Detener el setTimeout desde una variable
// clearTimeout(temporizador);

const intervalo = setInterval(() => {
  document.write('Hola!');
}, 2000);

//Detener el setInterval
setTimeout(() => {
  clearInterval(intervalo);
}, 7000);

// const input = document.querySelector('.input-prueba');
// const contenedor = document.querySelector('.seleccionado');

// //DETECTAR LAS TECLAS DEL TECLADO

// input.addEventListener('keyup', (e) => {
//   console.log(e);
//   let tecla = e.key;
//   let nuevoContenido = `La última tecla presionada fue: <b>${tecla}</b>`;
//   contenedor.innerHTML = nuevoContenido;
// });

//OBTENER LO QUE EL USUARIO SELECCIONO

// input.addEventListener('select', (e) => {
//   let start = e.target.selectionStart;
//   let end = e.target.selectionEnd;
//   let textoCompleto = input.value;
//   contenedor.innerHTML = textoCompleto.substring(start, end);
// });

// const button = document.querySelector('#button');
// const container1 = document.querySelector('#container-1');
// // const container2 = document.querySelector('#container-2');
// const input = document.querySelector('.input-prueba');

// button.addEventListener('dblclick', (e) => {
//   alert('Di click en el botón!');
// });

//OBJETO EVENTO -> E.TARGET

// container1.addEventListener('mouseup', (e) => {
//   alert('Di click en el contenedor rojo!');
//   console.log(e);
//   //Detiene la propagación
//   //e.stopPropagation();
// });

// input.addEventListener('keydown', (e) => {
//   console.log('Una tecla fue presioanda');
// });

// input.addEventListener('keypress', (e) => {
//   console.log('Un usuario presiono una tecla');
// });

// input.addEventListener('keyup', (e) => {
//   console.log('Una tecla fue soltada');
// });

/*
FLUJO DE EVENTOS: Los más específicos son los hijos y los menos específicos son los contenedores. Dos tipos de flujo de evento, Event Bubbling (Burbuja) o Event Capturing (Captura) ya que es el orden en el que se ejecutan los eventos.
 */

//MANEJADOR DE EVENTOS -> EVENTÑ¿LISTENER

// button.addEventListener('click', () => {
//   alert('Pedro');
// });

// button.addEventListener('click', saludar);

// //Declaración de función

// function saludar() {
//   alert('Hola');
//   //Remover el evento
//   button.removeEventListener('click', saludar);
// }

/*
EVENTOS DE MOUSE:

click -> Ocurre con un click.

dbclick -> Ocurre con un doble click.

mouseover -> Ocurre cuando el puntero se mueve sobre un 
elemento o sobre uno de sus hijos.

mousedown -> Ocurre cuando un usuario apreta un botón del mouse sobre un elemento.

--- OTROS ---

contextmenu -> Ocurre con un click en el botón derecho de un elemento para abrir un menú contextual.

mouseenter -> Ocurre cuando el puntero se mueve sobre un elemento.

mouseleave -> Ocurre cuando el puntero se mueve fuera de un elemento.

mouseup -> Ocurre cuando un usuario suelta un botón del mouse sobre un elemento.

mousemove -> Ocurre cuando el puntero se mueve mientras está sobre un elemento.
*/

/*
EVENTOS DE TECLADO:

keydown -> Se activa cuando se presiona una tecla.

keyup -> El evento se activa cuando se suelta una tecla.

keypress -> Ocurre cuando una tecla se presiona y suelta en un elemento.
*/

/*
EVENTOS DE INTERFAZ:

abort -> Ocurre cuando un elemento madre elimina a su hijo.

error -> Ocurre cuando sucede un error durante la carga de un archivo multimedia.

load -> Ocurre cuando un objeto se ha cargado.

beforeunload -> Ocurre antes de que el documento esté a punto de descargarse.

unload -> Ocurre una vez que se ha descargado una página.

resize -> Ocurre cuando se cambia el tamaño de la vista del documento.

scroll -> Ocurre cuando se desplaza la barra de desplazamiento de un elemento.

select -> Ocurre después de que el usuario selecciona algun texto de <input> o <textarea> 
*/
