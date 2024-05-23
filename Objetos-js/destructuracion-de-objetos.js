/*
Utilizando destructuración de objetos podemos separar en variables las propiedades que tenemos en el objetos.
*/
const USER = {
  firstName: 'Juan',
  role: 'Streamer',
  life: 99,
};

// const { firstName, role, life } = USER;
// console.log({firstName, role, life});

//Renombrar las variables

// const { firstName, role: type, life } = USER;
// console.log({ firstName, type, life });

/*
Si una de las propiedades no existe (o tenga un valor undefined), también se puede establecer un valor por defecto.
*/

// const { firstName, role = 'Normal user', life = 100 } = USER;
// console.log({ firstName, role, life });

/*
REESTRUCTURANDO NUEVOS OBJETOS: Reutilizar objetos y recrear nuevos objetos a partir de otros, basandose en objetos existentes, añadiendole nuevas propiedades o sobreescribiendo algunas de sus propiedades antiguas.

*/

// const USER2 = {
//   firstName: 'Juan',
//   role: 'Streamer',
//   life: 99,
// };
// //Nueva propiedad power y sobreescribir la propiedad life
// const FULL_USER = {
//   ...USER2,
//   power: 25,
//   life: 50,
// };

/*
HACIENDO COPIAS DE OBJETOS: Crear un nuevo objeto a partir de un objeto existente, copiando sus propiedades y sus valores. Los tipos de datos complejos como arrays y objetos no se copian, SON REFERENCIAS.
*/

// const USER3 = {
//   firstName: 'Juan',
//   role: 'Streamer',
//   life: 99,
//   features: ['Streaming', 'Gaming', 'Music'],
// };

// const FULL_USER3 = {
//   ...USER3,
//   power: 25,
//   life: 50,
// };

// console.log(USER3.features);
// console.log(FULL_USER3.features);

// // Modificando el objeto original y alterando ambos objetos
// FULL_USER3.features[0] = 'Movies';

// console.log(USER3.features);
// console.log(FULL_USER3.features);

//...structuredClone() -> Función que devuelve un nuevo objeto y no la referencia
const USER4 = {
  firstName: 'Manz',
  role: 'Streamer',
  life: 99,
  features: ['Learn', 'Code', 'Paint'],
};

const FULL_USER4 = {
  ...structuredClone(USER4),
  power: 25,
  life: 50,
};

console.log(USER4.features);
console.log(FULL_USER4.features);

//FULL_USER4 Ha sido modificado y USER4 no ha sido alterado.
FULL_USER4.features[0] = 'Program';

console.log(FULL_USER4.features);
console.log(USER4.features);

//ESTRUCTURAS ANIDADAS

const USER5 = {
  name: 'Manz',
  role: 'Streamer',
  attributes: {
    height: 180,
    favColor: 'blueviolet',
    hairColor: 'black',
  },
};

//Extraer propiedad attributes
const { attributes } = USER5;
console.log(attributes);

//Extraer propiedad height
const {
  attributes: { height },
} = USER5;
console.log(height);

//Extraer propiedad height y renombrarlo por size
const {
  attributes: { height: size },
} = USER5;
console.log(size);

//DESTRUCTURACIÓN REST (...)
const USER6 = {
  myName: 'Manz',
  myRole: 'Streamer',
  myLife: 99,
};
//myName destructurado como variable y rest como objeto que contiene el resto de propiedades
const { myName, ...rest } = USER6;

/*
PARÁMETROS DESESTRUCTURADOS:
Podemos separar en variables individuales un objeto en un ámbito específico.

OBSERVACIÓN: La desestructuración solo funciona para estructuras de datos. Si se tiene un objeto que contiene métodos o elementos del DOM, Por ejemplo, no se coparán y lanzará una excepción.
*/
const USER7 = {
  name: 'Manz',
  role: 'Streamer',
  life: 99,
};
//Desestructurando las primeras 3 propiedades
function show({ name, role, life }) {
  const stars = '⭐'.repeat(life / 20);
  return `
  Nombre: ${name} (${role})${stars}`;
}

console.log(show(USER7));
