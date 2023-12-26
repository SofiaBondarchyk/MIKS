from abc import ABC, abstractmethod
from car_options import CarOptions


class AddOptionCommand:
    def __init__(self, option, category):
        self.option = option
        self.category = category

    def execute(self):
        self.category.add_option(self.option)

    def undo(self):
        self.category.remove_option(self.option)
