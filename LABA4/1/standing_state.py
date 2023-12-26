from utils import update_player_state_text

class StandingState:
    def handle_squat(self):
        from squatting_state import SquattingState
        update_player_state_text("Присідання")
        return SquattingState()

    def handle_jump(self):
        update_player_state_text("Звичайний стрибок")

    def handle_run(self):
        update_player_state_text("Звичайний біг")

    def __str__(self):
        return "Стійка"