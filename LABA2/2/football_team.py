from team_formation import TeamFormation


class FootballTeam:
    def __init__(self, name, formation):
        # Constructor for FootballTeam class.
        self.name = name
        self.formation = formation
        self.players = []

    def add_player(self, player):
        # Add a player to the football team.
        self.players.append(player)

    def clone(self):
        # Clone the football team.
        team_copy = FootballTeam(self.name, self.formation.clone())
        for player in self.players:
            team_copy.add_player(player.clone())
        return team_copy
