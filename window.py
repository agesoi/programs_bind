from tkinter import *
from tkinter import ttk


window = Tk()
window.geometry('500x500')

def night_theme():
    window['bg'] = '#000000'
    

btn = ttk.Button(text='night theme', width=20, command=night_theme)
btn.pack(expand=True, ipadx=10, ipady=10)

window.mainloop()