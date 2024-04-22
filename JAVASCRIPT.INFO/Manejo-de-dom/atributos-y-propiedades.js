//PROPIEDADES DEL DOM
//Los nodos DOM son objetos de JavaScript normales, puede ser alterado!
document.body.myData = {
  name: 'Cesar',
  title: 'Emperador',
};
console.log(document.body.myData.title);

//También podemos agregar un método
document.body.sayTagName = function () {
  console.log(this.tagName); //Valor de 'this' -> BODY
};
document.body.sayTagName();
//Modificar prototipos incorporados y agregar nuevos métodos a todos los elementos
Element.prototype.sayHi = function () {
  console.log(`Hola, yo soy ${this.tagName}`);
};
document.documentElement.sayHi();
document.body.sayHi();

//ATRIBUTOS HTML -> Cuando un elemento tiene 'id' u otro atributo estándar
//Se crea la propiedad correspondiente. Pero eso no ocurre si el atributo no es
//estándar
document.body.id;
document.body.something;
//Atributos estándar
console.log(input.type);
/*
MÉTODOS PARA TRABAJAR CON ATRIBUTOS:
- elem.hasAttribute(nombre) -> Comprueba si existe.
- elem.getAttribute(nombre) -> Obtiene el valor.
- elem.setAttribute(nombre, valor) -> Eatablece el valor.
- elem.removeAttribute(nombre) -> Elimina el atributo.
- elem.attributes -> Lee todos los atributos (nombre, valor).
*/
console.log(document.body.getAttribute('something'));
