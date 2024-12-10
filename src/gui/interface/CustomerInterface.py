import tkinter as tk
from Base.BaseRole import BaseRole
# Интерфейс заказчика
class CustomerInterface(BaseRole):
    def __init__(self, root):
        self.root = root

    def create_interface(self):
        self.clear_window()
        tk.Label(self.root, text="Интерфейс Заказчика", font=("Arial", 16)).pack(pady=20)
        # Add further customer-specific UI elements here

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
