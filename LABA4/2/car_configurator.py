from option_category import OptionCategory


# Define a class representing a CarConfigurator.
class CarConfigurator:
    # Constructor method to initialize the CarConfigurator instance.
    def __init__(self):
        self.categories = []

    def add_category(self, category):
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
