let alumnos = [
  {
    nombre: "Luca Dalto",
    email: "soydalto@gmail.com",
    materia: "Fisica 3",
  },
  {
    nombre: "Karin Guerra",
    email: "karin@gmail.com",
    materia: "Fisica 1",
  },
  {
    nombre: "Jorge Ramirez",
    email: "ramirez@gmail.com",
    materia: "Cálculo 2",
  },
  {
    nombre: "Fernando Roberto",
    email: "roberto@gmail.com",
    materia: "Literatura",
  },
  {
    nombre: "Cofla",
    email: "soydalto@gmail.com",
    materia: "Recreo",
  },
];

const boton = document.querySelector(".boton-confirmar");
const contenedor = document.querySelector(".grid-container");

boton.addEventListener("click", () => {
  let confirmar = confirm("¿Realmente quieres confirmar las mesas?");
  if (confirmar) {
    //Eliminando boton
    document.body.removeChild(boton);
    //Selecciona todos los elementos de semana
    let elementos = document.querySelectorAll(".semana");
    let semanasElegidas = document.querySelectorAll(".semana-elegida");
    for (let elemento in elementos) {
      semana = elementos[elemento];
      semana.innerHTML = semanasElegidas[elemento].value;
    }
  }
});

for (let alumno in alumnos) {
  let datos = alumnos[alumno];
  let nombre = datos["nombre"];
  let email = datos["email"];
  let materia = datos["materia"];
  let htmlCode = `
  <div class="grid-item nombre">${nombre}</div>
      <div class="grid-item email">${email}</div>
      <div class="grid-item materia">${materia}</div>
      <div class="grid-item semana">
        <select class="semana-elegida">
          <option value="Semana 1">Semana 1</option>
          <option value="Semana 2">Semana 2</option>
        </select>
      </div>`;
  contenedor.innerHTML += htmlCode;
}
