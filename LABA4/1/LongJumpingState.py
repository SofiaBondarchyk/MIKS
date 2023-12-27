from q import update_player_state_text


class LongJumpingState:
    def handle_squat(self):
        update_player_state_text("Cannot squat during long jump")
        return self

    def handle_jump(self):
        update_player_state_text("Jump during long jump")

    def handle_run(self):
        update_player_state_text("Cannot run during long jump")

    def __str__(self):
        return "Long jump"  # Textual representation of the state