import { Account } from "./Account.js";
// import {Car} from "./Car.js"
import { UberX } from "./UberX.js";


// let car1 = new Car(2234, "Jorge");
// car1.printDataCar()

let user1 = new Account('Jorge', 'ADN6473', 'jorge@algo.com')
let uber1 = new UberX("JOR4632", user1, 'Ford', 'Fiesta')
uber1.printDataCar()