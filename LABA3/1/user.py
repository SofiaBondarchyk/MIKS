class User:
    def __init__(self, name="", weight=0, height=0):
        self.name = name
        self.weight = weight
        self.height = height

    def display(self):
        return f"Name: {self.name}, Weight: {self.weight} kg, Height: {self.height} cm"
