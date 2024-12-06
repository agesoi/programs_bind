from tkinter import *
from tkinter import ttk, filedialog
from conf.add_to_json import Add_to_json
import keyboard



window = Tk()
window.geometry('200x200')
window.resizable(False, False)
window.iconbitmap(default="icon.ico")
window.title('programs_bind')



def select_file_path():
    global filepath
    filepath = filedialog.askopenfilename()
    print(filepath)
    
def bind():
    global bind_button
    bind_button = keyboard.record("esc")



def save():
    obj = Add_to_json()  # создаём экземпляр класса
    obj.add_app(path=filepath, btns=bind_button)  # вызываем метод через экземпляр

    
def create_bind():
    btn = ttk.Button(text="select file path", command=select_file_path)
    btn.pack(anchor=N, padx=6, pady=6)
    
    btn = ttk.Button(text="input bind", command=bind)
    btn.pack(anchor=N, padx=6, pady=6)
    
    btn = ttk.Button(text="Save", command=save)
    btn.pack(anchor=N, padx=6, pady=6)
    
    
btn = ttk.Button(text="Create bind", command=create_bind)
btn.pack(anchor=N, padx=6, pady=6)


window.mainloop()