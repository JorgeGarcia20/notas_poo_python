from Car import Car
from Account import Account

class UberVan(Car):
    typeCarAccepted: list
    seatsMaterial: list
    
    def __init__(self, license: str, driver: Account, typeCarAccepted: list, seatsMaterial: list) -> None:
        super().__init__(license, driver)
        self.typeCarAccepted = typeCarAccepted
        self.seatsMaterial = seatsMaterial