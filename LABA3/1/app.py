import tkinter as tk
from tkinter import messagebox
import json
from user import User
from adapter import Adapter, convert_to_metric, convert_to_imperial



# Class representing the main application.
class App:
    def __init__(self, root):
   
        self.root = root

        self.root.title("Non-Mobile App")

        self.users = {}

        self.load_data()

        self.create_widgets()

    # Method to create GUI widgets.
    def create_widgets(self):
    
        self.label = tk.Label(self.root, text="Welcome to the Non-Mobile App!")
        self.label.pack()

        self.name_label = tk.Label(self.root, text="Enter your name:")
        self.name_label.pack()

        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()

        self.choice_var = tk.StringVar()

        self.metric_button = tk.Radiobutton(self.root, text="Use Metric System",  value="metric")
        self.metric_button.pack()

        self.imperial_button = tk.Radiobutton(self.root, text="Use Imperial System", value="imperial")
        self.imperial_button.pack()

        self.weight_label = tk.Label(self.root, text="Enter weight:")
        self.weight_label.pack()

        self.weight_entry = tk.Entry(self.root)
        self.weight_entry.pack()

        self.height_label = tk.Label(self.root, text="Enter height:")
        self.height_label.pack()

        self.height_entry = tk.Entry(self.root)
        self.height_entry.pack()

        self.register_button = tk.Button(self.root, text="Register", command=self.register)
        self.register_button.pack()

        self.show_all_button = tk.Button(self.root, text="Show All Users", command=self.show_all_users)
        self.show_all_button.pack()

        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.destroy)
        self.exit_button.pack()

    # Method to register a new user.
    def register(self):
        name = self.name_entry.get()
        choice = self.choice_var.get()
        weight_entry_value = self.weight_entry.get()
        height_entry_value = self.height_entry.get()

        if not name or not weight_entry_value or not height_entry_value:
            messagebox.showerror("Error", "Please enter name, weight, and height.")
            return

        try:
            weight = float(weight_entry_value)
            height = float(height_entry_value)
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter numeric values.")
            return

        # Creating a new User instance and adapting it with an Adapter.
        user = User(name, 0, 0)
        self.users[name] = Adapter(user)

        # Saving user data to a file.
        self.save_data()

        # Registering the user with the chosen measurement system.
        self.users[name].register(weight, height, choice)

        # Displaying registration information.
        if choice == "metric" or choice == "imperial":
            messagebox.showinfo("Registration", user.display() + "\n" + self.users[name].exchange_data())
        else:
            messagebox.showerror("Error", "Please select a valid system.")

    # Method to convert units and display the result.
    def convert_units(self):
        name = self.name_entry.get()

        if name not in self.users:
            messagebox.showerror("Error", "User not found. Please register first.")
            return

        user_adapter = self.users[name]

        # Converting and displaying the units.
        if self.choice_var.get() == "metric":
            metric_weight, metric_height = convert_to_metric(user_adapter.user.weight, user_adapter.user.height)
            messagebox.showinfo("Unit Conversion", f"{user_adapter.user.name}'s weight: {metric_weight:.2f} kg, height: {metric_height:.2f} cm")
        elif self.choice_var.get() == "imperial":
            imperial_weight, imperial_height = convert_to_imperial(user_adapter.user.weight, user_adapter.user.height)
            messagebox.showinfo("Unit Conversion", f"{user_adapter.user.name}'s weight: {imperial_weight:.2f} lbs, height: {imperial_height:.2f} inches")
        else:
            messagebox.showerror("Error", "Please select a system before converting units.")

    # Method to display information about all registered users.
    def show_all_users(self):
        user_info = "\n".join([user.display() for user in self.users.values()])
        messagebox.showinfo("All Users", user_info)

    # Method to save user data to a file.
    def save_data(self):
        with open("user_data.json", "w") as file:
            data = [{"name": user.user.name, "weight": user.user.weight, "height": user.user.height} for user in self.users.values()]
            json.dump(data, file)

    # Method to load existing user data from a file.
    def load_data(self):
        try:
            with open("user_data.json", "r") as file:
                data = json.load(file)
                for user_data in data:
                    name = user_data["name"]
                    weight = user_data["weight"]
                    height = user_data["height"]
                    user = User(name, 0, 0)
                    self.users[name] = Adapter(user)
                    self.users[name].register(weight, height, "imperial")  
        except FileNotFoundError:
            pass
