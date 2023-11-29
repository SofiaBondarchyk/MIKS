from player import Player


class Defender(Player):
    def clone(self):
        return Defender(self.position)
