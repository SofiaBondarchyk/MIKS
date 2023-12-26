from main import update_player_state_text  # Додайте цей рядок
from lying_state import LyingState  # Додайте цей рядок
from main import update_player_state_text

class SquattingState:
    def handle_squat(self):
        update_player_state_text("Лежання")
    def handle_squat(self):
        update_player_state_text("Лежання")
        return LyingState()

    def handle_jump(self):
        update_player_state_text("Стрибок з присідання")

    def handle_run(self):
        update_player_state_text("Підкат")

    def __str__(self):
        return "Присідання"