/*
CREACIÓN DE ELEMENTOS - MÉTODOS:
- createElement() -> Crea un elemento HTML .

- createTexNode -> Crea un nuevo nodo de texto. Es usado para escapar carácteres.

- createDocumentFragment() -> Crea un nuevo fragmento vacío, dentro del cual un nodo del DOM puede ser adicionado para construir un nuevo árbol DOM fuera de la pantalla.

- appendChild() -> Agrega un nuevo nodo al final de la lista de un elemento hijo de un elemento padre específicado.

*/
//Crear un elemento
const contenedor = document.querySelector('.contenedor');
const fragmento = document.createDocumentFragment();

for (i = 0; i < 20; i++) {
  const item = document.createElement('LI');
  item.innerHTML = 'Este es un item de la lista';
  fragmento.appendChild(item);
}
//Agregando el elemento
contenedor.appendChild(fragmento);
