import { Car } from "./Car";

class UberVan extends Car{
    constructor(license, driver, typeCarAccepted, seatsMaterial){
        super(license, driver)
        this.typeCarAccepted = typeCarAccepted
        this.seatsMaterial = seatsMaterial
    }
}

export {UberVan}