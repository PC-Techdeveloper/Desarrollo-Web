//Crear un arreglo (array)
let myArr1 = ['Hola', 'Mundo', 7];

let myAArr2 = [];

//Acceder a los arrays desde el índice -> 0, 1, 2...
console.log(myArr1[2]);

//Modificar un array
myArr1[0] = 'Hello, It is amazing';
console.log(myArr1);

//Métodos de arrays

//length -> Regresa la longitud del array
let miArreglo = ['hola', 'mundo', 7, 1, 2, 3, 4, 5];
console.log(miArreglo.length);

//pop -> Elimina el último elemento del array
console.log(miArreglo.pop());
console.log(miArreglo);

//push -> Agrega un elemento al final del array
miArreglo.push(6);
console.log(miArreglo);

//shift -> Elimina el primer elemento del array
console.log(miArreglo.shift());
console.log(miArreglo);

//unshift -> Agrega un elemento al principio del array
miArreglo.unshift(20);
console.log(miArreglo);

//splice -> Agrega y borra elementos de acuerdo a su posición
/*
- El primer parámetro es la posición donde se insertará el elemento
- El segundo parámetro es la cantidad de elementos que se eliminarán y los siguientes son los valores que se agregarán
*/
let deleteElement = miArreglo.splice(1, 2, 8, 'world');
console.log(deleteElement);

//slice
/*
Sólo accede a porciones específicas de un array las regresa.
- Puede tener hasta dos parámetros, ambos índices del arreglo que serán el intervalo de elementos a copiar. El segundo parámetro es el limite, sólo hay uno, copia todo a partir del primer índice.
*/
let myArray3 = ['hello', 'world', 22, 45, 67];
let myArray4 = myArray3.slice(0, 1);
console.log(myArray4);
