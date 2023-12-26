from main import update_player_state_text  # Додайте цей рядок

class LyingState:
    def handle_run(self):
        update_player_state_text("Біг під час лежання")
        return self

    def handle_squat(self):
        update_player_state_text("Присідання під час лежання")
        return self

    def handle_lie_down(self):
        update_player_state_text("Продовження лежання")
        return self

    def handle_long_jump(self):
        update_player_state_text("Стрибок під час лежання")
        return self

    def handle_stand(self):
        update_player_state_text("Вставання з лежачого положення")
        return self