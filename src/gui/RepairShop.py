import tkinter as tk
from tkinter import messagebox
from tkinter import Tk
from pydantic import BaseModel,  ValidationError, field_validator


from interface.OperatorInterface import OperatorInterface
from interface.MasterInterface import MasterInterface
from interface.CustomerInterface import CustomerInterface
from interface.ManagerInterface import ManagerInterface

class RepairShop:
    def __init__(self,root:Tk):
        self.password_entry = None
        self.login_entry = None
        self.root = root
        self.root.title("Ремонтная Мастерская")
        self.interface = None

        self.users = {
            "login1": "pass1",
            "login2": "pass2",
            "login3":"pass3",
        }

        self.roles = {
            "login1":"Менеджер",
            "login2":"Мастер",
            "login3":"Оператор",
            "login4":"Заказчик",
        }

        self.create_login_page()


    class UserLogin(BaseModel):
        login:str
        password:str

        @field_validator("login")
        def validate_login(cls,value):
            if len(value) < 3:
                raise ValueError("Логин должен содержать хотя бы 3 символа")
            return value

        @field_validator("password")
        def validate_password(cls,value):
            if len(value) < 3:
                raise ValueError("Пароль должен содержать хотя бы 3 символа")


    def create_login_page(self):
        self.clear_window()

        tk.Label(self.root,  text="Логин:").grid(row=0,column=0,padx=10,pady=5,sticky="w")
        self.login_entry = tk.Entry(self.root)
        self.login_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Пароль:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Button(self.root, text="Войти", command=self.handle_login).grid(pady=10)

    def handle_login(self):
        login = self.login_entry.get()
        password = self.password_entry.get()

        # Validate login and password using Pydantic
        try:
            user_data = self.UserLogin(login=login, password=password)

            # Check if the login and password match
            if login in self.users and self.users[login] == password:
                role = self.roles.get(login)
                if role:
                    self.switch_to_role_interface(role)
                else:
                    messagebox.showerror("Ошибка", "Неизвестная роль!")
            else:
                messagebox.showerror("Ошибка", "Неверные данные для входа!")
        except ValidationError as e:
            messagebox.showerror("Ошибка", f"Ошибка валидации: {e}")


    def switch_to_role_interface(self, role):
        if role == "Менеджер":
            self.interface = ManagerInterface(self.root)
        elif role == "Мастер":
            self.interface = MasterInterface(self.root)
        elif role == "Оператор":
            self.interface = OperatorInterface(self.root)
        elif role == "Заказчик":
            self.interface = CustomerInterface(self.root)
        else:
            messagebox.showerror("Ошибка", f"Неизвестная роль: {role}")
            return
        self.interface.create_interface()


    def clear_window(self):
      for widget in self.root.winfo_children():
           widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = RepairShop(root)
    root.geometry("300x200")
    root.mainloop()
