/*
Al tener acceso a un elemento, podemos cambiar su estilo, utilizando la propiedad style.
*/

//Modificando la propiedad de CSS
const cambiarColor = () => {
  document.getElementById('p1').style.color = '#09f';
};

const cambiarTexto = () => {
  let text = document.getElementById('p1');

  text.style.fontWeight = 'bold';
};

//Agregar clases
const cambiarColor2 = () => {
  document.getElementById('d1').classList.add('div1');
};
