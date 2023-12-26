from abc import ABC, abstractmethod

# Опції авто
class CarOptions:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Команда для додавання опції
class AddOptionCommand:
    def __init__(self, option, category):
        self.option = option
        self.category = category

    def execute(self):
        self.category.add_option(self.option)

    def undo(self):
        self.category.remove_option(self.option)

# Категорія опцій
class OptionCategory:
    def __init__(self, name):
        self.name = name
        self.options = []

    def add_option(self, option):
        self.options.append(option)

    def remove_option(self, option):
        self.options.remove(option)

# Конфігуратор
class CarConfigurator:
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

# Створюємо категорії опцій
interior_category = OptionCategory("Interior")
exterior_category = OptionCategory("Exterior")
safety_category = OptionCategory("Safety")

# Створюємо декілька опцій для кожної категорії
leather_seats = CarOptions("Leather Seats", 1500)
sunroof = CarOptions("Sunroof", 1200)
backup_camera = CarOptions("Backup Camera", 800)
blind_spot_monitoring = CarOptions("Blind Spot Monitoring", 1000)

# Додаємо опції до категорій
interior_category.add_option(leather_seats)
exterior_category.add_option(sunroof)
safety_category.add_option(backup_camera)
safety_category.add_option(blind_spot_monitoring)

# Створюємо конфігуратор та додаємо категорії до нього
configurator = CarConfigurator()
configurator.add_category(interior_category)
configurator.add_category(exterior_category)
configurator.add_category(safety_category)

# Створюємо команди для додавання опцій
add_leather_seats = AddOptionCommand(leather_seats, interior_category)
add_sunroof = AddOptionCommand(sunroof, exterior_category)
add_blind_spot_monitoring = AddOptionCommand(blind_spot_monitoring, safety_category)

# Викликаємо команди для додавання опцій
add_leather_seats.execute()
add_sunroof.execute()
add_blind_spot_monitoring.execute()

# Виводимо стан конфігуратора
configurator.configure_car()

# Викликаємо команду для скидання категорії "Safety"
add_blind_spot_monitoring.undo()

# Виводимо оновлений стан конфігуратора
configurator.configure_car()
