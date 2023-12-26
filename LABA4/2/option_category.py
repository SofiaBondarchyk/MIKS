from car_options import CarOptions


class OptionCategory:
    def __init__(self, name):
        self.name = name
        self.options = []

    def add_option(self, option):
        self.options.append(option)

    def remove_option(self, option):
        self.options.remove(option)
