from tkinter import Tk
import tkinter as tk
from Base.BaseRole import BaseRole

#интерфейс менеджера
class ManagerInterface(BaseRole):

    def __init__(self, root: Tk):
        self.root = root

    def create_interface(self):
        self.clear_window()
        tk.Label(self.root, text="Интерфейс Менеджера", font=("Arial", 16)).pack(pady=20)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
