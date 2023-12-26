from utils import update_player_state_text


# Class representing the state of a player while standing.
class StandingState:
    def handle_squat(self):
        from squatting_state import SquattingState
        update_player_state_text("Squatting")
        return SquattingState()

    def handle_jump(self):
        update_player_state_text("Normal jump")

    def handle_run(self):
        update_player_state_text("Normal run")

    def __str__(self):
        return "Standing"
