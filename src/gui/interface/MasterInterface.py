import tkinter as tk
from tkinter import messagebox
from tkinter import Tk
from pydantic import BaseModel, validator, ValidationError
from Base.BaseRole import BaseRole

class MasterInterface(BaseRole):
    def __init__(self,root:Tk):
        self.root = root

    def create_interface(self):
        self.clear_window()
        tk.Label(self.root,text="Интерфейс мастера",font=("Arial",16).pack(pady=20))

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
