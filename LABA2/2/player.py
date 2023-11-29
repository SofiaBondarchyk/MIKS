class Player:
    def __init__(self, position):
        self.position = position

    def clone(self):
        pass

class Goalkeeper(Player):
    def clone(self):
        return Goalkeeper(self.position)

class Defender(Player):
    def clone(self):
        return Defender(self.position)

class Midfielder(Player):
    def clone(self):
        return Midfielder(self.position)

class Forward(Player):
    def clone(self):
        return Forward(self.position)
