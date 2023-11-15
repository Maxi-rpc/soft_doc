# imports
import tkinter as tk
from db_utils import db_config
import mysql.connector

userProfile = {
    'User': 'maxirpc',
    'Nombre': 'Maximiliano',
    'Edad': 31
}

userProgress = {
    'User': userProfile['User'],
    'Problema': 'Ansiedad',
    'Objetivo': 'controlar la ansiedad generada'
}

userConsejo = {
    'Problema': userProgress['Problema'],
    'Consejo': 'cambiar dieta',
    'Actividad': 'hacer futbol pa'
}

class data_view:
    def __init__(self, user):
        # initializations
        self.username = user
        self.datos = self.get_user_persona()

        self.wind = tk.Tk()
        self.wind.title('Data')
        self.wind.geometry('600x500')

        ### Persona
        # Frame Container 
        frame = tk.LabelFrame(self.wind, text = 'Datos del usuario')
        frame.grid(row = 0, column = 0, pady = 10)

        # text name
        tk.Label(frame, text = 'User: ').grid(row = 1, column = 0)
        self.user = tk.Entry(frame)
        self.user.insert(0, self.datos['User'])
        self.user.grid(row = 1, column = 1)
        self.user.config(state='readonly')

        # text edad
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
        self.progreso = self.get_user_progreso()
        # Frame Container 
        frame_prog = tk.LabelFrame(self.wind, text = 'Progreso')
        frame_prog.grid(row = 4, column = 0, columnspan = 3, pady = 10)

        # text problema
        tk.Label(frame_prog, text = 'Problema: ').grid(row = 1, column = 0)
        self.prob = tk.Text(frame_prog, height=1, width=40)
        self.prob.insert(tk.END, self.progreso['Problema'])
        self.prob.grid(row = 1, column = 1)
        self.prob.config(state='disabled')

        # text objetivo
        tk.Label(frame_prog, text = 'Objetivo: ').grid(row = 2, column = 0)
        self.objet = tk.Text(frame_prog, height=2, width=40)
        self.objet.insert(tk.END, self.progreso['Objetivo'])
        self.objet.grid(row = 2, column = 1)
        self.objet.config(state='disabled')


        ### Consejo
        self.consejos = self.get_user_consejos()
        # Frame Container 
        frame_prog = tk.LabelFrame(self.wind, text = 'Recomendaciones')
        frame_prog.grid(row = 7, column = 0, columnspan = 10, pady = 10)

        # text consejo
        tk.Label(frame_prog, text = 'Consejo: ').grid(row = 1, column = 0)
        self.consej = tk.Text(frame_prog, height=3, width=50)
        self.consej.insert(tk.END, self.consejos['Consejo'])
        self.consej.grid(row = 1, column = 1)
        self.consej.config(state='disabled')

        # text actividad
        tk.Label(frame_prog, text = 'Actividad: ').grid(row = 2, column = 0)
        self.activ = tk.Text(frame_prog, height=3, width=50)
        self.activ.insert(tk.END, self.consejos['Actividad'])
        self.activ.grid(row = 2, column = 1)
        self.activ.config(state='disabled')

        # text libro
        tk.Label(frame_prog, text = 'Libro: ').grid(row = 3, column = 0)
        self.libr = tk.Text(frame_prog, height=1, width=50)
        self.libr.insert(tk.END, self.consejos['Libro'])
        self.libr.grid(row = 3, column = 1)
        self.libr.config(state='disabled')

        ### Editar
        # Frame Container 
        frame_btn = tk.Frame(self.wind)
        frame_btn.grid(row = 8, column = 0, columnspan = 2)
        # Button Add Product 
        btnConsejo = tk.Button(frame_btn, text = 'Consejo', command = self.edit_user)
        btnConsejo.grid(row = 0, column=0, columnspan = 2, sticky = tk.W + tk.E)


        self.wind.mainloop()

    def get_user_persona(self):
        usr = self.username

        cnx = mysql.connector.connect(
                host = db_config['host'],
                user = db_config['user'], 
                database = db_config['database']
            )
        cursor = cnx.cursor()
        query = f"SELECT * FROM persona WHERE User = '{usr}'"
        cursor.execute(query)
        data = {}
        for (User, Nombre, Edad) in cursor:
            data['User'] = User
            data['Nombre'] = Nombre
            data['Edad'] = Edad

        cursor.close()    
        cnx.close()
        return data
    
    def get_user_progreso(self):
        usr = self.username

        cnx = mysql.connector.connect(
                host = db_config['host'],
                user = db_config['user'], 
                database = db_config['database']
            )
        cursor = cnx.cursor()
        query = f"SELECT * FROM progreso WHERE User = '{usr}'"
        cursor.execute(query)
        data = {}
        for (User, Problema, Objetivo) in cursor:
            data['Problema'] = Problema
            data['Objetivo'] = Objetivo

        cursor.close()    
        cnx.close()
        return data
    
    def get_user_consejos(self):
        prob = self.progreso['Problema']

        cnx = mysql.connector.connect(
                host = db_config['host'],
                user = db_config['user'], 
                database = db_config['database']
            )
        cursor = cnx.cursor()
        query = f"SELECT * FROM consejos WHERE Problema = '{prob}'"
        cursor.execute(query)
        data = {}
        for (Problema, Consejo, Actividad, Libro) in cursor:
            data['Consejo'] = Consejo
            data['Actividad'] = Actividad
            data['Libro'] = Libro

        cursor.close()    
        cnx.close()
        return data
    
    def edit_user(self):
        print('a editar user')

