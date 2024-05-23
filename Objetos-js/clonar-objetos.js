/*
Existen dos mecanismos para copiar objtetos, para cambiar uno y dejar intacto el original:

1. Copia por VALOR -> Duplica el contenido (Tipos de datos primitivos, number, string, boolean, null, undefined)
2. copia por REFERENCIA -> Hace a dónde está el contenido (Tipos de datos no primitivos)
*/

//Copia por valor
let originalValue = 42;
let copyValue = originalValue;

//Alterar el valor de copyValue
copyValue = 100;

console.log(originalValue);
console.log(copyValue);

//Copia por referencia
let originalReference = { name: 'ManzDev' };
//Supuesta copia de origianlReference
let copyReference = originalReference;

//Alterar el valor de copyReference
copyReference.name = 'Midudev';
console.log(originalReference);
console.log(copyReference);

/*
CLONANDO VARIABLES O CONSTANTES:
- Clonado Superficial (SHALLOW CLONE): Se llama así cuando realizamos una clonación de una estructura de datos y sólo se copia su primer nivel, mientras que el segundo y niveles más profundos, se crean referencias.
- Clonado Profunda (DEEP CLONE): Se llama así cuando realizamos una clonación de una estructura de datos a todos sus niveles.
*/

const DATA = {
  //Se clona en superficial y en profundida
  name: 'ManzDev',
  tired: false,
  //Sólo en profundidad
  likes: ['css', 'html', 'js', 'vue'],
  numbers: [4, 8, 15, 16, 23, 42],
};
