from q import update_player_state_text
from Player import Player


class RunningState:
    def handle_squat(self):
        update_player_state_text("Squatting while running")
        return self

    def handle_jump(self):
        update_player_state_text("Long jump")

    def handle_run(self):
        update_player_state_text("Continue running")

    def __str__(self):
        return "Running"  # Textual representation of the state