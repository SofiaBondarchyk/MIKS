from car_options import CarOptions
from add_option_command import AddOptionCommand
from option_category import OptionCategory
from car_configurator import CarConfigurator


# Create option categories.
interior_category = OptionCategory("Interior")
exterior_category = OptionCategory("Exterior")
safety_category = OptionCategory("Safety")

# Create several options for each category.
leather_seats = CarOptions("Leather Seats", 1500)
sunroof = CarOptions("Sunroof", 1200)
backup_camera = CarOptions("Backup Camera", 800)
blind_spot_monitoring = CarOptions("Blind Spot Monitoring", 1000)

# Add options to categories.
interior_category.add_option(leather_seats)
exterior_category.add_option(sunroof)
safety_category.add_option(backup_camera)
safety_category.add_option(blind_spot_monitoring)

# Create a configurator and add categories to it.
configurator = CarConfigurator()
configurator.add_category(interior_category)
configurator.add_category(exterior_category)
configurator.add_category(safety_category)

# Create commands for adding options.
add_leather_seats = AddOptionCommand(leather_seats, interior_category)
add_sunroof = AddOptionCommand(sunroof, exterior_category)
add_blind_spot_monitoring = AddOptionCommand(blind_spot_monitoring, safety_category)

# Execute commands to add options.
add_leather_seats.execute()
add_sunroof.execute()
add_blind_spot_monitoring.execute()

# Display the state of the configurator.
configurator.configure_car()

# Undo the command for the "Safety" category.
add_blind_spot_monitoring.undo()

# Display the updated state of the configurator.
configurator.configure_car()