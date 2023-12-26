from abc import ABC, abstractmethod

# Car options class representing individual options with a name and price.
class CarOptions:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Command class for adding options to a category.
class AddOptionCommand:
    def __init__(self, option, category):
        self.option = option
        self.category = category

    def execute(self):
        # Execute the command by adding the option to the category.
        self.category.add_option(self.option)

    def undo(self):
        # Undo the command by removing the option from the category.
        self.category.remove_option(self.option)

# Option category class representing a category of options with a name and a list of options.
class OptionCategory:
    def __init__(self, name):
        self.name = name
        self.options = []

    def add_option(self, option):
        # Add an option to the category.
        self.options.append(option)

    def remove_option(self, option):
        # Remove an option from the category.
        self.options.remove(option)

# Car configurator class managing option categories and providing a method to display configured options.
class CarConfigurator:
    def __init__(self):
        self.categories = []

    def add_category(self, category):
        # Add a category to the configurator.
        self.categories.append(category)

    def configure_car(self):
        total_price = 0
        for category in self.categories:
            print(f"{category.name}:")
            for option in category.options:
                print(f"  - {option.name}: ${option.price}")
                total_price += option.price
            print()
        print(f"Total Price: ${total_price}")

# Creating option categories
interior_category = OptionCategory("Interior")
exterior_category = OptionCategory("Exterior")
safety_category = OptionCategory("Safety")

# Creating options for each category
leather_seats = CarOptions("Leather Seats", 1500)
sunroof = CarOptions("Sunroof", 1200)
backup_camera = CarOptions("Backup Camera", 800)
blind_spot_monitoring = CarOptions("Blind Spot Monitoring", 1000)

# Adding options to categories
interior_category.add_option(leather_seats)
exterior_category.add_option(sunroof)
safety_category.add_option(backup_camera)
safety_category.add_option(blind_spot_monitoring)

# Creating a configurator and adding categories to it
configurator = CarConfigurator()
configurator.add_category(interior_category)
configurator.add_category(exterior_category)
configurator.add_category(safety_category)

# Creating commands for adding options
add_leather_seats = AddOptionCommand(leather_seats, interior_category)
add_sunroof = AddOptionCommand(sunroof, exterior_category)
add_blind_spot_monitoring = AddOptionCommand(blind_spot_monitoring, safety_category)

# Executing commands to add options
add_leather_seats.execute()
add_sunroof.execute()
add_blind_spot_monitoring.execute()

# Displaying the state of the configurator
configurator.configure_car()

# Undoing the command for the "Safety" category
add_blind_spot_monitoring.undo()

# Displaying the updated state of the configurator
configurator.configure_car()