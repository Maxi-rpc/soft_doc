# imports
import tkinter as tk

userProfile = {
    'user': 'maxirpc',
    'nombre': 'Maximiliano',
    'edad': 31
}

userProgress = {
    'user': userProfile['user'],
    'problema': 'Ansiedad',
    'objetivo': 'controlar la ansiedad generada'
}

userConsejo = {
    'problema': userProgress['problema'],
    'consejo': 'cambiar dieta',
    'actividad': 'hacer futbol pa'
}

class data_view:
    def __init__(self, user):
        # initializations
        self.user = user 
        self.wind = tk.Tk()
        self.wind.title('Data')
        self.wind.geometry('500x400')

        ### Persona
        # Frame Container 
        frame = tk.LabelFrame(self.wind, text = 'Datos del usuario')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 10)

        # text name
        tk.Label(frame, text = 'User: ').grid(row = 1, column = 0)
        self.user = tk.Entry(frame)
        self.user.insert(0, userProfile['user'])
        self.user.grid(row = 1, column = 1)
        self.user.config(state='readonly')

        # text edad
        tk.Label(frame, text = 'Nombre: ').grid(row = 2, column = 0)
        self.name = tk.Entry(frame)
        self.name.insert(0, userProfile['nombre'])
        self.name.grid(row = 2, column = 1)
        self.name.config(state='readonly')

        # text edad
        tk.Label(frame, text = 'Edad: ').grid(row = 3, column = 0)
        self.age = tk.Entry(frame)
        self.age.insert(0, userProfile['edad'])
        self.age.grid(row = 3, column = 1)
        self.age.config(state='readonly')

        ### Progreso
        # Frame Container 
        frame_prog = tk.LabelFrame(self.wind, text = 'Progreso')
        frame_prog.grid(row = 4, column = 0, columnspan = 10, pady = 10)

        # text problema
        tk.Label(frame_prog, text = 'Problema: ').grid(row = 1, column = 0)
        self.prob = tk.Text(frame_prog, height=1, width=40)
        self.prob.insert(tk.END, userProgress['problema'])
        self.prob.grid(row = 1, column = 1)
        self.prob.config(state='disabled')

        # text objetivo
        tk.Label(frame_prog, text = 'Objetivo: ').grid(row = 2, column = 0)
        self.objet = tk.Text(frame_prog, height=2, width=40)
        self.objet.insert(tk.END, userProgress['objetivo'])
        self.objet.grid(row = 2, column = 1)
        self.objet.config(state='disabled')


        ### Consejo
        # Frame Container 
        frame_prog = tk.LabelFrame(self.wind, text = 'Recomendaciones')
        frame_prog.grid(row = 7, column = 0, columnspan = 10, pady = 10)

        # text consejo
        tk.Label(frame_prog, text = 'Consejo: ').grid(row = 1, column = 0)
        self.prob = tk.Text(frame_prog, height=1, width=40)
        self.prob.insert(tk.END, userConsejo['consejo'])
        self.prob.grid(row = 1, column = 1)
        self.prob.config(state='disabled')

        # text actividad
        tk.Label(frame_prog, text = 'Actividad: ').grid(row = 2, column = 0)
        self.objet = tk.Text(frame_prog, height=2, width=40)
        self.objet.insert(tk.END, userConsejo['actividad'])
        self.objet.grid(row = 2, column = 1)
        self.objet.config(state='disabled')

        ### Editar
        # Frame Container 
        frame_btn = tk.Frame(self.wind)
        frame_btn.grid(row = 8, column = 0, columnspan = 2, pady = 50, padx= 50)
        # Button Add Product 
        btnEdit = tk.Button(frame_btn, text = 'Editar', command = self.edit_user)
        btnEdit.grid(row = 1, columnspan = 2, sticky = tk.W + tk.E)


        self.wind.mainloop()

    def edit_user(self):
        print('a editar user')

    # User Input Validation
    def validation(self):
        return len(self.name.get()) != 0 and len(self.password.get()) != 0
    
    def login(self):
        if self.validation():
            print(self.name.get(), self.password.get())
        else:
            self.message['text'] = 'Completar campos'
