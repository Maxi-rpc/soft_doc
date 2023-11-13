# imports
import tkinter as tk

class login_view:
    def __init__(self, window):
        # initializations 
        self.wind = window
        self.wind.title('Login')

        # creating a Frame Container 
        frame = tk.LabelFrame(self.wind, text = 'Iniciar Sesion')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        # input name
        tk.Label(frame, text = 'Nombre: ').grid(row = 1, column = 0)
        self.name = tk.Entry(frame)
        self.name.focus()
        self.name.grid(row = 1, column = 1)

        # input pass
        tk.Label(frame, text = 'Contraseña: ').grid(row = 2, column = 0)
        self.password = tk.Entry(frame)
        self.password.grid(row = 2, column = 1)

        # Button Add Product 
        tk.Button(frame, text = 'Iniciar', command = self.login).grid(row = 3, columnspan = 2, sticky = tk.W + tk.E)

        # Output Message
        self.message = tk.Label(text = '', fg = 'red')
        self.message.grid(row = 3, column = 0, columnspan = 2, sticky = tk.W + tk.E)

    # User Input Validation
    def validation(self):
        return len(self.name.get()) != 0 and len(self.password.get()) != 0
    
    def login(self):
        if self.validation():
            print(self.name.get(), self.password.get())
        else:
            self.message['text'] = 'Completar campos'
