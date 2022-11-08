from Car import Car
from Account import Account

class UberPool(Car):
    brand: str
    model: str
    
    def __init__(self, license: str, driver: Account, brand: str, model: str) -> None:
        super().__init__(license, driver)
        self.brand = brand
        self.model = model