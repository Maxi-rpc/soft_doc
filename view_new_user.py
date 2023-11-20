# imports
import tkinter as tk
from tkinter import ttk
from db_utils import db_config, run_query
import mysql.connector

class new_user_view:
    def __init__(self):
        # initializations
        self.wind = tk.Toplevel()
        #self.wind = tk.Tk()
        self.wind.title('Nuevo User')
        self.wind.geometry('600x500')

        ### Persona
        # Frame Container 
        frame = tk.LabelFrame(self.wind, text = 'Datos del usuario')
        frame.grid(row = 0, column = 0, pady = 10)

        # text nombre
        tk.Label(frame, text = 'Nombre: ').grid(row = 1, column = 0)
        self.name = tk.Entry(frame)
        self.name.grid(row = 1, column = 1)

        # text edad
        tk.Label(frame, text = 'Edad: ').grid(row = 2, column = 0)
        self.age = tk.Entry(frame)
        self.age.grid(row = 2, column = 1)

        ### Progreso
        # Frame Container 
        frame_prog = tk.LabelFrame(self.wind, text = 'Progreso')
        frame_prog.grid(row = 3, column = 0, columnspan = 3, pady = 10)

        # lista problema
        self.listProblemas = self.list_problemas()
        tk.Label(frame_prog, text = 'Problema: ').grid(row = 1, column = 0)

        self.prob = ttk.Combobox(frame_prog, height= 1, width = 27, textvariable = tk.StringVar())
        self.prob['values'] = self.listProblemas
        self.prob.current()
        self.prob.grid(row = 1, column = 1)
        self.prob.bind("<<ComboboxSelected>>", func=self.complete_data)

        # text descripcion
        tk.Label(frame_prog, text = 'Descripcion: ').grid(row = 2, column = 0)
        self.descrip = tk.Text(frame_prog, height=4, width=50)
        self.descrip.grid(row = 2, column = 1)

        # text objetivo
        tk.Label(frame_prog, text = 'Objetivo: ').grid(row = 3, column = 0)
        self.objet = tk.Text(frame_prog, height=2, width=50)
        self.objet.grid(row = 3, column = 1)


        ### Consejo
        # Frame Container 
        frame_prog = tk.LabelFrame(self.wind, text = 'Recomendaciones')
        frame_prog.grid(row = 6, column = 0, columnspan = 10, pady = 10)

        # text consejo
        tk.Label(frame_prog, text = 'Consejo: ').grid(row = 1, column = 0)
        self.consej = tk.Text(frame_prog, height=4, width=50)
        self.consej.grid(row = 1, column = 1)

        # text libro
        tk.Label(frame_prog, text = 'Libro: ').grid(row = 2, column = 0)
        self.libr = tk.Text(frame_prog, height=1, width=50)
        self.libr.grid(row = 2, column = 1)

        # user login
        # Frame Container 
        frame = tk.LabelFrame(self.wind, text = 'Datos de login')
        frame.grid(row = 10, column = 0, columnspan = 6)

        # input user
        tk.Label(frame, text = 'User: ').grid(row = 1, column = 0)
        self.user = tk.Entry(frame)
        self.user.grid(row = 1, column = 1)

        # input pass
        tk.Label(frame, text = 'Contraseña: ').grid(row = 2, column = 0)
        self.password = tk.Entry(frame)
        self.password.grid(row = 2, column = 1)

        ### agregar
        # Frame Container 
        frame_btn = tk.Frame(self.wind)
        frame_btn.grid(row = 13, column = 0, columnspan = 4)
        # Button
        btnEditar = tk.Button(frame_btn, text = 'Guardar registro', command = self.add_data)
        btnEditar.grid(row = 0, column=0, columnspan = 2, padx = 10)

        # Button
        btnCerrar = tk.Button(frame_btn, text = 'Volver', command = self.wind.destroy)
        btnCerrar.grid(row = 0, column=3, columnspan = 2, padx = 10)

        # Output Message
        frame_msg = tk.Frame(self.wind)
        frame_msg.grid(row = 15, column = 0, columnspan = 2)
        self.message = tk.Label(frame_msg, text = '', fg = 'red')
        self.message.grid(row = 3, column = 0, columnspan = 6, sticky = tk.W + tk.E)

    def list_problemas(self):
        query = f"SELECT Problema FROM consejos"
        dataDB = run_query(query)
        data = []
        for (Problema) in dataDB:
            data.append(Problema[0])
        return data
    
    def complete_data(self, event):
        probl = event.widget.get()
        data = self.get_user_consejos(probl)
        self.descrip.insert(tk.END, data['Descripcion'])
        self.consej.insert(tk.END, data['Consejo'])
        self.libr.insert(tk.END, data['Libro'])
    
    def get_user_consejos(self, probl):
        query = f"SELECT * FROM consejos WHERE Problema = '{probl}'"
        dataDB = run_query(query)
        data = {}
        for (Problema, Descripcion, Consejo, Libro) in dataDB:
            data['Descripcion'] = Descripcion
            data['Consejo'] = Consejo
            data['Libro'] = Libro
        return data
    
    def add_data(self):
        # users
        usr = self.user.get()
        pas = self.password.get()

        query = f"INSERT INTO users (`Id`, `User`, `Pass`) VALUES (NULL, '{usr}', '{pas}')"
        self.add_sql(query=query)

        # persona
        name = self.name.get()
        age = self.age.get()
        query2 = f"INSERT INTO persona (`User`, `Nombre`, `Edad`) VALUES ('{usr}', '{name}', '{age}')"
        self.add_sql(query=query2)


        # progreso
        prob = self.prob.get()
        obje = self.objet.get('1.0', tk.END)
        obje = obje.rstrip()
        query3 = f"INSERT INTO progreso (`User`, `Problema`, `Objetivo`) VALUES ('{usr}', '{prob}', '{obje}')"
        save = self.add_sql(query=query3)

        if save:
            self.message['text'] = f'Se agregan datos'
            self.message.config(fg = 'green')

    def add_sql(self, query):
        isSave = False
        try:
            run_query(query)
            isSave = True
        except Exception as e:
            self.message['text'] = f'Error al guardar datos {e}'
        return isSave