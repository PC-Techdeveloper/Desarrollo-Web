//Async -> Asegura de que la función devuelva una promesa o envuelve
//Las no promesas

async function f() {
  return 1;
}

f().then(console.log(f()));

//Await -> Hace que JavaScript espere hasta que la promesa responda y devuelva
//Su resultado.

async function f() {
  let promise = new Promise((resolve, reject) => {
    setTimeout(() => resolve('¡Hecho!'), 1000);
  });

  const result = await promise;
  console.log(result);
}

f();

//Manejo de errores

//Primera versión
async function f() {
  await Promise.reject(new Error('Whoops!'));
}

//Segunda versión más legible
async function f() {
  throw new Error('Whoops!');
}

//Atrapar al error -> try - catch

async function f() {
  try {
    let response = await fetch('/no-user-here');
    let user = await response.json();
  } catch (err) {
    console.log(err);
  }
}

f();
