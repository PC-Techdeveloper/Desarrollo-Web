//Expresión de función -> Crear una función en medio de cualquier expresión
let sayHi = function () {
  console.log('Hola!');
};
sayHi();

//Copiar una función a otra variable:
const myFunction = sayHi;
myFunction();

//Funciones Callback -> Funciones dentro de otra función
function ask(question, yes, no) {
  if (console.log(question)) yes();
  else no();
}
function showOk() {
  console.log('Estás de acuerdo.');
}
function showCancel() {
  console.log('Cancelaste la ejecución.');
}
ask('Estás de acuerdo?', showOk, showCancel);
