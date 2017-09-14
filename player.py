class Player():
    def __init__(self,name):
        self.name=name
        self.wins = 0
        self.losses = 0
        self. ties = 0

    def get_name(self):
        return self.name


class Human_Player(Player):
        pass

class Ai_Player(Player):
        pass
