import tkinter as tk

from Base import BaseRole


#интерфейс админа
class AdminInterface(BaseRole):


    def __init__(self,root):
        self.root = root
        tk.Label(self.root,text="Интерфейс админа",font=("Arial",16)).pack(pady=20)

    def create_interface(self):
        self.clear_window()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()