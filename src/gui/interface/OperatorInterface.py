from tkinter import Tk
import tkinter as tk
from Base.BaseRole import BaseRole

class OperatorInterface(BaseRole):
    def __init__(self, root):
        self.root = root

    def create_interface(self):
        self.clear_window()
        tk.Label(self.root, text="Интерфейс Оператора", font=("Arial", 16)).pack(pady=20)
        # Add further operator-specific UI elements here

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()