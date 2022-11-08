class Card:
    id: int
    number: str
    cvv: int
    date: str

    def __init__(self, id: int, number: str, cvv: int, date: str) -> None:
        self.id = id
        self.number = number
        self.cvv = cvv
        self.date = date