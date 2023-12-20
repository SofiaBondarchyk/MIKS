from user import User


class Adapter:
    def __init__(self, user):
        self.user = user

    def register(self, weight, height, system):
        if system == "imperial":
            weight, height = convert_to_metric(weight, height)
        self.user.weight = weight
        self.user.height = height

    def display(self):
        return self.user.display()

    def exchange_data(self):
        return "Sending data to the server..."

def convert_to_metric(imperial_weight, imperial_height):
    metric_weight = imperial_weight * 0.453592
    metric_height = imperial_height * 2.54
    return metric_weight, metric_height

def convert_to_imperial(metric_weight, metric_height):
    imperial_weight = metric_weight / 0.453592
    imperial_height = metric_height / 2.54
    return imperial_weight, imperial_height
