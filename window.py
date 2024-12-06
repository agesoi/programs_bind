from tkinter import *
from tkinter import ttk, filedialog




window = Tk()
window.geometry('200x200')
window.resizable(False, False)
window.iconbitmap(default="icon.ico")
window.title('programs_bind')

def select_file_path():
    global filepath
    filepath = filedialog.askopenfilename()
    print(filepath)
    
    
def create_bind():
    btn = ttk.Button(text="select file path", command=select_file_path)
    btn.pack(anchor=N, padx=6, pady=6)
    
    btn = ttk.Button(text="input bind", command=None)
    btn.pack(anchor=N, padx=6, pady=6)
    
    btn = ttk.Button(text="Save")
    btn.pack(anchor=N, padx=6, pady=6)
    
    
btn = ttk.Button(text="Create bind", command=create_bind)
btn.pack(anchor=N, padx=6, pady=6)


window.mainloop()
