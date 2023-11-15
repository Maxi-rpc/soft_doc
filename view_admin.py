# imports
import tkinter as tk
from tkinter import ttk
from db_utils import db_config
import mysql.connector

class admin_view:
    def __init__(self):
        # initializations
        self.wind = tk.Tk()
        self.wind.title('Admin')
        self.wind.geometry('600x500')

        ### buscar user
        self.listUsers = self.list_users()

        # Frame Container 
        frame = tk.LabelFrame(self.wind, text = 'Buscar usuario')
        frame.grid(row = 0, column = 0, pady = 10)

        # text buscar
        tk.Label(frame, text = 'Buscar: ').grid(row = 1, column = 0)
        self.userList = ttk.Combobox(frame, width = 27, textvariable = tk.StringVar())
        self.userList['values'] = self.listUsers
        self.userList.current()
        self.userList.grid(row = 1, column = 1)

        # Button
        tk.Button(frame, text = 'Buscar', command = self.get_data).grid(row = 3, columnspan = 2, sticky = tk.W + tk.E)

        ### Persona
        self.datos = {}
        # Frame Container 
        frame = tk.LabelFrame(self.wind, text = 'Datos del usuario')
        frame.grid(row = 3, column = 0, pady = 10)

        # text nombre
        tk.Label(frame, text = 'Nombre: ').grid(row = 1, column = 0)
        self.name = tk.Entry(frame)
        self.name.grid(row = 1, column = 1)

        # text edad
        tk.Label(frame, text = 'Edad: ').grid(row = 2, column = 0)
        self.age = tk.Entry(frame)
        self.age.grid(row = 2, column = 1)

        ### Progreso
        self.progreso = {}
        # Frame Container 
        frame_prog = tk.LabelFrame(self.wind, text = 'Progreso')
        frame_prog.grid(row = 6, column = 0, columnspan = 3, pady = 10)

        # text problema
        tk.Label(frame_prog, text = 'Problema: ').grid(row = 1, column = 0)
        self.prob = tk.Text(frame_prog, height=1, width=40)
        self.prob.grid(row = 1, column = 1)

        # text objetivo
        tk.Label(frame_prog, text = 'Objetivo: ').grid(row = 2, column = 0)
        self.objet = tk.Text(frame_prog, height=2, width=40)
        self.objet.grid(row = 2, column = 1)

        ### Consejo
        self.consejos = {}
        # Frame Container 
        frame_prog = tk.LabelFrame(self.wind, text = 'Recomendaciones')
        frame_prog.grid(row = 9, column = 0, columnspan = 10, pady = 10)

        # text consejo
        tk.Label(frame_prog, text = 'Consejo: ').grid(row = 1, column = 0)
        self.consej = tk.Text(frame_prog, height=3, width=50)
        self.consej.grid(row = 1, column = 1)

        # text actividad
        tk.Label(frame_prog, text = 'Actividad: ').grid(row = 2, column = 0)
        self.activ = tk.Text(frame_prog, height=3, width=50)
        self.activ.grid(row = 2, column = 1)

        # text libro
        tk.Label(frame_prog, text = 'Libro: ').grid(row = 3, column = 0)
        self.libr = tk.Text(frame_prog, height=1, width=50)
        self.libr.grid(row = 3, column = 1)

        ### Editar
        # Frame Container 
        frame_btn = tk.Frame(self.wind)
        frame_btn.grid(row = 13, column = 0, columnspan = 2)
        # Button
        btnConsejo = tk.Button(frame_btn, text = 'Editar', command = self.update_data)
        btnConsejo.grid(row = 0, column=0, columnspan = 2, sticky = tk.W + tk.E)

        # Output Message
        frame_msg = tk.Frame(self.wind)
        frame_msg.grid(row = 15, column = 0, columnspan = 2)
        self.message = tk.Label(frame_msg, text = '', fg = 'red')
        self.message.grid(row = 3, column = 0, columnspan = 6, sticky = tk.W + tk.E)

        self.wind.mainloop()

    # functions
    def list_users(self):
        cnx = mysql.connector.connect(
                host = db_config['host'],
                user = db_config['user'], 
                database = db_config['database']
            )
        cursor = cnx.cursor()
        query = f"SELECT User FROM users"
        cursor.execute(query)
        data = []
        for (User) in cursor:
            data.append(User[0])
        cursor.close()    
        cnx.close()
        return data
    
    def get_data(self):
        usr = self.userList.get()
        data = self.get_user_persona(username=usr)
        self.datos['Nombre'] = data['Nombre']
        self.name.insert(0, self.datos['Nombre'])
        
        self.datos['Edad'] = data['Edad']
        self.age.insert(0, self.datos['Edad'])

        progres = self.get_user_progreso(username=usr)
        self.progreso['Problema'] = progres['Problema']
        self.prob.insert(tk.END, self.progreso['Problema'])

        self.progreso['Objetivo'] = progres['Objetivo']
        self.objet.insert(tk.END, self.progreso['Objetivo'])
        
        consej = self.get_user_consejos(probl=self.progreso['Problema'])
        self.consejos['Consejo'] = consej['Consejo']
        self.consej.insert(tk.END, self.consejos['Consejo'])

        self.consejos['Actividad'] = consej['Actividad']
        self.activ.insert(tk.END, self.consejos['Actividad'])

        self.consejos['Libro'] = consej['Libro']
        self.libr.insert(tk.END, self.consejos['Libro'])       

    def get_user_persona(self, username):
        usr = username
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
    
    def get_user_progreso(self, username):
        usr = username
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
    
    def get_user_consejos(self, probl):
        prob = probl
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
    
    def update_data(self):
        usr = self.userList.get()
        nombre = self.name.get()
        edad = self.age.get()
        query = f"UPDATE persona SET Nombre = '{nombre}', Edad = '{edad}' WHERE User = '{usr}'"
        isSave = self.update_sql(query=query)

        if isSave:
            self.message['text'] = f'Se actualizaron datos'
            self.message.config(fg = 'green')

    def update_sql(self, query):
        cnx = mysql.connector.connect(
            host = db_config['host'],
            user = db_config['user'], 
            database = db_config['database']
        )
        cursor = cnx.cursor()
        isSave = False
        try:
            cursor.execute(query)
            isSave = True
        except Exception as e:
            self.message['text'] = f'Error al guardar datos {e}'
        cursor.close()    
        cnx.close()
        return isSave