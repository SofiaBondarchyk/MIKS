from player import Player


class Midfielder(Player):
    def clone(self):
        return Midfielder(self.position)
