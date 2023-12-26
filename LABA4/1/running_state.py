from main import update_player_state_text  # Додайте цей рядок

class RunningState:
    def handle_run(self):
        update_player_state_text("Продовження бігу")
        return self

    def handle_squat(self):
        update_player_state_text("Присідання під час бігу")
        return self

    def handle_lie_down(self):
        update_player_state_text("Лягання під час бігу")
        return self

    def handle_long_jump(self):
        update_player_state_text("Стрибок під час бігу")
        return self

    def handle_stand(self):
        update_player_state_text("Зупинка під час бігу")
        return self