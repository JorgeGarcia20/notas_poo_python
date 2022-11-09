import { Car } from "./Car";

class UberX extends Car{
    constructor(license, driver, brand, model){
        super(license, driver)
        this.brand = brand
        this.model = model
    }
}

export{UberX}