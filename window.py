from tkinter import *
from tkinter import ttk




window = Tk()
window.geometry('500x500')
window.resizable(False, False)
window.iconbitmap(default="icon.ico")
window.title('programs_bind')


def select_file_path():
    label = ttk.Label(text="select file path:")
    label.pack(anchor=W, padx=6, pady=6)

    entry = ttk.Entry()
    entry.pack(anchor=W, padx=6, pady=6)
    
    global path_entry
    path_entry = entry.get()
    
    btn = ttk.Button(text="Save")
    btn.pack(anchor=W, padx=6, pady=6)
    
    
btn = ttk.Button(text="Create bind", command=select_file_path)
btn.pack(anchor=N, padx=6, pady=6)


window.mainloop()
