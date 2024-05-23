- EXPORTACIÓN DE MÓDULOS

Por defecto, un fichero javascript no tiene módulo de exportación si no se usa un `export`, al menos una vez en el código si se usa el export, tendrá un objeto llamado `Módulo de exportación`, donde puede tener uno o múltiples datos. Existen varias formas de exportar un módulo, pero la más común es usar el `export` de javascript.

`

- export: Declaración de exportación.
- export { name }: Añade el elemento `name` al módulo de exportación.
- export {name as newName}: Añade el elemento `name` al módulo de exportación, pero con un nombre diferente.
- export { n1, n2, n3 }: Añade los elementos `n1`, `n2` y `n3` al módulo de exportación.
- export \* from './file.js': Exporta todos los elementos del módulo `file.js` al módulo de exportación.
- export default: Exporta el módulo como el valor por defecto de un módulo.
  `

- EXPORTACIÓN POST-DECLARACIÓN
  Primero se declara la información y posteriormente se exporta.

let number = 42;
const hello = 'Hello World';
const goodbye = 'Goodbye World';
class CodeBlock {}

export { number, hello as greet, goodbye as bye };

- EXPORTACIÓN EXTERNA
  Se trata de añadir a nuestro módulo de exportación del fichero actual, todos los elementos exportados en otro fichero.

CASO 1: Se exportan todos los elementos del módulo en otro fichero.
export \* from './math.js';

CASO 2: Se exportan elementos del módulo en otro fichero.
export { abs, min, max } from './math.js';

CASO 3: Exporta todo lo exportado en el otro fichero en un objeto con un nombre diferente.
export const number = 42;
export \* as math from './math.js';

- EXPORTACIÓN POR DEFECTO
  Para añadirla, sólo se escribe la palabra `default` tras el `export`. En este caso, se esta creando un elemento en el módulo de exportación con el nombre `default` y es considerado como el elemento principal del módulo. Sólo puede haber un elemento llamado `default` por módulo de exportación, por lo que tampoco se puede hacer más de un `export default` por fichero.

Declaración y exportación -> export const number = 42;
Exportación por defecto -> export default 'Manz';

- IMPORTACIÓN DE MÓDULOS
  import { nombre } from "./file.js" Importa el elemento nombre de file.js.
  import { nombre as newName } from "./file.js" Importa el elemento nombre de file.js como newName.
  import { n1, n2... } from "./file.js" Importa los elementos indicados desde file.js.
  import nombre from "./file.js" Importa el elemento por defecto de file.js como nombre.
  import \* as name from "./file.js" Importa todos los elementos de file.js en el objeto name.
  import "./file.js" Ejecuta el código de file.js. No importa ningún elemento.
  import { name } from "https://web.com/file.js" Descarga el fichero e importa el elemento name de su módulo.

- IMPORTACIÓN CON NOMBRE: La forma más habitual de importar elementos es a través de la denominada importación nombrada, donde se especifica el nombre del elemento que se desea importar con la palabra clave `ìmport` en el interior de las llaves { }, todo ello se le denomina el `Módulo de exportación` del fichero file.js

import { nombre } from "./file.js" -> Se importa el nombre del fichero
import { number, element } from "./file.js" -> Se importan varios elementos
import { brand as brandName } from "./file.js" -> Se importa el elemento brand renombrado brandName

- IMPORTACIÓN POR DEFECTO: Lo único que hace es buscar el elemento llamado `default` en el módulo de exportación y importarlo como el nombre del elemento que se desea importar.

import nombre from "./math.js"

- IMPORTACIÓN MASIVA: Al utilizar el símbolo `*` a la hora de importar, indica que se deben cargar todos los elementos que se exportan en el módulo de exportación. En esta modalidad, es obligatorio utilizar el `as` seguido del nombre del elemento, ya que indica un nombre para crear un objeto que contendrá los elementos importados.

import \* as module from "./file.js"

- IMPORTACIÓN DE CÓDIGO: Sin importar elementos, simplemente se ejecuta el código del fichero que se importa.

import './math.js' -> El navegador lee el código del fichero y procesarlo, sin importar ningún elemento.

- IMPORTACIONES REMOTAS: Que esten en un dominio diferente al nuestro
  import { ceil } from 'https://web.com/lodash.js'

- METADATOS DE MÓDULOS: Cuando nos encontramos en un fichero `.js` que es el módulo, podemos acceder a la propiedad `import.meta` la cual es un objeto que contiene metadatos del módulo en cuestión.

//main.js
import module from './module.js'
//module.js
console.log(import.meta) -> { url: 'https://dominio.com/module.js'}

- BARE IMPORTS (Imports desnudos): Estos ficheros siempre empiezan por `.` o `/` si son ficheros locales, o por `https://` si son ficheros remotos. Los imports desnudos son aquellos que se realizan indicando en `from` un `string` que no comienza por ., / ni http, sino directamente por el nombre de una carpeta o paquete:

'./math.js' -> Fichero local
'../math.js' -> Fichero en la carpeta padre
'/math.js' -> En la raíz del proyecto
'https://web.com/math.js' -> Fichero alojado en una web

import { Howler, Howl } from 'howler' -> Bare import

- IMPORTACIÓN COMMONJS -> ❌ Ya no se utiliza en JavaScript, rara vez se usa.

//module-name.js
module.exports = {'Hello World'}

//index.js
const module = require('./module-name.js')
const package = require('package-name')

- IMPORT DINÁMICO EN JAVASCRIPT

IMPORT ESTÁTICO VS DINÁMICO
import {name} from './module.js' -> Importación estática

import ('./module.js').then(module => console.log(module.name)) -> Importación dinámica, `.then()` devuelve una promesa, por lo que trata de un código asíncrono.

EJEMPLOS DE IMPORTACIÓN DINÁMICO

Opción 1: Se carga functions.js si se cumple la condición

if(number > 42) {
import('./functions.js').then(module => console.log(module.name))
}

Opción 2: Se carga functions.js interpolando la constante

const fileName = 'functions';
import(`./${fileName}.js`).then(module => console.log(module.func))

Opción 3: Se carga aditional.js sólo si el usuario hace click en un botón

const button = document.querySelector('button');
button.addEventListener('click', () => {
import('./aditional.js'), {once: true}
})

El import dinámico nos permite indicar entre los paréntesis del import el nombre del archivo Javascript. A diferencia del import estático, este fichero no se cargará siempre y desde el principio, sino que sólo lo hará cuando se llegue a esta parte del código, siendo posible incluirla dentro de condicionales, funciones o lógica diversa.

Si el archivo .js importado es un módulo, al trabajar con la promesa que devuelve simplemente accedemos a las propiedades o métodos que necesitemos. Por otro lado, si el archivo .js cargado no es un módulo, simplemente se ejecutará su contenido.
