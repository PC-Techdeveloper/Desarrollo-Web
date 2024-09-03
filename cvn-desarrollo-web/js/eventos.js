/*
EVENTOS: Los eventos se utilizan para ejecutar código bajo condiciones específicas para la página y sus elementos. Existen muchos eventos en JavaScript para ejecutar código en situaciones como clics o cuando el usuario ingresa texto en un <input> o cuando se carga una página nueva.
*/

//Seleccionar al elemento para usar los eventos

//Opción 1: Asignar una función que ya ha sido declarada.
document.getElementById('elemento1').onclick = myFunc;

//Opción 2: Asignar una nueva función al evento.
document.getElementById('elemento2').onclick = function () {
  console.log('Hola Soy el evento clic!🌈');
};

//Opción 3: Utilizar el método addEventListener().
document.getElementById('elemento3').addEventListener('click', myFunction);

function myFunction() {
  console.log('Hola Soy el evento clic!🌈');
}

/*Otros Eventos.

- onmouseover -> Ocurre cuando el puntero esta sobre el elemento.
- onmouseout -> Ocurre cuando el puntero sale del elemento.
- onkeydown -> Ocurre cuando se presiona una tecla.
- onkeyup -> Ocurre cuando se libera una tecla.
- onload -> Ocurre cuando la página se carga.
- submit -> Ocurre cuando se envía un formulario.
- resize -> Ocurre cuando se redimensiona la ventana.
- scroll -> Ocurre cuando se desplaza la página.
- dbclick -> Ocurre cuando se hace doble clic en un elemento.
*/
