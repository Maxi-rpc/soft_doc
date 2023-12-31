# imports
import tkinter as tk
from view_data import data_view
from view_admin import admin_view
from db_utils import db_config, run_query
import mysql.connector

class login_view:
    def __init__(self, window):
        # initializations 
        self.wind = window
        self.wind.title('Login')

        # Frame Container 
        frame = tk.LabelFrame(self.wind, text = 'Iniciar Sesion')
        frame.grid(row = 0, column = 0, columnspan = 6, pady = 50, padx= 50)

        # input name
        tk.Label(frame, text = 'User: ').grid(row = 1, column = 0)
        self.name = tk.Entry(frame)
        self.name.focus()
        self.name.grid(row = 1, column = 1)

        # input pass
        tk.Label(frame, text = 'Contraseña: ').grid(row = 2, column = 0)
        self.password = tk.Entry(frame)
        self.password.grid(row = 2, column = 1)
        self.password.config(show='*')

        # Button
        tk.Button(frame, text = 'Iniciar', command = self.login).grid(row = 3, columnspan = 2, sticky = tk.W + tk.E)

        # Output Message
        self.message = tk.Label(text = '', fg = 'red')
        self.message.grid(row = 3, column = 0, columnspan = 6, sticky = tk.W + tk.E)

    # get user
    def search_user(self):
        usr = self.name.get()
        psw = self.password.get()
        query = f"SELECT * FROM users WHERE User = '{usr}' AND Pass = '{psw}'"
        data = run_query(query)
        return data

    # User Input Validation
    def validation(self):
        return len(self.name.get()) != 0 and len(self.password.get()) != 0
    
    def login(self):
        if self.validation():
            res = self.search_user()
            if len(res) > 0:
                user=self.name.get()
                if user == 'admin':
                    self.wind.destroy()
                    admin_view()
                self.wind.destroy()
                data_view(user=user)
            else:
                self.message['text'] = 'Nombre o Contraseña incorrectos'
        else:
            self.message['text'] = 'Completar campos'
