from Account import Account

class Car:
    id: int
    license: str
    driver: Account
    passengers: int

    def __init__(self,license: str, driver: Account) -> None:
        self.license = license
        self.driver = driver

    def print_data_car(self):
        print(f'License: {self.license}\nDriver name: {self.driver.name}\n')