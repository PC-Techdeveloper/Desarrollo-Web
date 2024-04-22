//ClassName -> Atributo 'class'.
//classList -> Métodos que Permite agregar, eliminar y alterar una sola clase.

//Atributo class del documento del body:
console.log(document.body.className);
//Agregar una clase:
document.body.classList.add('article');
document.write(document.body.className);

/*
MÉTODOS DE CLASSLIST:
- elem.classList.add/remove('class') -> Agrega o remueve la clase.
- elem.classList.toggle('class') -> Agrega la clase si no existe, si no la remueve.
- elem.classList.contains('class') -> Verifica si tiene la clase dada, devuelve true/false.
*/

//Además, classList es iterable:
for (let name of document.body.classList) {
  console.log(name);
}

//Style de un documento: Es un objeto que corresponde a lo escrito en el atributo 'style'.
//Para propiedades de varias palabras se usa camelCase:
// document.body.style.backgroundColor = prompt('background-color', 'green');

//RESETEANDO LA PROPIEDAD STYLE:
//Para ocultar un elemento, se establece display = 'none'
// document.body.style.display = 'none';
// setTimeout(() => {
//   document.body.style.dislay = '';
// }, 1000);

//QUITAR PROPIEDADES CON REMOVEPROPERTY('PROPERTY')
//Ocultar background después de 1 segundo
document.body.style.backgroundColor = 'blue';
setTimeout(() => {
  document.body.style.removeProperty('background');
}, 1000);

//REESCRIBIR TODO USANDO -> style.cssText
//Establecer estilos especiales con banderas como '!important'
// let div = document.getElementById('button');
// div.style.cssText = `color: red !important
//   background-color: yellow;
//   width: 100px;
//   text-align: center;
// `;

// console.log(div.style.cssText);
