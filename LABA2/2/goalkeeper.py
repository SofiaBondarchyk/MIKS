from player import Player


class Goalkeeper(Player):
    def clone(self):
        return Goalkeeper(self.position)
