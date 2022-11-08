class Account {
    
    constructor(name, document, email){
        this.id = id;
        this.name = name;
        this.document = document;
        this.email = email;
        this.password;
    }

    printDataCar() {
        console.log(this.name)
        console.log(this.document)
        console.log(this.email)
    }
}

export {Account}