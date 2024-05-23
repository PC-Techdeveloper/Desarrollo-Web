/*
El operador de encadenamiento opcional (opcional chaining)
*/

const gamesystem = {
  firstName: 'PS5',
  price: 550,
  specs: {
    cpu: 'AMD Ryzen Zen 2',
    gpu: 'AMD Ryzen RDNA 2',
  },
};

// gamesystem.specifications.cpu -> ERROR ❌

// Operador de encademiento opcional -> ?. -> Si no existe devolverá 'undefined'
// Pero lo interesante es que no mostrará un ERROR
console.log(gamesystem.specifications?.cpu);
console.log(gamesystem.whatever?.otra?.cosa?.aqui);

// Con propiedades que si existen
console.log(gamesystem.specs?.gpu);
