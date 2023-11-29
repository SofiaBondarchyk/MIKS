class TeamFormation:
    def __init__(self, formation):
        self.formation = formation

    def clone(self):
        pass

class FootballTeam:
    def __init__(self, name, formation):
        self.name = name
        self.formation = formation
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def clone(self):
        team_copy = FootballTeam(self.name, self.formation.clone())
        for player in self.players:
            team_copy.add_player(player.clone())
        return team_copy
