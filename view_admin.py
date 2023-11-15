# imports
import tkinter as tk
from db_utils import db_config
import mysql.connector

class admin_view:
    def __init__(self):
        # initializations
        self.wind = tk.Tk()
        self.wind.title('Admin')
        self.wind.geometry('600x500')


        self.wind.mainloop()