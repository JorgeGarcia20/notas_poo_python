class PayPal:
    id: int
    email: str

    def __init__(self, id: int, email: str) -> None:
        self.id = id
        self.email = email