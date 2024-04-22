//Las promesas usan métodos .then para recibir un resultado y .catch para mostrar un error.

//PROMISE WITH .THEN -> EXITOSO
const promise = new Promise(function (resolve, reject) {
  resolve(
    setTimeout(() => {
      console.log('¡Hecho!');
    }, 2000)
  );
});

//En caso de un error:
const promiseTwo = new Promise(function (resolve, reject) {
  setTimeout(() => reject(new Error('¡Vaya!')), 1000);
});

promise.then(
  (result) => console.log(result),
  (error) => console.log(error)
);

//PROMISE WITH .CATCH -> ERRORES
let thirdPromise = new Promise((resolve, reject) => {
  setTimeout(() => reject(new Error('Vaya!')), 2000);
});

thirdPromise.catch(alert);

//Limpieza finally -> Realiza la limpieza y finalización después de que las operaciones se han completado
new Promise((resolve, reject) => {
  setTimeout(() => resolve('valor'), 2000);
})
  //Se dispara primero
  .finally(() => console.log('Promesa lista'))
  .catch((err) => console.log(err));
