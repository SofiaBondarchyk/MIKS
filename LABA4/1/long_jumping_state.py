from main import update_player_state_text  

class LongJumpingState:
    def handle_run(self):
        update_player_state_text("Біг під час стрибка в довжину")
        return self

    def handle_squat(self):
        update_player_state_text("Присідання під час стрибка в довжину")
        return self

    def handle_lie_down(self):
        update_player_state_text("Лягання під час стрибка в довжину")
        return self

    def handle_long_jump(self):
        update_player_state_text("Продовження стрибка в довжину")
        return self

    def handle_stand(self):
        update_player_state_text("Вставання під час стрибка в довжину")
        return self