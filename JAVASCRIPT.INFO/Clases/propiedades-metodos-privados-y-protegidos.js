/*
En JavaScript hay dos tipos de campos de objeto (Propiedad y métodos):

PÚBLICO: Accesible desde cualquier lugar -> Interfaz externa
PRIVADO: Accesible solo desde dentro de la clase -> Interfaz interna
*/

//PROTEFER 'WATERAMOUNT' -> Clase de cafetera
class CoffeMachine {
  waterAmount = 0;
  constructor(power) {
    this.power = power;
    console.log(`Se creo una máquina de café, porder: ${power}`);
  }
}
//Se crea la máquina de café
let myCoffe = new CoffeMachine(200);
//Se agrega agua
CoffeMachine.waterAmount = 400;
console.log(CoffeMachine);

//PROPIEDAD PRIVADA -> _
class CoffeeMachineTwo {
  _waterAmount = 0;

  set waterAmount(value) {
    if (value < 0) {
      value = 0;
    }
    this._waterAmount = value;
  }

  get waterAmount() {
    return this._waterAmount;
  }

  constructor(power) {
    this._power = power;
  }
}

//Se crea la máquina de café
let myCoffeTwo = new CoffeeMachineTwo(100);
console.log(myCoffeTwo);
//Se agrega agua
myCoffe.waterAmount = -10;
console.log(CoffeeMachineTwo);
