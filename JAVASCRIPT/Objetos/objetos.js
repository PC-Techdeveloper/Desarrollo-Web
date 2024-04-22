/*
Un objeto puede contener datos asociados con identificadores, como una variable, pero mantiene su tipo de datos object sin importar los datos que contenga.
*/

let my_object = { key: { subKey: true, otherSubKey: false } };

console.log(my_object);

//Crear objetos con la palabra clave 'new'.

let my_object_2 = new Object();

console.log(my_object_2);

/*
Los valores null y undefined dan como resultado un objeto vacío, funcionalmente idéntico a invocar a new Object() sin proporcionar un argumento.
*/

let my_object_3 = new Object({ myValue: 10 });

console.log(my_object_3);

/*
Existen dos formas de configurar, modificar y accedr a las propiedades de un objeto: La notación de puntos y la notación de corchetes.
*/

//Notación de puntos:

const miObjeto = {
  myProp: 'String value',
};

console.log(miObjeto.myProp);

/*
Notación de puntos para acceder, cambiar o crear propiedades nuevas con los operadores de asignación.
*/

miObjeto.myProp = 'Ny second string value';

console.log(miObjeto);

/*
Encadenar claves de propiedad con la notación de puntos permite acceder a las propiedades de los objetos que son propiedades de un objeto.
*/

const myObj = { myProp: { childProp: true } };

console.log(myObj.myProp.childProp);

/*
Operador de encadenamiento opcional (?.) para acceder de forma segura a las propiedades anidadas de los objetos.
*/

console.log(myObj.myMissingProp?.childProp);

//Notación con corchetes

/*
Contiene un valor que evalúa una string (o un símbolo) que representa la clave de propiedad.
*/

console.log(myObj['myProp']);

/*
El valor entre corchetes se evalúa como un literal de string, sin importar su tipo de datos.
*/

const myObj2 = {
  false: 25,
  10: true,
  'key with spaces': true,
};

console.log(myObj2[false]);

console.log(myObj2[10]);

console.log(myObj2['key with spaces']);

/*
La fortaleza de esta sintaxis radica en su flexibilidad, que permite el uso de strings creadas de forma dinámica para acceder a las propiedades.
*/

const colors = {
  color1: 'red',
  color2: 'blue',
  color3: 'green',
};

const randomNumber = Math.ceil(Math.random() * 3);

console.log(colors['color2'] + randomNumber);

/*
Con la notación de corchetes se puede acceder y crear propiedades nuevas con operadores de asignación
*/

colors['color1'] = 'black';
console.log(colors);
