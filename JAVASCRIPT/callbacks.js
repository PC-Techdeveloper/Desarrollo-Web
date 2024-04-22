/*
Una función de callback es una función que se pasa a otra función como un argumento, que luego invoca dentro de la función externa para completar algún tipo de rutina o acción.
*/

//Función sincrónica

function saludar(name) {
  console.log(`Hola ${name}`);
}

function procesarEntradaUsuario(callback) {
  let nombre = prompt('Por favor ingresa tu nombre:');
  callback(nombre);
}

//Callback dentro de otra función
procesarEntradaUsuario(saludar);
