from LyingState import LyingState
from q import update_player_state_text


class SquattingState:
    def handle_squat(self):
        update_player_state_text("Lying down")
        return LyingState()

    def handle_jump(self):
        update_player_state_text("Jump from squatting position")

    def handle_run(self):
        update_player_state_text("Rolling")

    def __str__(self):
        return "Squatting"  # Textual representation of the state