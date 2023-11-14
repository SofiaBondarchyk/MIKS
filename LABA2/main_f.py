# main.py
import tkinter as tk
from player import Goalkeeper, Defender, Midfielder, Forward
from football_team import TeamFormation, FootballTeam

# Функція для виведення інформації про команду у спливаючому вікні
def show_team_info(team):
    team_info = f"{team.name} ({team.formation.formation}):\n"
    for player in team.players:
        team_info += f"{player.position}\n"

    info_window = tk.Toplevel(root)
    info_window.title("Team Info")
    label = tk.Label(info_window, text=team_info)
    label.pack()

# Приклад створення гравців і команд на основі прототипів:
def main():
    goalkeeper_prototype = Goalkeeper("Goalkeeper")
    defender_prototype = Defender("Defender")
    midfielder_prototype = Midfielder("Midfielder")
    forward_prototype = Forward("Forward")

    formation_4_3_3 = TeamFormation("4-3-3")
    formation_4_4_2 = TeamFormation("4-4-2")

    team_a = FootballTeam("Team A", formation_4_3_3)
    team_b = FootballTeam("Team B", formation_4_4_2)

    team_a.add_player(goalkeeper_prototype.clone())
    team_a.add_player(defender_prototype.clone())
    team_a.add_player(midfielder_prototype.clone())
    team_a.add_player(forward_prototype.clone())
    team_a.add_player(midfielder_prototype.clone())
    team_a.add_player(defender_prototype.clone())
    team_a.add_player(midfielder_prototype.clone())
    team_a.add_player(forward_prototype.clone())
    team_a.add_player(forward_prototype.clone())

    team_b.add_player(goalkeeper_prototype.clone())
    team_b.add_player(defender_prototype.clone())
    team_b.add_player(defender_prototype.clone())
    team_b.add_player(midfielder_prototype.clone())
    team_b.add_player(midfielder_prototype.clone())
    team_b.add_player(midfielder_prototype.clone())
    team_b.add_player(midfielder_prototype.clone())
    team_b.add_player(forward_prototype.clone())
    team_b.add_player(forward_prototype.clone())

    # Виведення інформації про команди у спливаючих вікнах
    show_team_info(team_a)
    show_team_info(team_b)

if __name__ == "__main__":
    root = tk.Tk()
    main()
    root.mainloop()
