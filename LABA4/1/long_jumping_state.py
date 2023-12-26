from main import update_player_state_text  

# Class representing the state of a player during a long jump.
class LongJumpingState:
    def handle_run(self):
        update_player_state_text("Running during long jump")
        return self

    def handle_squat(self):
        update_player_state_text("Squatting during long jump")
        return self

    def handle_lie_down(self):
        update_player_state_text("Lying down during long jump")
        return self

    def handle_long_jump(self):
        update_player_state_text("Continuing the long jump")
        return self

    def handle_stand(self):
        update_player_state_text("Standing up during long jump")
        return self
