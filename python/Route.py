class Route:
    id: int
    star: list
    end: list

    def __init__(self, id: int, star: list,  end: list) -> None:
        self.id = id
        self.star = star
        self.end = end