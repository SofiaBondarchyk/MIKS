from main import update_player_state_text  


# Class representing the state of a player while running.
class RunningState:
    def handle_run(self):
        update_player_state_text("Continuing to run")
        return self

    def handle_squat(self):
        update_player_state_text("Squatting while running")
        return self

    def handle_lie_down(self):
        update_player_state_text("Lying down while running")
        return self

    def handle_long_jump(self):
        update_player_state_text("Jumping while running")
        return self

    def handle_stand(self):
        update_player_state_text("Stopping while running")
        return self
