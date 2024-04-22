//document.getElementById o sólo id -> El id debe ser único
const elemento = document.getElementById('elemento');
elemento.style.background = '#0f0';

//querySelectorAll -> Devuelve todos los elementos que coinciden con el selector CSS dado.
//querySelector -> Devuelve el primer elemento para el selector CSS dado.
let elements = document.querySelectorAll('ul > li:last-child');
for (let elem of elements) {
  console.log(elem.innerHTML);
}

//matches -> Devuelve true o false
for (let elem of document.body.children) {
  if (elem.matches('a[href$="zip"]')) {
    console.log('La referencia del archivo es: ' + elem.href);
  }
}

//closest -> Busca el ancestro más cercano que coincide con el selector CSS
let chapter = document.querySelector('.chapter');
console.log(chapter.closest('.book'));
console.log(chapter.closest('.contents'));
console.log(chapter.closest('h1')); //null -> h1 no es un ancestro

/*
MÉTODOS DE getElements:
- getElementsByTagName(tag) -> Busca elementos con la etiqueta dada y devuelve una colección con ello.
- getElementsByClassName(className) -> Devuelve elementos con la clase dada.
- getElementsByName(name) -> Devuelve elementos con el atributo 'name' dado, en todo el document. Muy raramente usado.
*/

//Obtener todos los 'div' del documento
let divs = document.getElementsByTagName('div');

/*
MÉTODO:                  
querySelector -> Selector css
querySelectorAll -> Selector css
getElementById -> Id
getElementsByName -> Name
getElementsByTagName -> Etiqueta o '*'
getElementsByClassName -> Class

Los más utilizados son querySelector y querySelectorAll, getElementById (¡Puede encontrarse en un script antiguo!)
*/
