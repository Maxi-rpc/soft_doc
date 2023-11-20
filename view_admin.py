# imports
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from db_utils import db_config, run_query
import mysql.connector
from view_new_user import new_user_view

class admin_view:
    def __init__(self):
        # initializations
        self.wind = tk.Tk()
        self.wind.title('Admin')
        self.wind.geometry('600x600')

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
        frame.grid(row = 3, column = 0)

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

        # text problema
        tk.Label(frame_prog, text = 'Descripcion: ').grid(row = 2, column = 0)
        self.descrip = tk.Text(frame_prog, height=5, width=40)
        self.descrip.grid(row = 2, column = 1)

        # text objetivo
        tk.Label(frame_prog, text = 'Objetivo: ').grid(row = 3, column = 0)
        self.objet = tk.Text(frame_prog, height=2, width=40)
        self.objet.grid(row = 3, column = 1)

        ### Consejo
        self.consejos = {}
        # Frame Container 
        frame_prog = tk.LabelFrame(self.wind, text = 'Recomendaciones')
        frame_prog.grid(row = 9, column = 0, columnspan = 10, pady = 10)

        # text consejo
        tk.Label(frame_prog, text = 'Consejo: ').grid(row = 1, column = 0)
        self.consej = tk.Text(frame_prog, height=3, width=50)
        self.consej.grid(row = 1, column = 1)

        # text libro
        tk.Label(frame_prog, text = 'Libro: ').grid(row = 2, column = 0)
        self.libr = tk.Text(frame_prog, height=1, width=50)
        self.libr.grid(row = 2, column = 1)

        ### Editar
        # Frame Container 
        frame_btn = tk.Frame(self.wind)
        frame_btn.grid(row = 13, column = 0, columnspan = 4)
        # Button
        btnEditar = tk.Button(frame_btn, text = 'Editar registro', command = self.update_data)
        btnEditar.grid(row = 0, column=0, columnspan = 2, padx = 10)
        # Button
        btnAgregar = tk.Button(frame_btn, text = 'Nuevo registro', command = self.new_user)
        btnAgregar.grid(row = 0, column=3, columnspan = 2)

        # Button
        btnEliminar = tk.Button(frame_btn, text = 'Eliminar registro', command = self.delete_user)
        btnEliminar.grid(row = 0, column=5, columnspan = 2, padx = 10)

        # Button
        btnCerrar = tk.Button(frame_btn, text = 'Cerrar sesion', command = self.exit_session)
        btnCerrar.grid(row = 0, column=7, columnspan = 2, padx = 10)

        # Output Message
        frame_msg = tk.Frame(self.wind)
        frame_msg.grid(row = 15, column = 0, columnspan = 2)
        self.message = tk.Label(frame_msg, text = '', fg = 'red')
        self.message.grid(row = 3, column = 0, columnspan = 6, sticky = tk.W + tk.E)

        self.wind.mainloop()

    # functions
    def list_users(self):
        query = f"SELECT User FROM users"
        dataDB = run_query(query)
        data = []
        for (User) in dataDB:
            data.append(User[0])
        return data
    
    def clean_inputs(self):
        self.name.delete(0, tk.END)
        self.age.delete(0, tk.END)
        self.prob.delete('1.0', tk.END)
        self.descrip.delete('1.0', tk.END)
        self.objet.delete('1.0', tk.END)
        self.consej.delete('1.0', tk.END)
        self.libr.delete('1.0', tk.END) 

    def get_data(self):
        self.clean_inputs()

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
        self.consejos['Descripcion'] = consej['Descripcion']
        self.descrip.insert(tk.END, self.consejos['Descripcion'])

        self.consejos['Consejo'] = consej['Consejo']
        self.consej.insert(tk.END, self.consejos['Consejo'])

        self.consejos['Libro'] = consej['Libro']
        self.libr.insert(tk.END, self.consejos['Libro'])    

    def get_user_persona(self, username):
        usr = username
        query = f"SELECT * FROM persona WHERE User = '{usr}'"
        dataDB = run_query(query)
        data = {}
        for (User, Nombre, Edad) in dataDB:
            data['User'] = User
            data['Nombre'] = Nombre
            data['Edad'] = Edad
        return data
    
    def get_user_progreso(self, username):
        usr = username

        query = f"SELECT * FROM progreso WHERE User = '{usr}'"
        dataDB = run_query(query)
        data = {}
        for (User, Problema, Objetivo) in dataDB:
            data['Problema'] = Problema
            data['Objetivo'] = Objetivo
        return data
    
    def get_user_consejos(self, probl):
        prob = probl

        query = f"SELECT * FROM consejos WHERE Problema = '{prob}'"
        dataDB = run_query(query)
        data = {}
        for (Problema, Descripcion, Consejo, Libro) in dataDB:
            data['Descripcion'] = Descripcion
            data['Consejo'] = Consejo
            data['Libro'] = Libro
        return data
    
    def get_user_login(self):
        usr = self.userList.get()
        query = f"SELECT * FROM users WHERE User = '{usr}'"
        dataDB = run_query(query)
        data = {}
        for (Id, User, Pass) in dataDB:
            data['Id'] = Id
            data['User'] = User
            data['Pass'] = Pass
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
        isSave = False
        try:
            run_query(query)
            isSave = True
        except Exception as e:
            self.message['text'] = f'Error al guardar datos {e}'
        return isSave
    
    def new_user(self):
        new_user_view()

    def delete_user(self):
        usr = self.userList.get()
        user = self.get_user_login()
        id = user['Id']
        msj = f'Eliminar registro: {usr}'
        msgb = messagebox.askquestion('Alerta', msj, parent=self.wind)
        if msgb == 'yes':
            usr = self.userList.get()

            query = f"DELETE FROM users WHERE Id = '{id}'"
            self.delete_sql(query)

            query1 = f"DELETE FROM persona WHERE User = '{usr}'"
            self.delete_sql(query1)

            query2 = f"DELETE FROM progreso WHERE User = '{usr}'"
            self.delete_sql(query2)

            self.message['text'] = f'Se elimino registro correctamente'
            self.clean_inputs()
            print('delete')

    def delete_sql(self, query):
        isSave = False
        try:
            run_query(query)
            isSave = True
        except Exception as e:
            self.message['text'] = f'Error al eliminar datos {e}'
        return isSave

    def exit_session(self):
        self.wind.destroy()
