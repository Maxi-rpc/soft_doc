# imports
import tkinter as tk
from view_login import login_view

# config ventana
configScreen = {
    'title': 'App Doc',
    'width': 500,
    'height': 400,
    'widthXheight': '600x500'
}

# functions

# main
def main():
    # tk
    root = tk.Tk()
    root.title(configScreen['title'])
    #root.minsize(width=configScreen['width'], height=configScreen['height'])
    #root.geometry(configScreen['widthXheight'])

    application = login_view(root)

    root.mainloop()

main()