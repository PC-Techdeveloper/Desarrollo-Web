// Iterando con for...in -> Itera sobre las propiedades enumerables de un objeto.
// for...of -> Itera sobre elementos de un objeto iterable de un objeto (como los elementos de un Array)
const spiderman = {
  name: 'Spidey',
  universe: 42,
  powers: ['web', 'invisibility', 'spider-sense'],
};

for (const property in spiderman) {
  console.log(`${property}: ${spiderman[property]}`);
}

// TRANSFORMAR UN OBJETO EN UN ARRAY:
// .keys(), .values(), .entries()

// Iterar con .keys() -> Retorna un Array con las propiedades enumerables de un objeto
const segundoSpiderman = {
  name: 'spidey',
  universe: 35,
  powers: ['spider-sense', 'web'],
};

const properties = Object.keys(segundoSpiderman);
console.log(properties);
console.log(properties.length);

properties.forEach(property => {
  console.log(property);
});

// Iterando sobre Object.values() -> Retorna un Array con los valores correspondientes
// A las propiedaes enumerables de un objeto
const values = Object.values(segundoSpiderman);

values.forEach(value => {
  console.log(value);
});

/*
Iterando con Object.entries(): Retorna un Array de arrays, donde cada subarray es un par [property, value] correspondiente a las propiedades enumerables de un objeto
*/

const entries = Object.entries(segundoSpiderman);

entries.forEach(entry => {
  const property = entry[0];
  const value = entry[1];

  console.log(`${property}: ${value}`);
});
