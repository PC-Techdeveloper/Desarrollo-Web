//value -> Acceder a la información
//getElementById -> Selector ID del HTML
//querySelector -> Selector de CLASE del HTML -> .class
//e.preventDefault(); -> No actualiza ni envía los datos
/*
MÉTODOS CLASSLIST:
add -> Añade las clases indicadas

remove -> Elimina las clases indicadas

item -> Devuelve el valor de la clase por índice de colección

toggle -> Cuando sólo hay un argumento presente: Alterna el valor de la clase; ej., si la clase existe la elimina y devuelve false, si no, la añade y devuelve true. Cuando el segundo argumento está presente: Si el segundo argumento se evalúa como true, se añade la clase indicada, y si se evalúa como false, la elimina.

contains -> Comprueba si la clase indicada existe en el atributo de clase del elemento.

replace -> Reemplaza una clase existente por una nueva.

*/
//VALIDACIONES DE UN FORMULARIO

//Seleccionando todos los elementos del input
const nombre = document.getElementById('nombre');
const email = document.getElementById('email');
const materia = document.getElementById('materia');
const boton = document.getElementById('btn-enviar');
const resultado = document.querySelector('.resultado');

boton.addEventListener('click', (e) => {
  e.preventDefault();
  let error = vallidarCampos();
  if (error[0]) {
    resultado.innerHTML = error[1];
    //Añadiendo una clase
    resultado.classList.add('red');
  } else {
    resultado.innerHTML = 'Solicitud enviada correctamente';
    resultado.classList.add('green');
    resultado.classList.remove('red');
  }
});

//Función verificar -> Validar errores
const vallidarCampos = () => {
  //Primer válidación
  let error = [];
  if (nombre.value.length < 5 || nombre.value.length > 40) {
    error[0] = true;
    error[1] = 'El nombre es inválido.';
    return error;
  } else if (
    email.value.lengt < 5 ||
    email.value.length > 40 ||
    email.value.indexOf('@') === -1 ||
    email.value.indexOf('.') === -1
  ) {
    error[0] = true;
    error[1] = 'El email es inválido.';
    return error;
    //Tercera validación
  } else if (materia.value < 4 || materia.value > 40) {
    error[0] = true;
    error[1] = 'La materia no existe.';
  }
  //Si no hay errores
  error[0] = false;
  return error;
};
