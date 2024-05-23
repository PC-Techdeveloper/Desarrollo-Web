// Atajo al crear un objeto -> Usar como valor las variables
const myName = 'Spidey';
const universe1 = 42;

const spiderman = {
  myName: myName,
  universe: universe1,
  powers: ['web', 'invisibility', 'spider-sense'],
};

// Si tienen el mismo nombre se puede omitir el valor y dejar solo el nombre de la propiedad
const firstName = 'Spidey';
const universe = 42;
const powers = ['web', 'invisibility', 'spider-sense'];

const otherSpidermna = { firstName, universe, powers };

// Destructuración de objetos: Al recuperar propiedades
const hero = {
  nombre: 'Spidey',
  universo: 32,
  poderes: ['invisibility', 'web'],
};

const { nombre, universo, poderes } = hero;
console.log(nombre);
console.log(universo);
console.log(poderes);

// Renombrar variables y valores por defecto
const { universo: universeNumber } = hero;
console.log(universeNumber);

// Si una propiedad no existe, se puede asignar un valor por defecto
const { yourName, isAvenger = false } = spiderman;

console.log(isAvenger);

// OBJETOS ANIDADOS Y ATAJOS
const soySpiderman = {
  name: 'Spidey',
  universe: 42,
  powers: ['web', 'invisibility', 'spider-sense'],
  partner: {
    name: 'Mary Jane',
    universe: 42,
    powers: ['red hair', 'blue eyes'],
  },
};

// Recuperar la propiedadd name del objeto partner y guardarla en una variable
const { partner } = soySpiderman;
const { myname } = partner;
console.log(myname);

// También se puede hacer en una sola línea
const { partner: { name } } = soySpiderman;



