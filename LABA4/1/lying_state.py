from main import update_player_state_text  

# Class representing the state of a player while lying down.
class LyingState:
    # Method to handle running while lying down.
    def handle_run(self):
        update_player_state_text("Running while lying down")
        return self

    # Method to handle squatting while lying down.
    def handle_squat(self):
        update_player_state_text("Squatting while lying down")
        return self

    # Method to handle continuing lying down.
    def handle_lie_down(self):
        update_player_state_text("Continuing to lie down")
        return self

    # Method to handle long jump while lying down.
    def handle_long_jump(self):
        update_player_state_text("Jumping while lying down")
        return self

    # Method to handle standing up from a lying position.
    def handle_stand(self):
        update_player_state_text("Standing up from lying position")
        return self