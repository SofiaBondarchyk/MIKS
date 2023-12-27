from q import update_player_state_text


class LyingState:
    def handle_squat(self):
        update_player_state_text("Lying - cannot squat further")
        return self

    def handle_jump(self):
        update_player_state_text("Cannot jump from lying state")

    def handle_run(self):
        update_player_state_text("Cannot run from lying state")

    def __str__(self):
        return "Lying"  # Textual representation of the state