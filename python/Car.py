class Car:
    id: int
    license: int
    driver: str
    passengers: int

    def __init__(self, id: int, license: int, driver: str, passengers: int ) -> None:
        self.id = id
        self.license = license
        self.driver = driver
        self.passengers = passengers

    def __str__(self) -> str:
        return f'id: {self.id}\nlicense: {self.license}\nDriver: {self.driver}\nNumber of passengers: {self.passengers}\n'
