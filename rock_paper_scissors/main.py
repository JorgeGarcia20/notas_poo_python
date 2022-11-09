class Participant:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.__choice__ = ""

    
    def choose(self):
        self.choice = input(f'{self.name} select rock, paper, scissors, lizard or spock: ')
        print(f'{self.name} selects {self.choice}')


    def to_numerical_choice(self):
        switcher = {
            "rock": 0,
            "paper": 1,
            "scissor": 2,
            "lizard": 3,
            "spock": 4
        }
        return switcher[self.choice]


    def increment_point(self):
        self.points += 1


class GameRound:
    def __init__(self, p1, p2):
        self.rules = [
            [0, -1, 1, 1, -1],
            [1, 0, -1, -1, 1],
            [-1, 1, 0, 1, -1],
            [-1, 1, -1, 0, 1],
            [1, -1, 1, -1, 0]
        ]
        p1.choose()
        p2.choose()
        result = self.compare_choices(p1, p2)
        print(f'Round resulted in a {self.get_result_as_string(result)}')

        if result > 0:
            p1.increment_point()
        elif result < 0:
            p2.increment_point()
        

    def compare_choices(self, p1, p2):
        return self.rules[p1.to_numerical_choice()][p2.to_numerical_choice()]


    def get_result_as_string(self, result):
        res = {
            0: "draw",
            1: "win",
            -1: "loss"
        }
        return res[result]
    
    def award_points(self):
        print('implement')


class Game:
    def __init__(self) -> None:
        self.end_game = False
        self.participant = Participant("Jor")
        self.second_participand = Participant("Albert")

    
    def start(self):
        while not self.end_game:
            GameRound(self.participant, self.second_participand)
            self.check_end_condition()
    
    def check_end_condition(self):
        answer = input("Continue game [y/n]: ")
        if answer == 'y':
            GameRound(self.participant, self.second_participand)
            self.check_end_condition()
        else:
            print(f"Game ended, {self.participant.name} has {self.participant.points}\n{self.second_participand.name} has {self.second_participand.points}")
            self.determine_winner()
            self.end_game = True

    
    def determine_winner(self):
        result_string = "It's a Draw"

        if self.participant.points > self.second_participand.points:
            result_string = f"Winner is {self.participant.name}"
        elif self.participant.points < self.second_participand.points:
            result_string = f"Winner is {self.second_participand.name}"
        
        print(result_string)


game = Game()
game.start()