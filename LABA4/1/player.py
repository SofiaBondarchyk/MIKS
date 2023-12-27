from StandingState import StandingState
from LyingState import LyingState
from RunningState import RunningState
from LongJumpingState import LongJumpingState
from q import update_player_state_text


class Player:
    def __init__(self): 
        self.standing_state = StandingState()  # Initialize standing state
        self.running_state = RunningState()  # Initialize running state
        self.long_jumping_state = LongJumpingState()  # Initialize long jumping state
        self.state = self.standing_state  # Set initial state to standing


    def squat(self):
        self.state = self.state.handle_squat()

    def jump(self):
        self.state.handle_jump()

    def run(self):
        self.state = self.running_state
        update_player_state_text("Running started")

    def end_run(self):
        self.state = self.standing_state
        update_player_state_text("Running stopped")

    def long_jump(self):
        self.state = self.long_jumping_state
        update_player_state_text("Long jump started")

    def end_long_jump(self):
        self.state = self.standing_state
        update_player_state_text("Long jump stopped")

    def get_state_text(self):
        return str(self.state) # Get textual representation of current player state