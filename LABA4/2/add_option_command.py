from abc import ABC, abstractmethod
from car_options import CarOptions

# Define a class representing an AddOptionCommand.
class AddOptionCommand:
    # Constructor method to initialize the AddOptionCommand instance.
    def __init__(self, option, category):
        # Store the option and category associated with the command.
        self.option = option
        self.category = category

    # Method to execute the command, adding the option to the category.
    def execute(self):
        self.category.add_option(self.option)

    # Method to undo the command, removing the option from the category.
    def undo(self):
        self.category.remove_option(self.option)
