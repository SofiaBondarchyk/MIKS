from squatting_state import SquattingState
from lying_state import LyingState
from running_state import RunningState
from long_jumping_state import LongJumpingState
from standing_state import StandingState
from main import update_player_state_text


class Player:
    def __init__(self):
        self.standing_state = StandingState()
        self.running_state = RunningState()
        self.long_jumping_state = LongJumpingState()
        self.state = self.standing_state

    def squat(self):
        self.state = self.state.handle_squat()

    def jump(self):
        self.state.handle_jump()

    def run(self):
        self.state = self.running_state
        update_player_state_text("Початок бігу")

    def end_run(self):
        self.state = self.standing_state
        update_player_state_text("Зупинка бігу")

    def long_jump(self):
        self.state = self.long_jumping_state
        update_player_state_text("Початок довгого стрибка")

    def end_long_jump(self):
        self.state = self.standing_state
        update_player_state_text("Зупинка довгого стрибка")

    def get_state_text(self):
        return str(self.state)
