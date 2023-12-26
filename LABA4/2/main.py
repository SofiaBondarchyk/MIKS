from car_options import CarOptions
from add_option_command import AddOptionCommand
from option_category import OptionCategory
from car_configurator import CarConfigurator


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
