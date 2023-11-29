from player import Player


class Forward(Player):
    def clone(self):
        return Forward(self.position)
