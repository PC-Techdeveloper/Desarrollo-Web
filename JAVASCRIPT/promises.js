//SetTimeout -> Función que se ejecuta cada cierto tiempo

setTimeout(function () {
  console.log('Hola');
}, 3000);

//Creating a promise

const timerPromise = new Promise(function (resolve, reject) {
  setTimeout(function () {
    resolve('Hello!');
  }, 3000);
});

//The then() method

timerPromise.then(function (value) {
  console.log(value);
});
