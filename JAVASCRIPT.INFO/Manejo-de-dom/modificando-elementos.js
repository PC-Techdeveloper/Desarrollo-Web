//Creando un elemento
let div = document.createElement('div');
//Creando un nodo con texto
let textNode = document.createTextNode('Aquí estoy!');
//Creando el mensaje
div.className = 'Alert!';
div.innerHTML = '<strong>!Hola?</strong> Usted ha leído un importante mensaje!';

//MÉTODOS DE INSERCIÓN -> Insertar el div en algún lado dentro del document, con el método append()
/*
- node.append(..nodos o strings) -> Agrega nodos o strings AL FINAL DE NODE.
- node.prepend(..nodos o strings) -> Inserta nodos o strings AL PRINCIPIO DE NODE.
- node.before(..nodos o strings) -> Inserta nodos o strings ANTES DE NODE.
- node.after(..nodos o strings) -> Inserta nodos o strings DESPUÉS DE NODE.
- node.replaceWith(..nodos o strings) -> Reemplaza node con los nodos o strings dados.
*/
document.body.append(textNode);
