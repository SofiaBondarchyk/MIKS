from SquattingState import SquattingState
from q import update_player_state_text


class StandingState:
    def handle_squat(self):
        update_player_state_text("Squatting")
        return SquattingState()

    def handle_jump(self):
        update_player_state_text("Normal jump")

    def handle_run(self):
        update_player_state_text("Normal run")

    def __str__(self):
        return "Standing"  # Textual representation of the state