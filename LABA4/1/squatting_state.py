from main import update_player_state_text
from lying_state import LyingState
from main import update_player_state_text

# Class representing the state of a player while squatting.
class SquattingState:
    def handle_squat(self):
        update_player_state_text("Lying down")
        return LyingState()

    def handle_jump(self):
        update_player_state_text("Jump from squatting")

    def handle_run(self):
        update_player_state_text("Rolling up")

    def __str__(self):
        return "Squatting"
