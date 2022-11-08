class Account:
    id: int
    name: str
    document: str
    email: str
    password: str

    def __init__(self, id: int, name: str, document: str, email: str, password: str) -> None:
        self.id = id
        self.name = name
        self.document = document
        self.email = email
        self.password = password