# imports
import tkinter as tk
from db_utils import db_config, run_query
import mysql.connector

class data_view:
    def __init__(self, user):
        # initializations
        self.username = user
        self.datos = self.get_user_persona()
        self.progreso = self.get_user_progreso()
        self.consejos = self.get_user_consejos()

        self.wind = tk.Tk()
        self.wind.title('Data')
        self.wind.geometry('600x500')

        ### Persona
        # Frame Container 
        frame = tk.LabelFrame(self.wind, text = 'Datos del usuario')
        frame.grid(row = 0, column = 0)

        # text User
        tk.Label(frame, text = 'User: ').grid(row = 1, column = 0)
        self.user = tk.Entry(frame)
        self.user.insert(0, self.datos['User'])
        self.user.grid(row = 1, column = 1)
        self.user.config(state='readonly')

        # text nombre
        tk.Label(frame, text = 'Nombre: ').grid(row = 2, column = 0)
        self.name = tk.Entry(frame)
        self.name.insert(0, self.datos['Nombre'])
        self.name.grid(row = 2, column = 1)
        self.name.config(state='readonly')

        # text edad
        tk.Label(frame, text = 'Edad: ').grid(row = 3, column = 0)
        self.age = tk.Entry(frame)
        self.age.insert(0, self.datos['Edad'])
        self.age.grid(row = 3, column = 1)
        self.age.config(state='readonly')

        ### Progreso
        
        # Frame Container 
        frame_prog = tk.LabelFrame(self.wind, text = 'Progreso')
        frame_prog.grid(row = 4, column = 0, columnspan = 3, pady = 10)

        # text problema
        tk.Label(frame_prog, text = 'Problema: ').grid(row = 1, column = 0)
        self.prob = tk.Text(frame_prog, height=1, width=50)
        self.prob.insert(tk.END, self.progreso['Problema'])
        self.prob.grid(row = 1, column = 1)
        self.prob.config(state='disabled')

        # text descripcion
        tk.Label(frame_prog, text = 'Descripcion: ').grid(row = 2, column = 0)
        self.descrip = tk.Text(frame_prog, height=5, width=50)
        self.descrip.insert(tk.END, self.consejos['Descripcion'])
        self.descrip.grid(row = 2, column = 1)
        self.descrip.config(state='disabled')

        # text objetivo
        tk.Label(frame_prog, text = 'Objetivo: ').grid(row = 3, column = 0)
        self.objet = tk.Text(frame_prog, height=2, width=50)
        self.objet.insert(tk.END, self.progreso['Objetivo'])
        self.objet.grid(row = 3, column = 1)
        self.objet.config(state='disabled')


        ### Consejo
        
        # Frame Container 
        frame_prog = tk.LabelFrame(self.wind, text = 'Recomendaciones')
        frame_prog.grid(row = 7, column = 0, columnspan = 10, pady = 10)

        # text consejo
        tk.Label(frame_prog, text = 'Consejo: ').grid(row = 1, column = 0)
        self.consej = tk.Text(frame_prog, height=4, width=50)
        self.consej.insert(tk.END, self.consejos['Consejo'])
        self.consej.grid(row = 1, column = 1)
        self.consej.config(state='disabled')

        # text libro
        tk.Label(frame_prog, text = 'Libro: ').grid(row = 2, column = 0)
        self.libr = tk.Text(frame_prog, height=1, width=50)
        self.libr.insert(tk.END, self.consejos['Libro'])
        self.libr.grid(row = 2, column = 1)
        self.libr.config(state='disabled')

        ### Buttons
        # Frame Container 
        frame_btn = tk.Frame(self.wind)
        frame_btn.grid(row = 12, column = 0, columnspan = 4)

        # Button
        btnCerrar = tk.Button(frame_btn, text = 'Cerrar Sesion', command = self.exit_session)
        btnCerrar.grid(row = 0, column=3, columnspan = 2, padx = 10)


        self.wind.mainloop()

    def get_user_persona(self):
        usr = self.username
        
        query = f"SELECT * FROM persona WHERE User = '{usr}'"
        dataDB = run_query(query)
        data = {}
        for (User, Nombre, Edad) in dataDB:
            data['User'] = User
            data['Nombre'] = Nombre
            data['Edad'] = Edad
        return data
    
    def get_user_progreso(self):
        usr = self.username

        query = f"SELECT * FROM progreso WHERE User = '{usr}'"
        dataDB = run_query(query)
        data = {}
        for (User, Problema, Objetivo) in dataDB:
            data['Problema'] = Problema
            data['Objetivo'] = Objetivo

        return data
    
    def get_user_consejos(self):
        prob = self.progreso['Problema']

        query = f"SELECT * FROM consejos WHERE Problema = '{prob}'"
        dataDB = run_query(query)
        data = {}
        for (Problema, Descripcion, Consejo, Libro) in dataDB:
            data['Descripcion'] = Descripcion
            data['Consejo'] = Consejo
            data['Libro'] = Libro

        return data
    
    def exit_session(self):
        self.wind.destroy()